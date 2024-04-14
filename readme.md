# Flask App 🌳🐍🌳 with Docker 🌊🐋🌊 & postgreSQL 🌴🐘🌴

This is a simple Flask application with Docker and pgAdmin integration, allowing you to quickly set up a web application backed by a PostgreSQL database.

## Prerequisites
Before you begin, ensure you have the following installed:

- Docker: [Install Docker](https://docs.docker.com/engine/install/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

### Work Directory
```
back_end|
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







