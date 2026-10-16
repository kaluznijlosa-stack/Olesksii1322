import random

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.skills = 1
        self.money = 100

    def info(self):
        print(f"My name is {self.name} and I am {self.age} years old")
        print(f"Skills: {self.skills}")
        print(f"Money: ${self.money}")


    def study(self):
        self.skills += 1

    def chill(self):
        self.skills -= 0.5
        self.money -= 50
        self.money -= random.randint(25,100)
        print("Chilling...😊💪")

    def work(self):
        self.skills += 0.5
        self.money += 50
        print("Hard working...😊💪")

alex = Student("Alex", 13)
john = Student("John", 12)

alex.info()
john.info()

for day in range(365):
    alex.choice = random.randint(1, 3)
    john.choice = random.randint(1, 3)

    if alex.choice == 1:
        alex.study()
    elif alex.choice == 2:
        alex.chill()
    else:
        alex.work()

alex.age += 1
alex.info()


