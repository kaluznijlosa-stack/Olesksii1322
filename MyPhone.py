import os
import sqlite3
import requests

connection = sqlite3.connect("phone112.sl3")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS phone (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pin TEXT NOT NULL,
    balance INTEGER NOT NULL
)
""")

cursor.execute("SELECT * FROM phone")

if cursor.fetchone() is None:
    cursor.execute("INSERT INTO phone (pin, balance) VALUES ('1234', 1000)")
    connection.commit()


while True:
    os.system("cls")
    pin = input("Введіть PIN: ")

    cursor.execute("SELECT pin FROM phone")
    if pin == cursor.fetchone()[0]:
        break
    else:
        print("Неправильний PIN!")
        input("Enter")


def bank():
    while True:
        os.system("cls")

        cursor.execute("SELECT balance FROM phone")
        balance = cursor.fetchone()[0]

        print("1. Баланс")
        print("2. Поповнити")
        print("3. Зняти")
        print("0. Назад")

        choice = input("Вибір: ")

        if choice == "1":
            print("Баланс:", balance)

        elif choice == "2":
            amount = int(input("Сума: "))
            if amount > 0:
                balance += amount
                cursor.execute("UPDATE phone SET balance = ?", (balance,))
                connection.commit()
                print("Рахунок поповнено!")
            else:
                print("Неправильна сума!")

        elif choice == "3":
            amount = int(input("Сума: "))
            if amount > 0 and amount <= balance:
                balance -= amount
                cursor.execute("UPDATE phone SET balance = ?", (balance,))
                connection.commit()
                print("Гроші знято!")
            else:
                print("Недостатньо коштів!")

        elif choice == "0":
            break

        else:
            print("Неправильний вибір!")

        input("Enter")


def calculator():
    os.system("cls")

    a = float(input("Перше число: "))
    action = input("Дія (+, -, *, /): ")
    b = float(input("Друге число: "))

    if action == "+":
        print(a + b)
    elif action == "-":
        print(a - b)
    elif action == "*":
        print(a * b)
    elif action == "/" and b != 0:
        print(a / b)
    else:
        print("Помилка!")

    input("Enter")


def weather():
    os.system("cls")

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 49.4444,
        "longitude": 32.0598,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }

    data = requests.get(url, params=params).json()

    print("Погода в Черкасах")
    print("Температура:", data["current"]["temperature_2m"], "°C")
    print("Вологість:", data["current"]["relative_humidity_2m"], "%")
    print("Вітер:", data["current"]["wind_speed_10m"], "км/год")

    input("Enter")


while True:
    os.system("cls")

    print("1. Банк")
    print("2. Калькулятор")
    print("3. Погода")
    print("0. Вимкнути")

    choice = input("Вибір: ")

    if choice == "1":
        bank()
    elif choice == "2":
        calculator()
    elif choice == "3":
        weather()
    elif choice == "0":
        break

connection.close()
