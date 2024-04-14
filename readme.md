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

### Run Docker Flask Application

```
cd back_end
```
```
docker-compose build web
```
```
docker-compose up web
```
### first basic app
Let's start the service with a first simple route [Flask](https://flask.palletsprojects.com/en/3.0.x/), so as to display a [return](https://flask.palletsprojects.com/en/3.0.x/quickstart/#routing) message on the page:
```
from flask import Flask

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
    app.run(host='0.0.0.0', port=5000, debug=True)

```
focus on this part of the code, which is essential for starting the services
- The if __name__ == '__main__': part in the main.py Python code and the services configuration in the docker-compose.yml file are both responsible for starting the Flask application within a Docker environment.
- In the Python main.py code, this condition if __name__ == '__main__': is used to test whether the Python script was executed directly, rather than imported as a module in another script.
- If run directly, the app.run() function is called, which launches the Flask application on a local web server. With the parameters host='0.0.0.0' and port=5000, the Flask application will be accessible on all network interfaces (0.0.0.0) on port 5000. Additionally, debug=True enables Flask's debug mode.

> [!NOTE]
> In the docker-compose.yml file, in the services section, the web service is configured to build the backend, mounting the source code from ./back_end inside the Docker container. The ports configuration maps port 5000 of the container to port 5000 of the host, thus allowing you to access the Flask application through the browser or another client application. The environment variables defined in the environment section are passed to the Flask application as environment variables, allowing dynamic configuration of the application. Finally, depends_on specifies that the web service depends on the db service, ensuring that the db service is started before the web service. 👉[take a look](https://github.com/JungleKiosk/DockerFlask_pgAdmin) 









