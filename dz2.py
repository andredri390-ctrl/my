import random

class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.skills = 5
        self.money = 50

    def hello(self):
        print(f'Hi. My name is {self.name}! I am {self.year}')
        print(f'My skills: {self.skills:.2f}')
        print(f'My money: {self.money:.2f}')

    def grow_up(self):
        self.year += 1

    def study(self):
        print('Studying... 👨‍🎓📚')
        self.skills += 0.3

    def chill(self):
        print('Chilling... 😎👍')
        self.skills -= 0.1
        self.money -= 5

    def work(self):
        print('Working... 💼')
        self.money += 10
        self.skills -= 0.05

    def live_day(self):
        if self.money < 10:
            print("I need money!")
            self.work()

        elif self.skills < 3:
            print("I must study!")
            self.study()

        else:
            choice = random.randint(1,3)

            if choice == 1:
                self.study()
            elif choice == 2:
                self.chill()
            else:
                self.work()

        print(f"Skills: {self.skills:.2f} | Money: {self.money:.2f}")
        print()


mark = Student("Mark", 13)

for day in range(1, 366):
    print(f'======= Day {day} =======')
    mark.live_day()

mark.grow_up()
mark.hello()