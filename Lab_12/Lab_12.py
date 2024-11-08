
import json

# Створення об'єкта JSON 
cars_data = [
    {"model": "Car A", "price": 10000, "age": 8},
    {"model": "Car B", "price": 15000, "age": 5},
    {"model": "Car C", "price": 20000, "age": 7},
    {"model": "Car D", "price": 12000, "age": 10},
    {"model": "Car E", "price": 17000, "age": 3},
    {"model": "Car F", "price": 25000, "age": 12},
    {"model": "Car G", "price": 30000, "age": 6},
    {"model": "Car H", "price": 18000, "age": 9},
    {"model": "Car I", "price": 22000, "age": 15},
    {"model": "Car J", "price": 13000, "age": 2}
]

# Збереження даних у файл JSON
with open('cars_data.json', 'w') as file:
    json.dump(cars_data, file, indent=4)


# Виведення вмісту JSON-файлу
def display_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        print("\nВміст JSON-файлу:")
        for entry in data:
            print(entry)


# Обчислення середньої вартості автомобілів, вік яких перевищує 6 років
def calculate_average_price(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        older_cars = [car['price'] for car in data if car['age'] > 6]

        if older_cars:
            average_price = sum(older_cars) / len(older_cars)
            print(f"\nСередня вартість автомобілів, вік яких перевищує 6 років: {average_price:.2f}")
        else:
            print("\nНемає автомобілів, вік яких перевищує 6 років.")


# Додавання нового запису
def add_car(filename, model, price, age):
    with open(filename, 'r') as file:
        data = json.load(file)

    data.append({"model": model, "price": price, "age": age})

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"\nДодано новий автомобіль: {model}")


# Видалення запису
def remove_car(filename, model):
    with open(filename, 'r') as file:
        data = json.load(file)

    data = [car for car in data if car['model'] != model]

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"\nАвтомобіль {model} видалено.")


# Основна функція запуску програми
def main():
    filename = 'cars_data.json'

    while True:
        print("\nМеню:")
        print("1. Вивести вміст JSON-файлу")
        print("2. Додати новий запис")
        print("3. Видалити запис")
        print("4. Обчислити середню вартість автомобілів, вік яких перевищує 6 років")
        print("5. Вийти")

        choice = input("Оберіть дію (1-5): ")

        if choice == '1':
            display_json(filename)
        elif choice == '2':
            model = input("Введіть модель: ")
            price = float(input("Введіть ціну: "))
            age = int(input("Введіть вік: "))
            add_car(filename, model, price, age)
        elif choice == '3':
            model = input("Введіть модель для видалення: ")
            remove_car(filename, model)
        elif choice == '4':
            calculate_average_price(filename)
        elif choice == '5':
            print("Вихід.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()

