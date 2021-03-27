# Example Environment for Django, MariaDB, NginX, Gunicorn using Docker 

> Languages: [English](./README.md) | [中文](./doc/README_zh_CN.md)

## Introduction

This is a Docker setup for a web application based on Django.

- The Django application is served by Gunicorn (WSGI application).
- We use NginX as reverse proxy and static files server. Static files are persistently stored in volumes.
- MariaDB is used. Data are persistently stored in local files.
- Python dependencies are managed through pipenv, with Pipfile and Pipfile.lock.

Also a Makefile is available for convenience. You might need to use `sudo make` instead of just `make` because docker and docker-compose commands often needs admin privilege.

**Note: `Make` command may not run on Windows !**

## Requirement
You need to install [Docker](https://www.docker.com/) and [Docker-Compose](https://docs.docker.com/compose/).

## Quick Start

In the first time, you should execute these commands step by step.

### Backend


``` shell
    docker-compose build
    docker-compose run --rm django answerplatform/manage.py migrate
    docker-compose run --rm django answerplatform/manage.py collectstatic --no-input
    docker-compose down
    docker-compose up
```

The server will run on port `8000`, so you can visit [localhost/backend/admin/](localhost/backend/admin/) to access to your Django server.

Stop the Django server with:

```shell
    docker-compose down
```

### Frontend

#### In **DEV (develop environment)**

``` shell
    cd frontend
    npm run serve
```

The frontend will serve on [localhost:8080](localhost:8080)
