# Docker大礼包

> 语言: [English](./README.md) | [中文](./doc/README_zh_CN.md)


## 简介

基于Django的web应用的Docker环境

- Django应用由Gunicorn提供。
- 使用Nginx来作为反向代理、静态文件服务器。静态文件被持久化储存在目录下。
- 该环境使用了Mariadb，数据被持久化存储在本地文件中。
- 通过pipenv管理python的依赖，使用了Pipfile和Pipfile.lock。

## 依赖

你需要安装[Docker](https://www.docker.com/) 和 [Docker-Compose](https://docs.docker.com/compose/)。

## 快速上手

### 后端服务

当你第一次使用该项目时，你应该一步步执行下边的命令。


```shell
docker-compose build
docker-compose run --rm django answerplatform/manage.py migrate
docker-compose down
docker-compose run --rm django answerplatform/manage.py collectstatic --no-input
docker-compose down
docker-compose up
```

服务端会运行在容器的`8000`端口，你可以通过访问[localhost/backend/admin/](localhost/backend/admin/)来访问后端服务。

当你想要停止服务端时：

```shell
django-compose down
```

### 前端服务

- 当你在开发环境下，通过运行下方的命令来启动前端服务。

```shell
cd frontend
npm run serve
```

当命令执行完成后，你可以通过在浏览器中输入 [localhost:8080](localhost:8080) 去访问你的前端页面。

