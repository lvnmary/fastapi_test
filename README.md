# Restaurant Booking API

REST API-сервис для бронирования столиков в ресторане. 
Реализовано на FastAPI + SQLAlchemy + PostgreSQL.

## Функциональность

- Управление столиками:
  - Получить список столов
  - Создать столик
  - Удалить столик

- Управление бронями:
  - Получить список броней
  - Создать бронь (с проверкой на пересечение)
  - Удалить бронь

## Технологии

- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Docker, docker-compose

## Запуск проекта

1. Клонировать репозиторий:

```
git clone 
cd restaurant_booking

```

2. Собрать и запустить:

```
docker-compose up --build

```

3. Документация доступна по адресу:

Swagger: http://localhost:8000/docs

Redoc: http://localhost:8000/redoc

