"""
Практическое занятие 10. Обработка изображений (продолжение).
Запуск: python practice_10.py

Подготовка открыток: python ../practice_09/prepare_test_images.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent
POSTCARDS_DIR = BASE / "postcards"
OUTPUT_DIR = BASE / "output"

HOLIDAYS = {
    "новый год": "new_year.jpg",
    "8 марта": "march8.jpg",
    "день рождения": "birthday.jpg",
}


def _font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    names = ("arialbd.ttf", "arial.ttf") if bold else ("arial.ttf", "segoeui.ttf")
    for name in names:
        path = Path("C:/Windows/Fonts") / name
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def _ensure_postcards() -> bool:
    if not POSTCARDS_DIR.exists() or not any(POSTCARDS_DIR.glob("*.jpg")):
        print("Нет открыток. Выполните:")
        print("  python ..\\practice_09\\prepare_test_images.py")
        return False
    return True


def run_10_1() -> None:
    print("\n--- Задание 10.1: обрезка открытки ---")
    if not _ensure_postcards():
        return

    path = POSTCARDS_DIR / "new_year.jpg"
    OUTPUT_DIR.mkdir(exist_ok=True)

    with Image.open(path) as img:
        w, h = img.size
        print(f"Исходный размер: {w} x {h}")
        print("Область обрезки: центральная часть (убираем края).")

        left = w // 6
        top = h // 6
        right = w - left
        bottom = h - top
        cropped = img.crop((left, top, right, bottom))

        out_path = OUTPUT_DIR / "cropped_new_year.jpg"
        cropped.save(out_path)
        print("Сохранено:", out_path)
        print("Новый размер:", cropped.size)
        cropped.show()


def run_10_2() -> None:
    print("\n--- Задание 10.2: открытка по празднику ---")
    if not _ensure_postcards():
        return

    print("Доступные праздники:")
    for name in HOLIDAYS:
        print(f"  — {name}")

    holiday = input("\nК какому празднику нужна открытка? ").strip().lower()
    filename = HOLIDAYS.get(holiday)
    if not filename:
        print("Такого праздника нет в словаре.")
        return

    path = POSTCARDS_DIR / filename
    if not path.exists():
        print("Файл не найден:", path)
        return

    with Image.open(path) as img:
        print("Открываю:", path.name)
        img.show()


def run_10_3() -> None:
    print("\n--- Задание 10.3: поздравление на открытке ---")
    if not _ensure_postcards():
        return

    print("Доступные праздники:")
    for name in HOLIDAYS:
        print(f"  — {name}")

    holiday = input("\nПраздник: ").strip().lower()
    filename = HOLIDAYS.get(holiday)
    if not filename:
        print("Такого праздника нет.")
        return

    name = input("Имя поздравляемого: ").strip()
    if not name:
        print("Имя не введено.")
        return

    text = f"{name}, поздравляю!"
    path = POSTCARDS_DIR / filename
    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / f"greeting_{Path(filename).stem}.png"

    with Image.open(path) as img:
        rgb = img.convert("RGB")
        draw = ImageDraw.Draw(rgb)

        title_font = _font(36, bold=True)
        name_font = _font(48, bold=True)

        draw.text((20, 20), "С праздником!", fill=(255, 215, 0), font=title_font)
        bbox = draw.textbbox((0, 0), text, font=name_font)
        tw = bbox[2] - bbox[0]
        x = (rgb.width - tw) // 2
        y = rgb.height - 80
        draw.text((x, y), text, fill=(255, 50, 50), font=name_font)

        rgb.save(out_path, format="PNG")
        print("Сохранено:", out_path)
        rgb.show()


TASKS = {
    "1": ("10.1 — обрезка", run_10_1),
    "2": ("10.2 — открытка по празднику", run_10_2),
    "3": ("10.3 — текст поздравления", run_10_3),
}


def run_all_in_order() -> None:
    print("\n=== Все задания 10 по порядку ===")
    for _, (_, func) in sorted(TASKS.items()):
        func()
        input("\nНажмите Enter для следующего задания...")


def main() -> None:
    while True:
        print("\n" + "=" * 40)
        print("Практическое занятие 10")
        print("=" * 40)
        for key, (title, _) in TASKS.items():
            print(f"  {key}. {title}")
        print("  4. Выполнить все задания по порядку")
        print("  0. Выход")

        choice = input("\nВыберите задание: ").strip()

        if choice == "0":
            print("До свидания!")
            break
        if choice == "4":
            run_all_in_order()
            continue
        if choice in TASKS:
            TASKS[choice][1]()
        else:
            print("Нет такого пункта. Введите 1–4 или 0.")


if __name__ == "__main__":
    main()
