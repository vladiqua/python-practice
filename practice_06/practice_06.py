"""
Практическое занятие 6. Функции в Python.
Запуск: python practice_06.py
Выберите номер задания в меню или 0 — выход.
"""


# --- 6.1: делится ли число на 3 ---

def is_divisible_by_3(number: int) -> bool:
    return number % 3 == 0


def run_6_1() -> None:
    print("\n--- Задание 6.1: деление на 3 ---")
    try:
        n = int(input("Введите число: "))
    except ValueError:
        print("Ошибка: введите целое число.")
        return

    if is_divisible_by_3(n):
        print(f"{n} делится на 3.")
    else:
        print(f"{n} не делится на 3.")


# --- 6.2: деление 100 на введённое число ---

def divide_100(divisor: float) -> float:
    return 100 / divisor


def run_6_2() -> None:
    print("\n--- Задание 6.2: 100 / число ---")
    raw = input("Введите число: ")
    try:
        divisor = float(raw.replace(",", "."))
    except ValueError:
        print("Ошибка: введите число, а не текст.")
        return

    try:
        result = divide_100(divisor)
    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно.")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
    else:
        print(f"100 / {divisor} = {result}")


# --- 6.3: магическая дата ---

def is_magic_date(date_str: str) -> bool:
    parts = date_str.strip().split(".")
    if len(parts) != 3:
        return False
    try:
        day = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])
    except ValueError:
        return False
    return day * month == year % 100


def run_6_3() -> None:
    print("\n--- Задание 6.3: магическая дата ---")
    date_str = input("Введите дату (ДД.ММ.ГГГГ): ")
    if is_magic_date(date_str):
        print("Дата магическая.")
    else:
        print("Дата не магическая.")


# --- 6.4: счастливый билет ---

def is_lucky_ticket(number: str) -> bool:
    if not number.isdigit() or len(number) % 2 != 0:
        return False
    mid = len(number) // 2
    first = sum(int(d) for d in number[:mid])
    second = sum(int(d) for d in number[mid:])
    return first == second


def run_6_4() -> None:
    print("\n--- Задание 6.4: счастливый билет ---")
    ticket = input("Введите номер билета: ").strip()
    if is_lucky_ticket(ticket):
        print("Билет счастливый.")
    else:
        print("Билет не счастливый.")


TASKS = {
    "1": ("6.1 — деление на 3", run_6_1),
    "2": ("6.2 — 100 / число", run_6_2),
    "3": ("6.3 — магическая дата", run_6_3),
    "4": ("6.4 — счастливый билет", run_6_4),
}


def run_all_in_order() -> None:
    print("\n=== Все задания по порядку ===")
    for _, (_, func) in sorted(TASKS.items()):
        func()
        input("\nНажмите Enter для следующего задания...")


def main() -> None:
    while True:
        print("\n" + "=" * 40)
        print("Практическое занятие 6")
        print("=" * 40)
        for key, (title, _) in TASKS.items():
            print(f"  {key}. {title}")
        print("  5. Выполнить все задания по порядку")
        print("  0. Выход")

        choice = input("\nВыберите задание: ").strip()

        if choice == "0":
            print("До свидания!")
            break
        if choice == "5":
            run_all_in_order()
            continue
        if choice in TASKS:
            TASKS[choice][1]()
        else:
            print("Нет такого пункта. Введите 1–5 или 0.")


if __name__ == "__main__":
    main()
