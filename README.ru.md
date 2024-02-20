# django-postgresql study
[![en](https://img.shields.io/badge/lang-en-red)](https://github.com/lcgeneralprojects/django-posgresql-study/blob/development/README.md)
[![ru](https://img.shields.io/badge/lang-ru-green)](https://github.com/lcgeneralprojects/django-posgresql-study/blob/development/README.ru.md)

Простой проект-блог, предназначенный для доказательства базовой компетенции в области работы с технологиями Django и PostgreSQL.

На данный момент подразумевается два способа запуска сервера.
Для начала пользователь должен перейти в поддиректорию `server/` и запустить выполнение одной из следующих команд:
- чтобы запустить сервер напрямую, пользователю нужно воспользоваться командой `python manage.py runserver`
- чтобы запустить сервер с помощью Docker, пользователю нужно воспользоваться командой `docker-compose up [--build]`.

На данный момент приложение позволяет пользователю регистрироваться, заходить в свою учетную запись, видеть комментарии, а также оставлять, редактировать и удалять их. Доступ к этим возможностям предоставляется с помощью ссылок в головном элементе страниц проекта.
