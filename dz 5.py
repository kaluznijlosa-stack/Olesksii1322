users = {"Олексій": "Підліток", "Іван": "Дорослий", "Андрій": "Дитина", "Максим": "Підліток"}

while True:
    name = input("Введіть ім'я: ")

    if name in users:
        print("Вікова група:", users[name])
    else:
        print("Користувача не знайдено!")

    restart = input("Перезапустити програму? (y/n): ")

    if restart == "n":
        print("Програму завершено!")
        break