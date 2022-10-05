### Адрес проекта:

http://62.84.114.84/recipes

### Админка:

**address:** http://62.84.114.84/admin/

**login:** admin@admin.com

**pswrd:** admin

# **Продуктовый помощник FOODGRAM**

[![foodgram_workflow](https://github.com/v4lerdon/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)](https://github.com/v4lerdon/foodgram-project-react/actions/workflows/foodgram_workflow.yml)

На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

## **Оглавление**

[Описание проекта](#Продуктовый-помощник-FOODGRAM)

[Запуск проекта локально](#как-запустить-проект-локально-(только-API))

[Запуск проекта с помощью Docker](#как-запустить-проект-локально-с-помощью-docker)

[Деплой на боевой сервер](#как-задеплоить-проект-на-сервер-по-ssh)

[Шаблон .env](#шаблон-env)

### **Как запустить проект локально (только API):**
<a name='Запуск проекта локально'></a>
Клонировать репозиторий с [GitHub](https://github.com/v4lerdon/foodgram-project-react)
```
git@github.com:v4lerdon/foodgram-project-react.git
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### **Как запустить проект локально с помощью Docker:**
<a name='Запуск проекта через Docker'></a>

Установить [Docker](https://www.docker.com/get-started/)

Клонировать репозиторий с [GitHub](https://github.com/v4lerdon/foodgram-project-react)
```
git clone git@github.com:v4lerdon/foodgram-project-react.git
```
Перейти в папку с docker-compose.yaml
```
cd infra
```
В папке infra создайте файл и назовите его .env
```
new-item .env (для powershell)
```
Для заполнения .env используйте следующий [шаблон](#шаблон-env)

Выполните сборку и запуск контейнера
```
docker-compose up -d
```
Выполните миграции
```
docker-compose exec backend python manage.py migrate
```
Создайте суперпользователя
```
docker-compose exec backend python manage.py createsuperuser
```
Скопируйте статику
```
docker-compose exec backend python manage.py collectstatic --no-input
```
Документация будет доступна по адресу:
```
http://localhost/api/schema/redoc/
```


### **Как задеплоить проект на сервер по ssh**
<a name='Деплой на боевой сервер'></a>

Создайте виртуальную машину и подключитесь к ней при помощи консоли по ssh
```
ssh <username>@<ip-сервера>
```
установите python и git
```
sudo apt install python3-pip python3-venv git -y
```
установите docker
```
sudo apt install docker.io
```
установить docker-compose
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```
клонируйте репозиторий с проектом
```
git clone git@github.com:v4lerdon/foodgram-project-react.git
```
перейдите в папку infra
```
cd infra
```
создайте файл .env по [шаблону](#шаблон-env)
```
sudo nano .env
```
запустите docker-compose и дождитесь создания контейнеров
```
docker-compose up -d
```
проект станет доступ по ip-адресу сервера

### **Шаблон .env**
<a name='Шаблон .env'></a>

<font color='orange'>DB_ENGINE</font>=**django.db.backends.postgresql** <font color='green'># Указываем используемую СУБД</font>

<font color='orange'>DB_NAME</font>=**postgres** <font color='green'># Имя базы данных</font>

<font color='orange'>POSTGRES_USER</font>=**postgres** <font color='green'># Логин для подключения к БД</font>

<font color='orange'>POSTGRES_PASSWORD</font>=**postgres** <font color='green'># Пароль для подключения (обязательно измените на свой)</font>

<font color='orange'>DB_HOST</font>=**db** <font color='green'># Название контейнера</font>

<font color='orange'>DB_PORT</font>=**5432** <font color='green'> # Порт для подключения к БД</font>