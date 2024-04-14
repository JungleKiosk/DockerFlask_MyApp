from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from os import environ
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'my_secret'


DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=environ.get('POSTGRES_USER'),
    pw=environ.get('POSTGRES_PASSWORD'),
    url=environ.get('POSTGRES_URL'),
    db=environ.get('POSTGRES_DB')
)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cosmo = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
       
    def __init__(self, name, surname, email, cosmo, password, password_hash):
        self.name = name
        self.surname = surname
        self.email = email
        self.cosmo = cosmo
        self.password = password
        self.password_hash = generate_password_hash(password_hash)

 
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home/home.html')

@app.route('/login')
def login():
      return render_template('home/user/login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        password = request.form['password']
        cosmo = request.form['cosmo']

        existing_user = Users.query.filter_by(email=email).first()

        if existing_user:
            flash('Email already exists, please choose another one', 'error')
            return redirect(url_for('signup'))

        password_hash = generate_password_hash(password)

        new_user = Users(
            name=name,
            surname=surname,
            email=email,
            cosmo=cosmo,
            password=password,
            password_hash=password_hash
        )
        db.session.add(new_user)
        db.session.commit()
        
        flash('User registered successfully', 'success')
        return redirect(url_for('login'))

    return render_template('home/user/signup.html')



if __name__ == '__main__':
        app.run(host='0.0.0.0',port=environ.get('PORT'),debug=environ.get('DEBUG'))