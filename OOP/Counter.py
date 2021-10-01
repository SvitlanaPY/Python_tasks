class Counter:
    def start_from(self, value=0):
        self.counter = value

    def increment(self):
        self.counter += 1

    def display(self):
        print(f"Дане значення лічильника = {self.counter}")

    def reset(self):
        self.counter = 0


c1 = Counter()
c1.start_from()
print(c1.display())
# Дане значення лічильника = 0
c1.increment()
print(c1.display())
# Дане значення лічильника = 1
c1.increment()
print(c1.display())
# Дане значення лічильника = 2
c1.increment()
print(c1.display())
# Дане значення лічильника = 3
c1.reset()
print(c1.display())
# Дане значення лічильника = 0

c2 = Counter()
c2.start_from(3)
print(c2.display())
# Дане значення лічильника = 3
c2.increment()
print(c2.display())
# Дане значення лічильника = 4
c2.increment()
print(c2.display())
# Дане значення лічильника = 5
