# Инструкция по развертыванию проекта на сервере (Ubuntu)

## 1. Требования к серверу
- Ubuntu 20.04+ 
- Установлены Docker и Docker Compose v2
- Пользователь \ubuntu\ с правами sudo
- Открыты порты: 80 (HTTP), 443 (HTTPS) - если используется Nginx, 8080 (для веб-приложения)

## 2. Подготовка SSH-ключей для деплоя через GitHub Actions
1. Создайте SSH-ключ для деплоя (или используйте существующий)
2. Приватный ключ добавьте в GitHub Secrets: \Settings > Secrets and variables > Actions > New repository secret\, имя \SERVER_SSH_KEY\, значение - содержимое приватного ключа
3. Публичный ключ добавьте на сервер в \~/.ssh/authorized_keys\ пользователя \ubuntu\

## 3. Настройка GitHub Secrets
| Секрет | Описание |
|---|---|
| \SERVER_SSH_KEY\ | Приватный SSH-ключ для подключения к серверу |
| \DJANGO_SECRET_KEY\ | Секретный ключ Django |
| \POSTGRES_DB\ | Имя БД PostgreSQL |
| \POSTGRES_USER\ | Пользователь PostgreSQL |
| \POSTGRES_PASSWORD\ | Пароль PostgreSQL |
| \TELEGRAM_BOT_TOKEN\ | Токен Telegram-бота |

## 4. Ручное развертывание
`ash
cd /home/ubuntu/app
docker compose up -d --build
docker compose exec -T web python manage.py migrate --noinput
docker compose exec -T web python manage.py collectstatic --noinput
`

## 5. Проверка работы
`ash
docker compose ps
curl http://localhost:8080/
`

## 6. Автоматический деплой через GitHub Actions
При пуше в \main\ или \eature/coursework_6\ запускается CI/CD с этапами lint, test, build-docker, deploy.
