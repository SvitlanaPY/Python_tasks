class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1
        print(f"Робот {self.name} был создан")

    def destroy(self):
        Robot.population -= 1
        print(f'Робот {self.name} был уничтожен')

    def say_hello(self):
        print(f'Робот {self.name} приветствует тебя, особь человеческого рода')

    @classmethod
    def how_many(cls):
        print(f'{cls.population}, вот сколько нас еще осталось')


r2 = Robot("R2-D2")
# Робот R2-D2 был создан
r2.say_hello()
# Робот R2-D2 приветствует тебя, особь человеческого рода
Robot.how_many()
# 1, вот сколько нас еще осталось
r2.destroy()
# Робот R2-D2 был уничтожен
r3 = Robot("Sirius")
r3.say_hello()
Robot.how_many()
r4 = Robot("Orion")
r4.say_hello()
Robot.how_many()
