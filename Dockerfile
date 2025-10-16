# Задаем базовый образ (версия не менее версии Python в проекте)
FROM python:3.13-slim

# Задаем рабочую директорию, в которой будет располагаться код
WORKDIR /app

# Устанавливаем poetry
RUN pip install poetry==2.2.1

# копируем файлы с зависимостями в рабочую директорию
COPY pyproject.toml poetry.lock ./

# Инициализируем poetry без создания виртуального окружения для установки основных зависимостей
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --only main

# Копируем остальной код проекта
COPY . .