# Yatube API

Проект реализации API для [социальной сети Yatube](https://github.com/Techinek/simple_social_network_yatube). 
Благодаря данному API клиент может:
- аутентифицироваться по токену;
- добавлять/удалять/редактировать посты;
- добавлять/удалять/редактировать комментарии;
- подписываться на автора.

#### Стек:
- Python 3.7
- Django 2.2.19
- djangorestframework 3.12.4
- djangorestframework-simplejwt 4.7.2

#### Примеры запросов:
```
- GET api/v1/posts/ - получить список всех публикаций (при указании параметров limit и offset 
выдача должна работать с пагинацией);
- GET api/v1/posts/{id}/ - получение публикации по id;
- GET api/v1/groups/ - получение списка доступных сообществ;
- GET api/v1/groups/{id}/ - получение информации о сообществе по id;
- GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации;
- GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id.
```
Полная документация по API доступна по адресу: http://localhost:8000/redoc/

#### Установка:

1. Клонируем репозиторий на локальную машину:
`$ git clone https://github.com/Techinek/simple_social_network_yatube.git`

2. Создаем виртуальное окружение(Linux):
`$ python -m venv venv`

3. Устанавливаем зависимости:
`$ pip install -r requirements.txt`

4. Создаем и применяем миграции:
`$ python manage.py makemigrations и $ python manage.py migrate`

5. Запускаем локальный django-сервер:
`$ python manage.py runserver`
