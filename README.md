# api_yamdb
![example workflow](https://github.com/Donatello-M/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
Сервис api_yamdb позволяет просматривать информацию
о различных художественных произведениях разных жанров.
Помимо просмотра, у вас будет возможность оставлять отзывы
на любое имеющееся произведение, поставить ему оценку, а
также комментировать любой интересующий вас отзыв.
## Над проектом работали:
- Кирилл Звонков
- Владислав Яковицкий 
- Данила Макаричев

## Ссылка на проект
```
http://51.250.31.105/
```
## Как запустить проект:

Клонировать репозиторий:

```
git clone https://github.com/Donatello-M/infra_sp2
```

```
cd infra_sp2
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить docker на свою операционную систему

Перейти в папку /infra и создать файл .env

```
cd infra

touch .env

vim .env
```

Заполнить файл по шаблону:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=yatube
POSTGRES_USER=yatube_user
POSTGRES_PASSWORD=xxxyyyzzz
DB_HOST=db
DB_PORT=5432
DEBUG=False
ALLOWED_HOSTS=192.112.66.32, 62.84.123.99
SECRET_KEY=pum-purum-pum-pum
```

Развернуть проект:

```
cd infra/

sudo docker-compose up -d
```

Произвести миграции, создать суперпользователя и собрать статику:

```
sudo docker-compose exec web python manage.py migrate
sudo docker-compose exec web python manage.py createsuperuser
sudo docker-compose exec web python manage.py collectstatic --no-input
```

Заполнить базу из дампа:

```
python3 manage.py shell  
>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> quit()

python manage.py loaddata dump.json
```

## Как выполнять запросы:
Полная документация по запросам
```
http://localhost/redoc/
```
## Установить docker:
```
sudo apt install curl
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh   
sudo apt remove docker docker-engine docker.io containerd runc
sudo apt update 
sudo apt install \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg-agent \
  software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt install docker-ce docker-compose -y
```
## Используемые технологии:
Gunicorn
Nginx
Docker
Django
PostgreSQL
