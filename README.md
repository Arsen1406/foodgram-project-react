# praktikum_new_diplom

## Описание проекта

Сайт для создания и просмотра рецептов для приготовления вкусных блюд. Так же можно скачать список рецептов.
Пользователи могут подписываться друг на друга, добавлять в избранное рецепты, а там же создавать и редактировать свои рецепты.


## Технологии
- Python
- Django
- DjangoRestFramework
- JavaScript
- React

## Системные требования

| Процессор  | ОЗУ  | Память |
| :------------ |:---------------:| -----:|
| 4 ядра      | 4 GB | 8 GB |
                
----

## Запуск проекта
Клонируйте проект на свою машину

`git clone <ssh ссылка на проект>`

Перейдите в папку с файлом с проектом

`cd foodgram-project-react`

Создайте виртуальное окружение и активируйте его

`python -m venv venv`

`source venv/bin/activate`

Перейдите в дирректорию с бекэндом приложения, обновите pip и установите зависимости
```
cd backend/foodgram
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Создайте .env-файл в нем укажите слдующие ключи

```
SECRET_KEY=some-secret-key
DEBUG=1
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=название для бызы данных
DB_USER=username
DB_PASSWORD=пароль для username
DB_HOST=host
DB_PORT=port
``` 

## Запуск проекта

Перейдите в дирректорию /infra, там поочередно выполните комманды:

```
sudo docker compose up -d
sudo docker exec -it backend python manage.py migrate 
sudo docker exec -it backend python manage.py createsuperuser
sudo docker exec -it backend python manage.py importingredients ingredients.json
```


Запустится весь проект.
```
API - http://localhost/
Redoc - http://localhost/api/docs/
Frontend - http://localhost/
Админка - http://localhost/admin/
```

## Автор
Григорян Арсен
