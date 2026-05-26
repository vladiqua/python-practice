import json
from pathlib import Path


def ensure_json_file(json_path: Path) -> None:
    if not json_path.exists():
        data = {
            "products": [
                {"name": "Шоколад", "price": 50, "available": True, "weight": 100},
                {"name": "Кофе", "price": 100, "available": False, "weight": 250},
                {"name": "Чай", "price": 70, "available": True, "weight": 50},
            ]
        }
        with json_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


def print_products(data: dict) -> None:
    for product in data.get("products", []):
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        if product.get("available"):
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()


def task_12_1(json_path: Path) -> None:
    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    print("12.1) Содержимое файла JSON:")
    print_products(data)


def task_12_2(json_path: Path) -> None:
    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    print("12.2) Добавление нового продукта:")
    name = input("Введите название: ")
    price = int(input("Введите цену: "))
    weight = int(input("Введите вес: "))
    available_input = input("В наличии? (да/нет): ").strip().lower()
    available = available_input in {"да", "д", "yes", "y", "true", "1"}

    new_product = {
        "name": name,
        "price": price,
        "available": available,
        "weight": weight,
    }

    data.setdefault("products", []).append(new_product)

    with json_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("\nОбновленное содержимое файла JSON:")
    print_products(data)


if __name__ == "__main__":

    file_path = Path("products.json")
    ensure_json_file(file_path)

    task_12_1(file_path)
    task_12_2(file_path)
{
  "products": [
    {
      "name": "Шоколад",
      "price": 50,
      "available": True,
      "weight": 100
    },
    {
      "name": "Кофе",
      "price": 100,
      "available": False,
      "weight": 250
    },
    {
      "name": "Чай",
      "price": 70,
      "available": True,
      "weight": 50
    },
    {
      "name": "???????",
      "price": 120,
      "available": False,
      "weight": 300
    }
  ]
}