from flask import Flask, request,render_template, redirect, url_for, make_response, session, Response, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ, path
import sys
import hashlib
import jwt
from flask_migrate import Migrate
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = environ.get('SECRET_KEY')

sys.path.append('./Middleware/')
from auth import getSessionUser

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=environ.get('POSTGRES_USER'),
    pw=environ.get('POSTGRES_PASSWORD'),
    url=environ.get('POSTGRES_URL'),
    db=environ.get('POSTGRES_DB')
)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['SECURITY_PASSWORD_SALT'] = "MY_SECRET"
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False
app.config['COUNTRIES'] = ['animals', 'cyber', 'plants', 'urban']
app.config['ACCESS_DASHBOARD'] = ['SUPER_ADMIN', 'ADMIN_ANIMALS', 'ADMIN_CYBER', 'ADMIN_PLANTS',  'ADMIN_URBAN']

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cosmo = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    roles = db.Column(db.String(100), nullable=True)

    def __init__(self, name, surname, email, cosmo, password, roles):
        self.name = name
        self.surname = surname
        self.email = email
        self.cosmo = cosmo
        self.password = password
        self.roles = roles

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home/home.html')

@app.route('/signup', methods=['GET', 'POST'])
@getSessionUser
def signup():
    if request.user:
        return redirect(url_for('home'))        
    if request.method == 'POST':
        # POST_get.getSessionUser
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        password = request.form['password']
        cosmo = request.form['cosmo']        

        if Users.query.filter_by(email=email).first() is not None:
            flash('Email already exists', 'danger')
            return redirect(url_for('signup'))

        password = hashlib.md5(password.encode("utf8")).hexdigest() 

        new_user = Users(name=name, 
                        surname=surname,
                        email=email,
                        password=password,
                        cosmo=cosmo,
                        roles="['USER']")


        db.session.add(new_user)
        db.session.commit()
        # getSessionUser(f)
        # @Wrap(f)
        token = jwt.encode({
            'id': new_user.id,
            'name': new_user.name,
            'surname': new_user.surname,
            'email': new_user.email,
            'roles': new_user.roles,
                }, app.config['SECRET_KEY'], algorithm='HS256')
        
        response = make_response(redirect(url_for('home')))
        response.set_cookie('SESSION', token)
        return response


    return render_template('home/user/signup.html')


#------------login---------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('home/user/login.html')

#------------appFlask------------------------
if __name__ == '__main__':
        app.run(host='0.0.0.0',port=environ.get('PORT'),debug=environ.get('DEBUG'))

        