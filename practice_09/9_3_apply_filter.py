"""9.3 — Фильтр ко всем изображениям 1.jpg … 5.jpg (без размытия)."""

from pathlib import Path

from PIL import Image, ImageFilter

IMAGES_DIR = Path(__file__).resolve().parent / "images"
OUTPUT_DIR = Path(__file__).resolve().parent / "filtered"


def apply_filter(img: Image.Image) -> Image.Image:
    """Контурный фильтр (не размытие)."""
    return img.filter(ImageFilter.CONTOUR)


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    files = sorted(IMAGES_DIR.glob("*.jpg"))
    if not files:
        print("Нет файлов в", IMAGES_DIR)
        print("Сначала выполните: python prepare_test_images.py")
        return

    for path in files:
        with Image.open(path) as img:
            result = apply_filter(img)
            out_path = OUTPUT_DIR / f"filtered_{path.name}"
            result.save(out_path)
            print("Сохранено:", out_path)


if __name__ == "__main__":
    main()
