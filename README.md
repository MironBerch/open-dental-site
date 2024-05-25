# dental-site

## Как запустить проект:

Создайте файл `.env`:

```dotenv
SECRET_KEY=secret

DJANGO_SUPERUSER_EMAIL=admin@gmail.ru
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=root

POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

YANDEX_METRIKA=<!-- Yandex.Metrika counter --> <script type="text/javascript" ></script> <noscript></noscript> <!-- /Yandex.Metrika counter -->

DOCKERHUB_USERNAME=
DOCKERHUB_TOKEN=

```

Запустите нужную команду:

for develop

```docker compose up --build```

for production

```docker compose -f docker-compose-prod.yml up --build```

for load test data

```docker exec -it dental sh -c ". ./init-data.sh"```

for use dump-data script

```docker exec -it dental sh -c ". ./dump-data.sh -d dent"```

for setup environment values

```. ./env_setup.sh```
