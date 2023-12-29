## Eazzy-Quizzy - мини-сервис для создания квизов и тестов

### Описание
Мини-сервис для прохождения квизов. Создание квизов - через админ-панель. Скриншоты в конце описания

### Используемые технологии:
![image](https://img.shields.io/badge/Python%203.11-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/Django%204.2-092E20?style=for-the-badge&logo=django&logoColor=green)
![image](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![image](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![image](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![image](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![image](https://img.shields.io/badge/Poetry-100000?style=for-the-badge&logoColor=white)

### Доступные возможности
- Регистрация / аутентификация пользователей
- Главная страница со списком квизов и статистиков их прохождения (для аутентифицированных пользователей)
- Просмотр страницы квиза с общей информацией и историей попыток
- Прохождение квиза (каждый вопрос на отдельном экране; пропускать и возвращаться нельзя); один/несколько вариантов ответов
- Админка для создания квизов и вопросов

### Установка
#### Создать файл с переменными окружения (можно переименовать шаблон .env.example)
```
SECRET_KEY='django-insecure-super-secret'
DEBUG=False
ALLOWED_HOSTS='localhost, 127.0.0.1'
TRUSTED_ORIGINS='http://127.0.0.1, http://127.0.0.1:8000'

POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

ADMIN_EMAIL=admin@admin.admin
ADMIN_PASSWORD=Qwerty-123
```

#### Стандартное разворачивание:
```
git clone git@github.com:ratarov/eazy-quizzy.git
cd eazzy-quizzy
py -m venv venv
pip install poetry
poetry install
python manage.py migrate
python manage.py runserver
```

#### Docker:
```
git clone git@github.com:ratarov/eazy-quizzy.git
cd eazzy-quizzy
docker-compose up -d --build
```
Сайт доступен по адресу http://127.0.0.1:8000/, добавлен суперпользователь с данными из .env

### Как выглядит фронт
![image](https://github.com/ratarov/eazy-quizzy/blob/main/static/screenshots/1.png) <br>
![image](https://github.com/ratarov/eazy-quizzy/blob/main/static/screenshots/2.png) <br>
![image](https://github.com/ratarov/eazy-quizzy/blob/main/static/screenshots/3.png) <br>
![image](https://github.com/ratarov/eazy-quizzy/blob/main/static/screenshots/4.png) <br>
![image](https://github.com/ratarov/eazy-quizzy/blob/main/static/screenshots/5.png) <br>