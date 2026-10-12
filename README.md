# hotel-cancellations

## Данные

Датасет: [Hotel Booking Demand](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)
(Kaggle). Файлы данных в репозиторий не включены.

Чтобы скачать их, выполните из корня проекта:

```bash
    python3 src/download_data.py
```

Файл появится в `data/raw/hotel_bookings.csv`.

## Запуск проекта

```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python3 src/download_data.py
```
Затем откройте ноутбуки из папки `notebooks/` по порядку.