class Task:
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.done = False


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Завдання додано!")

    def show_tasks(self):
        for task in self.tasks:
            print("----------------")
            print("Назва:", task.name)
            print("Опис:", task.description)
            print("Дедлайн:", task.deadline)

            if task.done:
                print("Стан: Виконано")
            else:
                print("Стан: Не виконано")

    def complete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                task.done = True
                print("Завдання виконано!")


manager = TaskManager()

while True:
    print("1. Додати завдання")
    print("2. Показати завдання")
    print("3. Виконати завдання")
    print("4. Вийти")

    choice = input("Ваш вибір: ")

    if choice == "1":
        name = input("Назва: ")
        description = input("Опис: ")
        deadline = input("Дедлайн: ")

        task = Task(name, description, deadline)
        manager.add_task(task)

    elif choice == "2":
        manager.show_tasks()

    elif choice == "3":
        name = input("Назва завдання: ")
        manager.complete_task(name)

    elif choice == "4":
        break
