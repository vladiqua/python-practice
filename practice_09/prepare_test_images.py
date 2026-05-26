"""Создаёт тестовые изображения для занятий 9 и 10."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent
IMAGES = BASE / "images"
POSTCARDS = BASE.parent / "practice_10" / "postcards"


def _font(size: int) -> ImageFont.ImageFont:
    for name in ("arial.ttf", "segoeui.ttf"):
        path = Path("C:/Windows/Fonts") / name
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def create_color_image(path: Path, size: tuple[int, int], color: tuple[int, int, int], text: str) -> None:
    if path.exists():
        print("Уже есть (не перезаписываю):", path.name)
        return
    img = Image.new("RGB", size, color)
    draw = ImageDraw.Draw(img)
    font = _font(28)
    draw.text((20, 20), text, fill=(255, 255, 255), font=font)
    img.save(path)
    print("Создано:", path.name)


def main() -> None:
    IMAGES.mkdir(exist_ok=True)
    POSTCARDS.mkdir(parents=True, exist_ok=True)

    create_color_image(IMAGES / "sample.jpg", (600, 400), (70, 130, 180), "Sample 9.1")

    colors = [
        ((200, 50, 50), "1"),
        ((50, 200, 50), "2"),
        ((50, 50, 200), "3"),
        ((200, 200, 50), "4"),
        ((200, 50, 200), "5"),
    ]
    for i, (color, label) in enumerate(colors, start=1):
        create_color_image(IMAGES / f"{i}.jpg", (300, 200), color, label)

    create_color_image(POSTCARDS / "new_year.jpg", (500, 350), (20, 60, 120), "Новый год")
    create_color_image(POSTCARDS / "march8.jpg", (500, 350), (180, 60, 120), "8 марта")
    create_color_image(POSTCARDS / "birthday.jpg", (500, 350), (120, 80, 200), "День рождения")

    print("Готово:")
    print(" ", IMAGES)
    print(" ", POSTCARDS)


if __name__ == "__main__":
    main()
