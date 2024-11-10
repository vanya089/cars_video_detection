FROM python:3.9

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /src
WORKDIR /src

EXPOSE 8888
EXPOSE 5000

ENV PYTHONUNBUFFERED=1

# Позволяем запускать несколько команд (например, Jupyter, MLflow)
ENTRYPOINT ["bash", "-c"]
CMD ["jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root"]
