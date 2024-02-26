# Welcome to Blogging Complete Backend with Django Rest Framework.

## This Project Covers
- How to use Docker with Celery, Redis, Flower with Django REST Framework<br>
- How to use Reverse Proxies with NGINX and NGINX Proxy Manager <br>
- How to Secure an API with HTTPS with SSL Certificates from Letsencrypt<br>
- API testing with Pytest using factories and fixtures<br>
- How to manage multiple Docker containers with Portainer<br>
- How to use shell scripts to automate and monitor processes<br>
- How to implement Asynchronous tasks with Celery and Redis<br>
- How to Serve static and media files with Nginx and Whitenoise.<br>
- How to implement Asynchronous tasks monitoring with Flower<br>
- How to work with Postgres within a Docker container, including how to perform backups using shell scripts.<br>
- How to setup an Ubuntu server, running Django over a Domain name.<br>
- How to use makefiles to make working with Docker easier.<br>
- Searching functionalities using elastic search<br>
- Python Test coverage using coverage<br>
- Logging in Django<br>
- Token Based Authentication<br>
- Working with emails using Mailhog in development and Mailgun in production.<br>



## Features

- User registration and authentication
- Creating, editing, and deleting blog posts
- Liking and commenting on blog posts
- Following other users and receiving notifications
- Categorizing blog posts using tags
- Searching for blog posts by keywords or tags
- Pagination and sorting of blog posts
- User profiles with bio and profile picture
- User activity feed
- Email notifications using MailHog
- Asynchronous task processing using Celery and Redis
- Monitoring and management of Celery tasks using Flower
- Containerized deployment using Docker and Docker Compose
- Reverse proxy and load balancing using Nginx


## Technologies

- [Python](https://www.python.org/) - Programming language
- [Django](https://www.djangoproject.com/) - Web framework
- [Django REST framework](https://www.django-rest-framework.org/) - Toolkit for building APIs
- [PostgreSQL](https://www.postgresql.org/) - Relational database management system
- [Redis](https://redis.io/) - In-memory data structure store
- [Celery](http://www.celeryproject.org/) - Distributed task queue
- [Flower](https://flower.readthedocs.io/) - Monitoring and management tool for Celery
- [Docker](https://www.docker.com/) - Containerization platform
- [Docker Compose](https://docs.docker.com/compose/) - Tool for defining and running multi-container Docker applications
- [Nginx](https://www.nginx.com/) - Web server and reverse proxy
- [Elasticsearch](https://www.elastic.co/elasticsearch/) - Distributed search and analytics engine
- [MailHog](https://github.com/mailhog/MailHog) - Email testing tool

## Prerequisites

Make sure you have the following technologies installed on your machine:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/samsorrahman/Advance-Backend-Blogging-with-DRF.git

2. Navigate to the project directory::

   ```bash
   cd src

3. Build the Docker containers and start the application:

   make build

Download insomnia and add the api.har file 

![Capture](https://github.com/samsorrahman/Advance-Backend-Blogging-with-DRF/assets/112087807/d24d3dcc-2341-425c-875a-c05fca14b4fe)

4. Once the containers are built and the application is running, you can access the following resources:

    Documentation: Open your web browser and visit `localhost:8080/redoc` to access the API documentation.

    Flower (Celery monitoring): Open your web browser and visit `localhost:5555` to access Flower, the monitoring and management tool for Celery tasks.

    MailHog (Email server): Open your web browser and visit `localhost:8025` to access MailHog, the email testing tool. You can view the email notifications sent by the application here.

## Additional Commands

The `Makefile` in the project contains other useful commands for managing the application. Some of the commonly used commands are:

Make sure to stop the application containers when you are done by running:
make down

## Complete Test Coverage

[index.pdf](https://github.com/samsorrahman/Advance-Backend-Blogging-with-DRF/files/14409301/index.pdf)

<h5>If you are on windows system: You Must Learn How to Run a Makefile in Windows</h5>
<p><a href="https://medium.com/@samsorrahman/how-to-run-a-makefile-in-windows-b4d115d7c516" target="blank">Here what I have brought for you!</a></p>
checkout the requirement folder for dependencies installation.


