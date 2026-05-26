# Практическое занятие 11: работа с файлами и CSV

from pathlib import Path
from PIL import Image, ImageOps
import csv


# -------------------- 11.1 --------------------
# Подготовить 5 графических файлов в папке и обработать их,
# итоговая папка создается через Pathlib.

def task_11_1():
    source_dir = Path("images_source")
    result_dir = Path("images_result")

    source_dir.mkdir(exist_ok=True)
    result_dir.mkdir(exist_ok=True)

    # Создаем 5 тестовых изображений (если их нет)
    colors = ["red", "green", "blue", "yellow", "purple"]
    for i, color in enumerate(colors, start=1):
        img_path = source_dir / f"img_{i}.png"
        if not img_path.exists():
            img = Image.new("RGB", (300, 200), color=color)
            img.save(img_path)

    # Обрабатываем: перевод в ч/б
    for file in source_dir.iterdir():
        if file.is_file():
            with Image.open(file) as img:
                processed = ImageOps.grayscale(img)
                out_path = result_dir / f"{file.stem}_gray{file.suffix}"
                processed.save(out_path)

    print("11.1 выполнено: изображения обработаны и сохранены в", result_dir)


# -------------------- 11.2 --------------------
# Обрабатывать только jpg/png, игнорируя остальные типы.

def task_11_2():
    source_dir = Path("mixed_files")
    result_dir = Path("filtered_result")

    source_dir.mkdir(exist_ok=True)
    result_dir.mkdir(exist_ok=True)

    allowed_ext = {".jpg", ".jpeg", ".png"}

    for file in source_dir.iterdir():
        if file.is_file() and file.suffix.lower() in allowed_ext:
            with Image.open(file) as img:
                # Пример операции: отзеркаливание
                processed = ImageOps.mirror(img)
                out_path = result_dir / f"{file.stem}_mirror{file.suffix}"
                processed.save(out_path)
        else:
            # Можно не печатать, но так видно, что фильтрация работает
            print("Пропущен файл:", file.name)

    print("11.2 выполнено: обработаны только jpg/png из", source_dir)


# -------------------- 11.3 --------------------
# Считать CSV, вывести список покупок и итоговую сумму.

def task_11_3():
    csv_file = Path("products.csv")

    # Если файла нет, создаем пример из задания
    if not csv_file.exists():
        with csv_file.open("w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Продукт", "Количество", "Цена"])
            writer.writerow(["Молоко", 2, 80])
            writer.writerow(["Сыр", 1, 500])
            writer.writerow(["Хлеб", 2, 70])

    total = 0
    rows = []

    with csv_file.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["Продукт"]
            qty = int(row["Количество"])
            price = int(row["Цена"])
            total += qty * price
            rows.append((name, qty, price))

    print("Нужно купить:")
    for name, qty, price in rows:
        print(f"{name} - {qty} шт. за {price} руб.")
    print(f"Итоговая сумма: {total} руб.")


if __name__ == "__main__":

    task_11_1()
    task_11_2()
    task_11_3()
