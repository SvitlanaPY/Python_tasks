from time import perf_counter

print("Task1")
# """
# 1. Написати функцію яка в циклі зчитує з консолі введені користувачем дані і записує їх в список.
# Написати декоратор який видасть час виконання роботи функції
# """
def f():
    m = input("Enter some data (or Q to exit): ")
    list_t = []
    while m != 'Q':
        list_t.append(m)
        m = input()
    return list_t


print('list_t:', f())


print("\nTask2")
# """
# 2. Написати функцію яка приймає два катети і повертає значення гіпотензузи.
# Написати декоратор на функцію, який виводить на екран текст з довжиною катетів і гіпотенузи.
# Важливо! Функція повинно повернути саме значення гіпотенузи як число,
# а декоратор повинен зробити вивід на екран, наприклад, такого тексту “При катетах 3, 4 – гіпотенуза дорівнює 5”.
# """
def hyp(a, b):
    return (a ** 2 + b ** 2) ** 0.5


print(hyp(3, 4))


print("\nTask3")
# """
# 3. Написати функцію яка приймає список елементів і знаходить суму,
# до функції написати декоратор, який перед тим як запустити функцію видаляє з списку всі не чисельні типи даних,
# але якщо є строка, яку можна перевести в число, (наприклад “1”) то строка приводиться до чисельного типу даних.
# """
def summa(list_t):
    new_list = []
    for i in list_t:
        try:
            i = float(i)
            new_list.append(i)
        except ValueError:
            continue
    return sum(new_list)


lst = [5, 10, '4', 1, 'hi', 10.5, 6, '4.5', 5]
print(summa(lst))


print("\nTask4")
# """
# 4. Написати функцію, яка приймає на вхід ціле число n, створює та повертає список цілих чисел від 0 до n.
# Написати до цієї функції декоратор, який всі елементи отриманого списку, переведе в строковий тип даних
# """
def ff():
    n = int(input('Enter some number: '))
    return list(range(n))


print(ff())
