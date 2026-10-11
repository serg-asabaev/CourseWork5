FROM python:3.14-slim

# Устанавливаем системные зависимости (нужны для Poetry и postgresql client).
# build-essential нужен для сборки psycopg2 из исходников (Linux-колёс нет):
# он тянет gcc и libc6-dev с заголовками <assert.h> и др. libpq-dev — заголовки PostgreSQL.
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry
RUN pip install --no-cache-dir poetry

# Добавляем Poetry в PATH
ENV PATH="/root/.local/bin:$PATH"

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости (без dev-пакетов для production)
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Копируем остальной код
COPY . .

# Команда по умолчанию (будет переопределена в compose)
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]