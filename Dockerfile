# Базовый образ
FROM python:3.9

# Обновление pip и установка зависимостей
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копируем весь проект в контейнер
COPY . /src
WORKDIR /src

# Открываем порты для Jupyter и MLflow
EXPOSE 8888
EXPOSE 5000

# Переменная окружения для Python
ENV PYTHONUNBUFFERED=1

# Позволяем запускать несколько команд (например, Jupyter, MLflow)
ENTRYPOINT ["bash", "-c"]
CMD ["jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root"]
