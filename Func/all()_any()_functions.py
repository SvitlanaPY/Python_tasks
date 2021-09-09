# потрібні для того, щоб перевірити кілька об"єктів на їх заповненість чи пустоту
# ф-ія all() приймає колекцію, пробігається по всіх елементах колекції і перевіряє їх на тип bool
# якщо ВСІ елементи колекції є НЕпусті (тобто є True-типу), то вона поверне TRUE.
# FALSE повернеться тоді, коли хоча б один (або ВСІ) елемент/-и колекції є пустим/-и (False-типу)

a = ['hello', 'hi', 'bye', 'world']
print(all(a), " - a")
# True  - бо всі строки є НЕпусті

aa = ['hello', 'hi', 'bye', 'world', '']
print(all(aa), " - aa")
# False  - бо останній елемент колекції є пустий/False

aaa = ['', [], '', 0]
print(all(aaa), " - aaa")
# False


print()
# ф-ія any() теж приймає колекцію, і вона поверне TRUE, якщо хоча б один елемент колекції буде НЕпустим
b = ['', [], 0, 'world']
print(any(b), " - b")
# True

bb = ['', [], 0]
print(any(bb), " - bb")
# False


print()
# ці ф-ії корисні, якщо потрібно перевірити одночасно кілька умов:
k = 100
condition_1 = k % 2 == 0   # true
condition_2 = k > 50       # true
condition_3 = k < 1000     # true
print(all([condition_1, condition_2, condition_3]))
# True
print(any((condition_1, condition_2, condition_3)))
# True


print()
n = 99
condition_1 = n % 2 == 0   # false
condition_2 = n > 50       # true
condition_3 = n < 1000     # true
print(all([condition_1, condition_2, condition_3]))
# False
print(any((condition_1, condition_2, condition_3)))
# True

print()
m = 1
condition_1 = m % 2 == 0   # false
condition_2 = m > 50       # false
condition_3 = m > 1000     # false
print(all([condition_1, condition_2, condition_3]))
# False
print(any((condition_1, condition_2, condition_3)))
# False
