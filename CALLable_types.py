# callable object - це такий об"єкт, до якого можна застосувати оператор виклику - ()

a = 10
# a()   # -> TypeError: 'int' object is not callable
# TypeError також буде, коли ми до строкового типу застосуємо оператор виклику

# CALLABLE типами є:
print("# 1: ")
# 1. Вбудовані ф-ії: len(), abs(), ф-ія int()
print(callable(len))   # True
print(callable(int))   # True


print("\n# 2: ")
# 2. Вбудовані методи:
b = [11, 5, 77, 101, 2]
print(callable(b.sort))   # True


print("\n# 3: ")
# 3. власні ф-ії та анонімна ф-ія lambda
def f():
    print("hello world")
print(callable(f))   # True

d = lambda : 'hi'
print(callable(d))   # True


print("\n# 4: ")
# 4. Класи:
class Cat:
    pass
print(callable(Cat))   # True


print("\n# 5: ")
# 5. Екземпляри класу (якщо є метод __call__)
class Cat:
    def __call__(self, *args, **kwargs):
        print("МЯУ-МУРррррр")
Tom = Cat()
print(callable(Tom))   # True
Tom()


print("\n# 6: ")
# Методи класу, які створили самі:
class Greetings:
    def say_hello(self):
        print("HELLO")

obj = Greetings()
obj.say_hello()
print(callable(obj.say_hello))   # True


print("\n# 7: ")
# 7. Ф-ії генератори (ф-ії, що містять інструкції yield:
def ff():
    n = 0
    while True:
        yield n
        n += 1

print(callable(ff))    # True
