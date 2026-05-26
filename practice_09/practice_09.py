"""
Практическое занятие 9. Обработка изображений.
Запуск: python practice_09.py

Перед первым запуском: pip install Pillow
Подготовка файлов: python prepare_test_images.py
"""

import os
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

BASE = Path(__file__).resolve().parent
IMAGES_DIR = BASE / "images"
OUTPUT_DIR = BASE / "output"
IMAGE_EXT = (".jpg", ".jpeg", ".png", ".bmp", ".webp")


def _find_image(stem: str) -> Path | None:
    """Ищет файл sample, 1, 2… (имя без учёта регистра)."""
    if not IMAGES_DIR.exists():
        return None

    stem_lower = stem.lower()
    for path in sorted(IMAGES_DIR.iterdir()):
        if path.is_file() and path.suffix.lower() in IMAGE_EXT:
            if path.stem.lower() == stem_lower:
                return path

    for ext in IMAGE_EXT:
        path = IMAGES_DIR / f"{stem}{ext}"
        if path.exists():
            return path
    return None


def _show_image(img: Image.Image, path: Path) -> None:
    """Показать изображение на экране (Windows / другие ОС)."""
    print("Открываю изображение в программе просмотра...")

    # На Windows надёжнее открыть файл напрямую (Фото / просмотрщик)
    try:
        if sys.platform == "win32":
            os.startfile(path)  # type: ignore[attr-defined]
            print("Окно с фото должно открыться. Файл:", path)
            return
        if sys.platform == "darwin":
            os.system(f'open "{path}"')
            print("Открыто:", path)
            return
        os.system(f'xdg-open "{path}"')
        print("Открыто:", path)
        return
    except Exception as e:
        print("Не удалось открыть через систему:", e)

    OUTPUT_DIR.mkdir(exist_ok=True)
    preview = OUTPUT_DIR / f"_preview_{path.stem}.png"
    img.convert("RGB").save(preview)

    try:
        if sys.platform == "win32":
            os.startfile(preview)  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            os.system(f'open "{preview}"')
        else:
            os.system(f'xdg-open "{preview}"')
        print("Открыта копия:", preview)
    except Exception as e:
        print("Откройте файл вручную в проводнике:", path)
        print("Причина:", e)


def _numbered_images() -> list[Path]:
    files = []
    for n in range(1, 6):
        path = _find_image(str(n))
        if path:
            files.append(path)
    return files


def _all_images() -> list[Path]:
    if not IMAGES_DIR.exists():
        return []
    result = []
    for path in sorted(IMAGES_DIR.iterdir()):
        if path.is_file() and path.suffix.lower() in IMAGE_EXT:
            result.append(path)
    return result


def _save_image(img: Image.Image, path: Path) -> None:
    """Сохранить JPG/PNG (любой режим Pillow → RGB)."""
    out = img.convert("RGB") if img.mode not in ("RGB", "L") else img
    if path.suffix.lower() in (".jpg", ".jpeg"):
        out.save(path, quality=95)
    else:
        out.save(path)


def _open_folder(folder: Path) -> None:
    """Открыть папку с результатами в проводнике."""
    folder.mkdir(parents=True, exist_ok=True)
    print("\n>>> Результаты в папке:")
    print(folder)
    try:
        if sys.platform == "win32":
            os.startfile(folder)  # type: ignore[attr-defined]
        elif sys.platform == "darwin":
            os.system(f'open "{folder}"')
        else:
            os.system(f'xdg-open "{folder}"')
    except Exception:
        print("(Откройте эту папку вручную в проводнике)")


def check_images() -> None:
    print("\n--- Проверка ваших изображений ---")
    print("Папка:", IMAGES_DIR)
    if not IMAGES_DIR.exists():
        print("Папка images не найдена. Создайте её и положите туда файлы.")
        return

    sample = _find_image("sample")
    print("sample (9.1, 9.2):", sample.name if sample else "НЕТ")

    for n in range(1, 6):
        path = _find_image(str(n))
        print(f"  {n} (9.3):", path.name if path else "НЕТ")

    all_files = _all_images()
    print(f"\nВсего файлов в images: {len(all_files)}")
    for path in all_files:
        try:
            with Image.open(path) as img:
                print(f"  — {path.name}: {img.size[0]}x{img.size[1]}, {img.format}")
        except Exception as e:
            print(f"  — {path.name}: ошибка открытия ({e})")


def _ensure_images() -> bool:
    if _find_image("sample"):
        return True
    print("Нет файла sample (sample.jpg или sample.png) в папке images.")
    print("Папка:", IMAGES_DIR)
    return False


def _font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    names = ("arialbd.ttf", "arial.ttf") if bold else ("arial.ttf", "segoeui.ttf")
    for name in names:
        path = Path("C:/Windows/Fonts") / name
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def run_9_1() -> None:
    print("\n--- Задание 9.1: открыть и показать изображение ---")
    if not _ensure_images():
        return

    path = _find_image("sample")
    print("Файл:", path)

    try:
        with Image.open(path) as img:
            print("Размер (ширина x высота):", img.size)
            print("Формат:", img.format)
            print("Цветовая модель:", img.mode)
            copy = img.copy()
    except Exception as e:
        print("Ошибка чтения файла:", e)
        print("Проверьте, что это обычный JPG/PNG (не повреждён).")
        return

    _show_image(copy, path)
    print("Готово. Закройте окно с фото и вернитесь в терминал.")


def run_9_2() -> None:
    print("\n--- Задание 9.2: уменьшение и зеркало ---")
    if not _ensure_images():
        return

    OUTPUT_DIR.mkdir(exist_ok=True)
    path = _find_image("sample")
    print("Исходный файл:", path)

    try:
        with Image.open(path) as img:
            img = img.convert("RGB")
            w, h = img.size
            nw, nh = max(1, w // 3), max(1, h // 3)

            small = img.resize((nw, nh))
            p1 = OUTPUT_DIR / "small_x3.jpg"
            _save_image(small, p1)

            mirror_h = ImageOps.mirror(img)
            p2 = OUTPUT_DIR / "mirror_horizontal.jpg"
            _save_image(mirror_h, p2)

            mirror_v = ImageOps.flip(img)
            p3 = OUTPUT_DIR / "mirror_vertical.jpg"
            _save_image(mirror_v, p3)

        print("\nГотово! Созданы файлы:")
        print(" ", p1.name, f"({nw}x{nh})")
        print(" ", p2.name)
        print(" ", p3.name)
        _open_folder(OUTPUT_DIR)
    except Exception as e:
        print("Ошибка:", e)


def _images_for_filter() -> list[Path]:
    """Файлы 1…5 или любые 5 картинок из images (кроме sample)."""
    numbered = _numbered_images()
    if len(numbered) >= 5:
        return numbered[:5]

    others = [p for p in _all_images() if p.stem.lower() != "sample"]
    if len(others) >= 5:
        print("(Файлов 1.jpg…5.jpg нет — беру любые 5 фото из папки images)")
        return others[:5]

    return numbered


def run_9_3() -> None:
    print("\n--- Задание 9.3: фильтр для 1.jpg … 5.jpg ---")
    files = _images_for_filter()
    if len(files) < 5:
        print("Нужно минимум 5 фото в папке images (1.jpg … 5.jpg или любые 5 файлов).")
        check_images()
        return

    out_dir = OUTPUT_DIR / "filtered"
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        for path in files:
            with Image.open(path) as img:
                result = img.convert("RGB").filter(ImageFilter.CONTOUR)
                out_path = out_dir / f"filtered_{path.stem}.jpg"
                _save_image(result, out_path)
                print("Сохранено:", out_path.name)

        print(f"\nГотово! Обработано файлов: {len(files)}")
        _open_folder(out_dir)
    except Exception as e:
        print("Ошибка:", e)


def run_9_4() -> None:
    print("\n--- Задание 9.4: водяной знак ---")
    files = _all_images()
    if not files:
        print("Нет изображений в папке images.")
        return

    out_dir = OUTPUT_DIR / "watermarked"
    out_dir.mkdir(parents=True, exist_ok=True)
    mark = input("Текст водяного знака (Enter = PYTHON): ").strip() or "PYTHON"

    try:
        for path in files:
            with Image.open(path) as img:
                rgb = img.convert("RGBA")
                overlay = Image.new("RGBA", rgb.size, (255, 255, 255, 0))
                draw = ImageDraw.Draw(overlay)
                font = _font(max(20, min(rgb.size) // 12))
                bbox = draw.textbbox((0, 0), mark, font=font)
                tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
                x = (rgb.width - tw) // 2
                y = (rgb.height - th) // 2
                draw.text((x, y), mark, fill=(255, 255, 255, 160), font=font)
                result = Image.alpha_composite(rgb, overlay)
                out_path = out_dir / f"wm_{path.stem}.jpg"
                _save_image(result, out_path)
                print("Сохранено:", out_path.name)

        print(f"\nГотово! Обработано файлов: {len(files)}")
        _open_folder(out_dir)
    except Exception as e:
        print("Ошибка:", e)


TASKS = {
    "1": ("9.1 — открыть изображение", run_9_1),
    "2": ("9.2 — уменьшение и зеркало", run_9_2),
    "3": ("9.3 — фильтр 1–5.jpg", run_9_3),
    "4": ("9.4 — водяной знак", run_9_4),
}


def run_prepare_images() -> None:
    from prepare_test_images import main as prepare_main

    prepare_main()


def run_all_in_order() -> None:
    print("\n=== Все задания 9 по порядку ===")
    for key in ("1", "2", "3", "4"):
        TASKS[key][1]()
        input("\nНажмите Enter для следующего задания...")


def main() -> None:
    while True:
        print("\n" + "=" * 40)
        print("Практическое занятие 9")
        print("=" * 40)
        for key, (title, _) in TASKS.items():
            print(f"  {key}. {title}")
        print("  5. Выполнить все задания по порядку")
        print("  6. Проверить, какие файлы видит программа")
        print("  8. Создать тестовые картинки (НЕ жмите, если уже положили свои!)")
        print("  0. Выход")

        choice = input("\nВыберите задание: ").strip()

        if choice == "0":
            print("До свидания!")
            break
        if choice == "6":
            check_images()
            continue
        if choice == "8":
            run_prepare_images()
            continue
        if choice == "5":
            run_all_in_order()
            continue
        if choice in TASKS:
            TASKS[choice][1]()
        else:
            print("Нет такого пункта.")


if __name__ == "__main__":
    main()
