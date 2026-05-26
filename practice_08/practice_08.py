"""
Практическое занятие 8. Словари. Множества.
Запуск: python practice_08.py
"""


def run_8_1() -> None:
    print("\n--- Задание 8.1: страны и столицы ---")
    countries = {
        "Россия": "Москва",
        "Франция": "Париж",
        "Германия": "Берлин",
        "Италия": "Рим",
        "Испания": "Мадрид",
    }

    print("\na) Все пары ключ-значение:")
    for country, capital in countries.items():
        print(f"  {country} — {capital}")

    country = input("\nВведите название страны: ").strip()
    capital = countries.get(country)
    print("\nb) Столица:")
    if capital:
        print(f"  {country} — {capital}")
    else:
        print(f"  Страна «{country}» не найдена в словаре.")

    print("\nc) Словарь в алфавитном порядке стран:")
    for country in sorted(countries):
        print(f"  {country} — {countries[country]}")


def run_8_2() -> None:
    print("\n--- Задание 8.2: стоимость слова (Эрудит) ---")
    scores = {
        **dict.fromkeys("АВЕИНОРСТ", 1),
        **dict.fromkeys("ДКЛМПУ", 2),
        **dict.fromkeys("БГЁЬЯ", 3),
        **dict.fromkeys("ЙЫ", 4),
        **dict.fromkeys("ЖЗХЦЧ", 5),
        **dict.fromkeys("ШЭЮ", 8),
        **dict.fromkeys("ФЩЪ", 10),
    }

    word = input("Введите слово: ").strip().upper()
    if not word:
        print("Слово не введено.")
        return

    total = 0
    unknown = []
    for letter in word:
        if letter in scores:
            total += scores[letter]
        elif letter.isalpha():
            unknown.append(letter)

    print(f"Слово: {word}")
    print(f"Стоимость: {total} очков")
    if unknown:
        print("Буквы без оценки:", ", ".join(sorted(set(unknown))))


def run_8_3() -> None:
    print("\n--- Задание 8.3*: языки студентов ---")
    students = {
        "Иванов": {"русский", "английский"},
        "Петров": {"русский", "немецкий", "китайский"},
        "Сидорова": {"русский", "французский", "китайский"},
        "Козлов": {"английский", "испанский"},
        "Новикова": {"русский", "китайский", "японский"},
    }

    all_languages = set()
    for langs in students.values():
        all_languages |= langs

    print("Различных языков:", len(all_languages))
    print("Отсортированный список языков:")
    for lang in sorted(all_languages):
        print(f"  — {lang}")

    print('\nСтуденты, которые знают китайский:')
    for name, langs in students.items():
        if "китайский" in langs:
            print(f"  — {name}")


TASKS = {
    "1": ("8.1 — страны и столицы", run_8_1),
    "2": ("8.2 — Эрудит", run_8_2),
    "3": ("8.3* — множества языков", run_8_3),
}


def run_all_in_order() -> None:
    print("\n=== Все задания 8 по порядку ===")
    for _, (_, func) in sorted(TASKS.items()):
        func()
        input("\nНажмите Enter для следующего задания...")


def main() -> None:
    while True:
        print("\n" + "=" * 40)
        print("Практическое занятие 8")
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
