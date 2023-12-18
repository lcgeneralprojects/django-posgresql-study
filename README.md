# django-postgresql study
A simple blog project, meant to be proof of basic competence in working with the technologies of Django and PostgreSQL.

There are two intended ways of starting the server.
First, one should navigate tho the `server/` subdirectory of the project, and then executing one of the following commands:
- to start the server directly, use the command `python manage.py runserver`.
- to start the server using Docker, use the command `docker-compose up [--build]`.

Currently, the project allows a user to register, log in, post comments, and view comments. The access to this functionality is provided by the links in the header of the project's pages.