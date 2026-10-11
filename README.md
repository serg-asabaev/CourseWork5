# Habit Tracker - Курсовая работа

## Описание
Приложение для трекинга привычек.

## Развертывание на сервере

### Быстрый старт с Docker Compose
1. Склонируйте репозиторий на сервер
2. Создайте .env файл по образцу из инструкции
3. Запустите: docker compose up -d --build
4. Примените миграции: docker compose exec -T web python manage.py migrate --noinput
5. Соберите статику: docker compose exec -T web python manage.py collectstatic --noinput

Подробная инструкция по развертыванию находится в файле [deploy_instructions.md](deploy_instructions.md).

## CI/CD
Проект настроен на автоматический деплой через GitHub Actions при пуше в ветки main и eature/coursework_6.