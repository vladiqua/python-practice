"""
Практическое занятие 7. Списки и кортежи.
Запуск: python practice_07.py
"""

from collections import Counter


def run_7_1() -> None:
    print("\n--- Задание 7.1: число в списке ---")
    numbers = [12, 5, 27, 5, 42]
    try:
        user_number = int(input("Введите число: "))
    except ValueError:
        print("Ошибка: введите целое число.")
        return

    print("Исходный список:", numbers)
    print("Число пользователя:", user_number)
    if user_number in numbers:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")


def run_7_2() -> None:
    print("\n--- Задание 7.2: повторяющиеся элементы ---")
    data = [1, 2, 3, 2, 4, 5, 3, 6, 2, 7]
    print("Исходный список:", data)

    counts = Counter(data)
    duplicates = [value for value, count in counts.items() if count > 1]

    if duplicates:
        print("Повторяющиеся элементы:")
        for value in duplicates:
            print(value)
    else:
        print("Повторяющихся элементов нет.")


def run_7_3() -> None:
    print("\n--- Задание 7.3: выходные и рабочие дни ---")
    week_days = (
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Воскресенье",
    )

    try:
        days_off_count = int(input("Сколько выходных на неделе вы хотите? (0-7): "))
    except ValueError:
        print("Ошибка: введите целое число.")
        return

    if not 0 <= days_off_count <= 7:
        print("Ошибка: введите число от 0 до 7.")
        return

    weekends = list(week_days[-days_off_count:]) if days_off_count else []
    workdays = list(week_days[:-days_off_count]) if days_off_count else list(week_days)

    print("Ваши выходные дни:", ", ".join(weekends) if weekends else "нет")
    print("Ваши рабочие дни:", ", ".join(workdays) if workdays else "нет")


def run_7_4() -> None:
    print("\n--- Задание 7.4: спортивная команда ---")

    group_a = [
        "Щербакова",
        "Ерастов",
        "Мишкова",
        "Кононенко",
        "Пилясов",
        "Базылев",
        "Ислам",
        "Мо",
        "Ма",
        "Лю",
    ]
    group_b = [
        "Лю",
        "Волкова",
        "Белова",
        "Смирнов",
        "Шаронов",
        "Ши",
        "Шэ",
        "Тэн",
        "Цзинь",
    ]

    team = tuple(group_a[:5] + group_b[:5])

    print("Группа 1:", group_a)
    print("Группа 2:", group_b)
    print("Спортивная команда (кортеж):", team)
    print("Длина кортежа:", len(team))

    sorted_team = tuple(sorted(team))
    print("Кортеж, отсортированный по алфавиту:", sorted_team)

    surname = "Иванов"
    in_team = surname in team
    count = team.count(surname)
    print(f'Студент "{surname}" в команде: {"да" if in_team else "нет"}')
    print(f'Фамилия "{surname}" встречается в кортеже: {count} раз(а)')


TASKS = {
    "1": ("7.1 — число в списке", run_7_1),
    "2": ("7.2 — повторы в списке", run_7_2),
    "3": ("7.3 — выходные дни", run_7_3),
    "4": ("7.4 — спортивная команда", run_7_4),
}


def run_all_in_order() -> None:
    print("\n=== Все задания 7 по порядку ===")
    for _, (_, func) in sorted(TASKS.items()):
        func()
        input("\nНажмите Enter для следующего задания...")


def main() -> None:
    while True:
        print("\n" + "=" * 40)
        print("Практическое занятие 7")
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
