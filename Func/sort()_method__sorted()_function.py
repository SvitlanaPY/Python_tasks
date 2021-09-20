# Syntax:  list.sort(reverse=True|False, key=myFunc)
# The sort() method sorts the list ascending by default.
# sort - метод списків; не потребує присвоєння; змінює список, до якого застосовується.
# метод - це ф-ія, яка застосовується до об"єктів;
# викликається метод - ім"я_об"єкту.ім"я методу(параметри/аргументи)
a = [4, -10, 43, -300, 54, 89, -34]
a.sort()
print(a)   # [-300, -34, -10, 4, 43, 54, 89]
print()


# Syntax:  sorted(iterable, key=key, reverse=reverse)
# sorted() - collects all the elements of the iterable into a list, sorts the list, and returns the sorted result.
# sorted() function returns a sorted list of the specified iterable object.
# sorted() - вбудована функція, яка дозволяє сортувати різні ітерабельні об"єкти;
# вона НЕ змінює початкову колекцію, для зміни початкової колекції потрібно використати присвоєння;
# колекція має містити лише ітерабельну послідовність (тип даних, який можна обійти в циклі фор);
# вона завжди повертає список.
b = (4, -10, 43, -300, 54, 89, -34)
sorted(b)
print("b", b)   # список НЕ відсортувався  --> b: [4, -10, 43, -300, 54, 89, -34]
print(sorted(b))   # [-300, -34, -10, 4, 43, 54, 89]
b = sorted(b)
print("sorted_b: ", b)   # список змінився (відсортувався) --> b:  [-300, -34, -10, 4, 43, 54, 89]

print()
# обидва сортування приймають:
# key - це іменований аргумент, який приймає функцію та аргумент reverse - який приймає булеве значення (True чи False)
# параметр reverse відповідає за те, в якому порядку будуть сортуватись елементи;
# по замовчуванню reverse=False, і сортування відбувається по зростанню.


print("\nАРГУМЕНТ key В СОРТУВАННІ")
# KEY - аргумент, який приймає ф-ію і за допомогою якого можна змінити спосіб сортування

# в key можна передавати:
# 1) вбудовану ф-ію:
aa = [4, -10, 43, -300, 54, 289, -34, 8, 749]
print(sorted(aa, key=abs))
# [4, 8, -10, -34, 43, 54, 289, -300, 749]

print()
# 2) власну ф-ію:
def f(x):
    return x % 10  #  x // 10 % 10  - додатковий критерій сортування, записуємо через кому в return

aaa = [4, 10, 43, 300, 54, 289, 34, 8, 749]
print(sorted(aaa, key=f))
# [10, 300, 43, 4, 54, 34, 8, 289, 749]

print()
# 3) вбудовані методи об"єкту (key=str.lower):
s = ['ZZZ', 'aaa', 'eee', 'DDD', 'BBB', 'www']
print(sorted(s))   # ['BBB', 'DDD', 'ZZZ', 'aaa', 'eee', 'www']
print(sorted(s, key=str.lower))   # ['aaa', 'BBB', 'DDD', 'eee', 'www', 'ZZZ']

print()
# 4) анонімні ф-ії (lambda):
# посортувати по числах:
ss = ['ZZZ 79', 'aaa 45', 'eee 43', 'DDD 800', 'BBB 5', 'www 14']
print(sorted(ss, key=lambda x: int(x.split()[1])))
# ['BBB 5', 'www 14', 'eee 43', 'aaa 45', 'ZZZ 79', 'DDD 800']

# lambda x: int(x.split()[1], де x = елементи списку (стрічки),
# розбиваємо їх по пробілу x.split() і отримуємо список з двох елементів
# беремо елемент, що стоїть на першому місці в списку і переводимо його в інт

print()
# посортувати спершу по числу, а якщо числа співпали - то по алфавіту
sss = ['ZZZ 800', 'aaa 45', 'eee 43', 'ddd 800', 'BBB 43', 'www 14']
print(sorted(sss, key=lambda x: (int(x.split()[1]), x.split()[0].lower())))
# ['www 14', 'BBB 43', 'eee 43', 'aaa 45', 'ddd 800', 'ZZZ 800']

print()
# !!!!!!! сортування словника по ключу і значенню одночасно:
dict_artist = {'Colorado': 1230, 'Boston': 1400, 'Minnesota': 2000, 'Milwaukee': 1400, 'Kansas City': 1400}
# dict_artist = {'Colorado': 'Rockies', 'Boston': 'Red Sox', 'Minnesota': 'Twins', 'Milwaukee': 'Brewers', 'Kansas City': 'Royals'}
print(sorted(dict_artist.items(), key=lambda x: (x[1], x[0])))      # - На выходе имеем list из кортежей
# [('Colorado', 1230), ('Boston', 1400), ('Kansas City', 1400), ('Milwaukee', 1400), ('Minnesota', 2000)]
# [('Milwaukee', 'Brewers'), ('Boston', 'Red Sox'), ('Colorado', 'Rockies'), ('Kansas City', 'Royals'), ('Minnesota', 'Twins')]


print()
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
# 20. Sort lst_to_sort from min to max
print(sorted(lst_to_sort))
# OUTPUT: [1, 5, 13, 15, 18, 24, 33, 55]

print()
# 21. Sort lst_to_sort from max to min
print(sorted(lst_to_sort, reverse=True))
# OUTPUT: [55, 33, 24, 18, 15, 13, 5, 1]
