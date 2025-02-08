# Installation & Setup Guide

Follow these steps to set up the project:

## 1️⃣ Clone the Repository

## 2️⃣ Rename .env.sample to .env

```bash
mv .env.sample .env
```

## 3️⃣ Build and Start Docker Containers

```bash
docker-compose up --build
```

## 4️⃣ Apply Migrations & Create Superuser

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

## 5️⃣ Open API Docs in Browser

[http://localhost:8001/api/docs/](http://localhost:8001/api/docs/)

### Docker Configuration Overview

The project uses **Docker Compose** to manage services:

- **Web Server** (`gunicorn` running Django Ninja)
- **PostgreSQL Database** (`db` service mapped to port **9000**)
- **Redis Cache** (`redis` service mapped to port **9001**)
- **Celery Worker** for background tasks

The services are configured in `docker-compose.yml`:

```yaml
version: '3.8'

services:
  web:
    build: .
    container_name: django_ninja_api
    command: >
      sh -c "python manage.py collectstatic --noinput &&
                   python manage.py migrate &&
                   gunicorn --bind 0.0.0.0:8000 djangoNinja.wsgi:application"
    volumes:
      - .:/app
    ports:
      - "8001:8000"
    depends_on:
      - db
      - redis
      - celery
    env_file:
      - .env

  db:
    image: postgres
    container_name: postgres_db_ninja
    restart: always
    environment:
      POSTGRES_DB: ninja_db
      POSTGRES_USER: ninja_user
      POSTGRES_PASSWORD: ninja_password
    ports:
      - "9000:5432"

  redis:
    image: redis
    container_name: redis_cache
    restart: always
    ports:
      - "9001:6379"

  celery:
    build: .
    container_name: celery_worker
    command: [ "celery", "-A", "djangoNinja", "worker", "--loglevel=info" ]
    depends_on:
      - redis
      - db
    environment:
      - DJANGO_SETTINGS_MODULE=djangoNinja.settings
      - CELERY_BROKER_URL=redis://redis:6379/0
```

For more details, refer to **[API Documentation](api.md)**.
