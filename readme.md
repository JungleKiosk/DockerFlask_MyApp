# Flask App🐍with Docker🌊🐋🌊& postgreSQL🌴🐘🌴

This is a simple [Flask](https://flask.palletsprojects.com/en/3.0.x/) application with Docker and pgAdmin integration, allowing you to quickly set up a web application backed by a PostgreSQL database.

## Prerequisites
Before you begin, ensure you have the following installed:

- Docker: [Install Docker](https://docs.docker.com/engine/install/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

### Work Directory
```
back_end|
        |-assets
        |-templates
        |-Dockerfile
        |-main.py
        |-requirements.txt
docker-compose.yml
readme.md
```

### Setting dependencies in requirements.txt
The **requirements.txt** file is a text file used to list all the Python dependencies needed for the project. Each line of the file contains the name of a Python package and, optionally, the package version. When you use the pip tool to install dependencies, pip will read this file and automatically install all listed dependencies.

### Using requirements.txt in Docker Compose
In the context of Docker Compose, the **requirements.txt** file is used to specify the dependencies of the Flask container. When Docker Compose builds the container for your Flask application, it reads the requirements.txt file and installs all the dependencies listed within the container. This ensures that all necessary dependencies are present within the container and ready for the application to run.

- To get started, import the **Flask** dependencies into the requirements.txt file by simply typing `flask`

![reqtxt](/back_end/assets/img/readme/1_reqtxt.png)

> [!IMPORTANT]
> Quando si avvia un nuovo ambiente di sviluppo o si distribuisce l'applicazione su un server, è possibile utilizzare il file requirements.txt per installare tutte le dipendenze necessarie con un singolo comando: `pip install -r requirements.txt`

> [!CAUTION]
> Nel contesto Docker Compose Il file requirements.txt viene chiamato dal **Dockerfile** (💡ricorda: Dockerfile è all'interno della cartella back_end insieme al file main.py e al file requirements.txt 🤓)

### Create Docker Compose & PostgreSQL environment 

Please refer to the repo dedicated to creating the [Docker Compose](https://github.com/JungleKiosk/DockerFlask_pgAdmin) environment

> [!IMPORTANT]
> It is important to note that the Flask service depends on the PostgreSQL (db) database service, so Docker Compose ensures that the database service is started before the Flask service.

> [!CAUTION]
> First the Docker Compose image must be built and run, and only then can the server be created in pgAdmin, otherwise it would lead to errors 👉[take a look](https://github.com/JungleKiosk/DockerFlask_pgAdmin) 

### How to Run Docker Flask Application 🚀

```
cd back_end
```
```
docker-compose build web
```
```
docker-compose up web
```

**the application is empty, to display a first route in the browser DOM it is necessary to write and run the main.py file from the service 👇**

### first basic app
```
from flask import Flask
from os import environ

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello Flak'

if __name__ == '__main__':
        app.run(host='0.0.0.0',port=environ.get('PORT'),debug=environ.get('DEBUG'))
```
- explanation:
Let's start the service with a first simple route [Flask](https://flask.palletsprojects.com/en/3.0.x/), so as to display a [return](https://flask.palletsprojects.com/en/3.0.x/quickstart/#routing) message on the page:
```
from flask import Flask
from os import environ

```
1) This line imports the Flask class from the flask module, which is the lightweight web framework used to build the application
```
app = Flask(__name__)

```
2) This instance is a predefined variable in Python that represents the name of the current module. By passing this to Flask, we are telling Flask to use the current module name to resolve static resources, such as CSS files, JavaScript, etc.
```
@app.route('/')

```
3) This is a function [decorator](https://flask.palletsprojects.com/en/3.0.x/patterns/viewdecorators/) that defines a route. Indicates that the following function (home()) should be executed when the home route ('/') is requested.
```
def home():
    return 'Hello Flask'

```
4) This is the function associated with the main route. When the `'/'` route is requested, this function executes and returns the string `'Hello Flask'`.
```
if __name__ == '__main__':
        app.run(host='0.0.0.0',port=environ.get('PORT'),debug=environ.get('DEBUG'))

```
focus on this part of the code, which is essential for starting the services
- The `if __name__ == '__main__'`: part in the main.py Python code and the services configuration in the docker-compose.yml file are both responsible for starting the Flask application within a Docker environment.
- In the Python main.py code, this condition` if __name__ == '__main__'` is used to test whether the Python script was executed directly, rather than imported as a module in another script.
- `environ.get('PORT')` viene utilizzato per recuperare il valore della variabile d'ambiente PORT, che specifica la porta su cui l'applicazione Flask sarà in ascolto. Questo consente di configurare dinamicamente la porta senza dover modificare direttamente il codice.
- `environ.get('DEBUG')` viene utilizzato per recuperare il valore della variabile d'ambiente DEBUG, che determina se la modalità di debug di Flask sarà abilitata ('1' per abilitato, None o qualsiasi altro valore per disabilitato).

> [!IMPORTANT]
> In the docker-compose.yml file, in the services section, environment variables are defined for the web service: `DEBUG=1` sets Flask's debug mode to enabled. `PORT=5000` specifies the port on which the Flask application will listen. 👉[take a look](https://github.com/JungleKiosk/DockerFlask_pgAdmin) 

> [!IMPORTANT]
> In the docker-compose.yml file, in the services section, the web service is configured to build the backend, mounting the source code from `./back_end` inside the Docker container. The ports configuration maps `port 5000` of the container to `port 5000` of the host, thus allowing you to access the Flask application through the browser or another client application. The environment variables defined in the environment section are passed to the Flask application as environment variables, allowing dynamic configuration of the application. Finally, depends_on specifies that the web service depends on the db service, ensuring that the db service is started before the web service. 👉[take a look](https://github.com/JungleKiosk/DockerFlask_pgAdmin)

>[!NOTE]
> In the context of the provided Python code, the `host='0.0.0.0'` option in the invocation of app.run() specifies the IP address on which the Flask application will listen.In the context of Docker Compose, when defining a service, such as in your docker-compose.yml file, setting IP addresses is not as explicit as in the Flask application. By default, Docker Compose creates a virtual network for the services defined in the docker-compose.yml file, and the services can communicate with each other using the service names as hostnames.So, when the Flask service defines `host='0.0.0.0'`, it is telling Flask to listen on all available network interfaces, making the application available from any IP address within the Docker container network.In the context of Docker Compose, the Flask service is exposed to the outside world through port mapping in the docker-compose.yml file, for example ports: - 5000:5000. This means that the Flask service is accessible from outside the Docker container on `port 5000`.

## HTTP protocol 💻 -> 🗃️ -> 🌐 -> 💻
> [!NOTE]
> The HTTP protocol is the foundation of data communication on the web. In this protocol, several methods are defined that are used to retrieve data from the given URL.

### Record the data in the DB PostgreSQL 🌴🐘🌴
### Import [SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/) ⚗️
- initialize the Flask application
- configure the SQLAlchemy database
- defines the table structure in the database
#### Dependences
```
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from os import environ
```
- Flask: Framework for developing web applications in Python.
render_template, request, redirect, url_for, flash: Flask modules for handling HTTP requests, rendering HTML templates, redirecting requests, and handling flash messages.
- SQLAlchemy: Python library for interfacing with relational databases.
- environ: Function for accessing the operating system's environment variables.

#### Secret Key 🔑🍪
```
app = Flask(__name__)
app.secret_key = 'my_secret'
```
- A Flask object called app is created.
- The secret_key is set to enable session features and cookie encryption.

#### URL of the DB
```
DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=environ.get('POSTGRES_USER'),
    pw=environ.get('POSTGRES_PASSWORD'),
    url=environ.get('POSTGRES_URL'),
    db=environ.get('POSTGRES_DB')
)
```
- The PostgreSQL database URL is created using environment variables for the user, password, database URL, and database name.

#### Database setup in Flask application
```
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
```
- The database URI is set in the app.config object of the Flask application. This tells SQLAlchemy how to connect to the database.

#### Initializing SQLAlchemy extension ⚗️ 
```
db = SQLAlchemy(app)
```
- The SQLAlchemy extension is initialized by passing the app object.

#### Create table in DB
```
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
```
- A Users class is defined that inherits from SQLAlchemy's `db.Model` class.
- The name of the table in the database `(__tablename__)` is specified.
- The table fields (id, name, surname, email, cosmo, password) are defined with their respective data types and constraints.

#### Creating tables in the database
```
with app.app_context():
    db.create_all()
```
- The table in the database is created using the Flask application context (app.app_context()). This ensures that the table creation operation is performed within the correct environment.

*Quick Refresher*
- Il metodo GET viene utilizzato per recuperare le informazioni dal server. Quando si accede alla rotta /signup tramite il metodo GET, il server restituirà la pagina HTML corrispondente al form di registrazione (render_template('home/user/signup.html')).

- Il metodo POST viene utilizzato per inviare dati al server per essere elaborati. Quando si invia il form compilato dalla pagina di registrazione, i dati vengono inviati al server utilizzando il metodo POST. Il server quindi riceve questi dati e li elabora, come nel caso della funzione signup(). Questo metodo è utilizzato per inviare informazioni sensibili, come password e altre informazioni personali, in modo sicuro al server.






