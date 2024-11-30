
import json

# Дані про автомобілі
cars = [
    {"model": "Ford Fiesta", "age": 5, "price": 5000},
    {"model": "Toyota Corolla", "age": 8, "price": 8000},
    {"model": "Honda Civic", "age": 10, "price": 7500},
    {"model": "BMW 3 Series", "age": 3, "price": 15000},
    {"model": "Audi A4", "age": 7, "price": 12000},
    {"model": "Mercedes-Benz C-Class", "age": 9, "price": 20000},
    {"model": "Volkswagen Golf", "age": 4, "price": 7000},
    {"model": "Hyundai Elantra", "age": 11, "price": 6500},
    {"model": "Kia Rio", "age": 6, "price": 6200},
    {"model": "Nissan Sentra", "age": 12, "price": 5800}
]

# Запис даних у JSON файл
with open("cars.json", "w", encoding="utf-8") as file:
    json.dump(cars, file, ensure_ascii=False, indent=4)

def calculate_average_price(cars):
    # Фільтрація автомобілів, вік яких перевищує 6 років
    filtered_cars = [car for car in cars if car['age'] > 6]
    
    # Якщо немає автомобілів, що відповідають критеріям, повертаємо повідомлення
    if not filtered_cars:
        return "Немає автомобілів віком більше 6 років."
    
    # Розрахунок середньої вартості
    total_price = sum(car['price'] for car in filtered_cars)
    average_price = total_price / len(filtered_cars)
    
    return average_price

while True:
    print("Select an option:\n1 - Calculate average price of cars older than 6 years\n2 - View car data\n3 - Exit")
    option = input("Choose an option: ")
    
    if option == "1":
        average_price = calculate_average_price(cars)
        if isinstance(average_price, str):
            print(average_price)
        else:
            print(f"Середня вартість автомобілів віком більше 6 років: {average_price:.2f} USD")
    elif option == "2":
        with open("cars.json", "r", encoding="utf-8") as file:
            cars_data = json.load(file)
            print(json.dumps(cars_data, ensure_ascii=False, indent=4))
    elif option == "3":
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
