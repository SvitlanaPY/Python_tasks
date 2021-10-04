"""
Extending - створення у дочірньому класі атрибуту чи методу такого, якого немає у батьківського класу.
"""
class Person:   # parent class

    def breathe(self):
        print("Person can breathe")


class Doc(Person):    # sub-class
    def sleep(self):
        print("Doctor can sleep")

p = Person()
# p.sleep()   # AttributeError: 'Person' object has no attribute 'sleep'
d = Doc()
d.sleep()
# Doctor can sleep
p.breathe()
# Person can breathe
d.breathe()
# Person can breathe


print()
class Person1:   # parent class

    def breathe(self):
        print("Person can breathe")

    def sleep(self):
        print("Person can sleep")

    def combo(self):
        self.breathe()
        self.sleep()
        self.walk()


class Doc1(Person1):    # sub-class
    def sleep(self):
        print("Doctor can sleep")

    def breathe(self):
        print("Doctor can breathe")

    def walk(self):
        print("Doctor can walk")


pp = Person1()
# pp.combo()   # AttributeError: 'Person1' object has no attribute 'walk'
dd = Doc1()
dd.combo()
# Doctor can breathe
# Doctor can sleep
# Doctor can walk


print()
class Person2:   # parent class

    def breathe(self):
        print("Person can breathe")

    def sleep(self):
        print("Person can sleep")

    def combo(self):
        self.breathe()
        self.sleep()
        if hasattr(self, "walk"):
            self.walk()


class Doc2(Person2):    # sub-class

    def sleep(self):
        print("Doctor can sleep")

    def breathe(self):
        print("Doctor can breathe")

    def walk(self):
        print("Doctor can walk")


p_ = Person2()
p_.combo()
# Person can breathe
# Person can sleep
print("-"*20)
# --------------------
d_ = Doc2()
d_.combo()
# Doctor can breathe
# Doctor can sleep
# Doctor can walk


print()
class Person3:   # parent class

    def breathe(self):
        print("Person can breathe")

    def sleep(self):
        print("Person can sleep")

    def combo(self):
        self.breathe()
        self.sleep()
        if hasattr(self, "walk"):
            self.walk()
        if hasattr(self, "age"):
            print(self.age)


class Doc3(Person3):    # sub-class

    age = 30

    def sleep(self):
        print("Doctor can sleep")

    def breathe(self):
        print("Doctor can breathe")

    def walk(self):
        print("Doctor can walk")

pp_ = Person3()
pp_.combo()
# Person can breathe
# Person can sleep
print("-"*20)
# --------------------
dd_ = Doc3()
dd_.combo()
# Doctor can breathe
# Doctor can sleep
# Doctor can walk
# 30
