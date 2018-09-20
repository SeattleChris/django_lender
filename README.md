# django_lender

**Author**: Chris L Chapman
**Version**: 0.2.0 (increment the patch/fix version number up if you make more commits past your first submission)

## Overview

Introduction to the concept of Docker and working within containers as a part of the developer workflow. In addition to Docker, this will explore building my first Django web application.

Continue building an application for managing all the various books you own (lets assume you own a lot…). In order to implement this application, you will need to iterate on your django_lender application and add a model, views (templates), and controllers (views).

## Getting Started

Install Docker and compose according to the steps starting from these sites:
https://docker-curriculum.com/#table-of-contents
https://docs.docker.com/compose/django/
https://www.pluralsight.com/codeschool

pipenv shell
docker-compose up -- build

docker container ls (to copy image for either the web or database)
docker exec -it [web_image_number] bash (command line in container)
 (not needed since in entrypoint.sh)./manage.py runserver

docker exec -it [postgres_image_number] psql -U postgres
    to login and see the DB and tables.

docker-compose down
