"""
Все практические занятия в одном меню.
Запуск: python main.py

Сначала 7 → 8 → 9 → 10 или выбор любого занятия отдельно.
"""

import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent

PRACTICES = {
    "6": ("Занятие 6 — функции", BASE / "practice_06" / "practice_06.py"),
    "7": ("Занятие 7 — списки и кортежи", BASE / "practice_07" / "practice_07.py"),
    "8": ("Занятие 8 — словари и множества", BASE / "practice_08" / "practice_08.py"),
    "9": ("Занятие 9 — изображения", BASE / "practice_09" / "practice_09.py"),
    "10": ("Занятие 10 — изображения (продолжение)", BASE / "practice_10" / "practice_10.py"),
}

ORDER_7_8_9 = ("7", "8", "9")
ORDER_ALL = ("6", "7", "8", "9", "10")


def run_practice(key: str) -> None:
    title, script = PRACTICES[key]
    if not script.exists():
        print(f"Файл не найден: {script}")
        return

    print("\n" + "=" * 50)
    print(f"Запуск: {title}")
    print("=" * 50)
    print("(После выхода из занятия — 0 — вернётесь в это меню)\n")

    subprocess.run([sys.executable, str(script)], cwd=script.parent)


def run_sequence(keys: tuple[str, ...]) -> None:
    for key in keys:
        run_practice(key)
        if key != keys[-1]:
            cont = input("\nПерейти к следующему занятию? (д/н): ").strip().lower()
            if cont not in ("д", "да", "y", "yes"):
                print("Остановлено.")
                return


def main() -> None:
    while True:
        print("\n" + "=" * 50)
        print("  ПРАКТИЧЕСКИЕ ЗАНЯТИЯ — ГЛАВНОЕ МЕНЮ")
        print("=" * 50)
        for key, (title, _) in PRACTICES.items():
            print(f"  {key}. {title}")
        print()
        print("  79. Занятия 7 → 8 → 9 по порядку")
        print("  99. Все занятия 6 → 7 → 8 → 9 → 10")
        print("  0. Выход")

        choice = input("\nВыберите занятие: ").strip()

        if choice == "0":
            print("До свидания!")
            break
        if choice == "79":
            run_sequence(ORDER_7_8_9)
            continue
        if choice == "99":
            run_sequence(ORDER_ALL)
            continue
        if choice in PRACTICES:
            run_practice(choice)
        else:
            print("Нет такого пункта. Введите 6–10, 79, 99 или 0.")


if __name__ == "__main__":
    main()
