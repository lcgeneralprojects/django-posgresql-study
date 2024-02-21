# django-postgresql study
[![en](https://img.shields.io/badge/lang-en-red)](https://github.com/lcgeneralprojects/django-posgresql-study/blob/main/README.md)
[![ru](https://img.shields.io/badge/lang-ru-green)](https://github.com/lcgeneralprojects/django-posgresql-study/blob/main/README.ru.md)

A simple blog project, meant to be proof of basic competence in working with the technologies of Django and PostgreSQL.

There are two intended ways of starting the server.
First, one should navigate tho the `server/` subdirectory of the project, and then executing one of the following commands:
- to start the server directly, use the command `python manage.py runserver`.
- to start the server using Docker, use the command `docker-compose up [--build]`.

Currently, the application allows a user to register, log in, view, post, edit, and delete comments. The access to this functionality is provided by the links in the header of the project's pages.
