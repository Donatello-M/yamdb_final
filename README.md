# api_yamdb
Сервис api_yamdb позволяет просматривать информацию
о различных художественных произведениях разных жанров.
Помимо просмотра, у вас будет возможность оставлять отзывы
на любое имеющееся произведение, поставить ему оценку, а
также комментировать любой интересующий вас отзыв.
## Над проектом работали:
- Кирилл Звонков
- Владислав Яковицкий 
- Данила Макаричев
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
![example workflow](https://github.com/Donatello-M/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
