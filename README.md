# Car Detection Project

Проект по детекции автомобилей с использованием YOLOv5 и MLflow для отслеживания экспериментов. Проект организован для работы в Docker.

## Структура проекта
- `data/`: хранит данные и модели.
- `notebooks/car_detection.ipynb`: основной код в Jupyter Notebook.
- `src/`: папка с исходным кодом.
- `Dockerfile`: настройки Docker.
- `requirements.txt`: зависимости проекта.

## Запуск проекта
1. Соберите Docker-образ:
   ```bash
   docker build -t car_detection_project .
