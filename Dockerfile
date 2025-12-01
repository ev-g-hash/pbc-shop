# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Копируем зависимости
COPY requirements.txt* ./
RUN pip install --no-cache-dir -r requirements.txt || echo "No requirements.txt found"

# Копируем весь проект
COPY . .

# Создаем необходимые директории
RUN mkdir -p /app/media /app/staticfiles

# Собираем статические файлы
RUN python manage.py collectstatic --noinput

# Открываем порт
EXPOSE 8000

# Команда для запуска
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "--timeout", "30", "shop.wsgi:application"]