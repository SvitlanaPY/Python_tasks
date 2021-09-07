# Дили Вили Били завели себе аккаунты в одной известной соцсети.
# И затем они решили узнать у кого из них самое большое количество уникальных комментатор.
# Ваша задача помочь им в этом и собрать нужную информацию.
#
# Входные данные
# В каждой строке будет вводиться одно из имен наших героев, а затем через двоеточие и пробел имя комментатора.
# Комментаторы могут повторяться и комментировать разных персонажей
# Строка "конец" означает окончание ввода и встречается последней

# Выходные данные
# Ваша задача вывести в порядке уменьшения популярности 3 строки вида:
# "Количество уникальных комментаторов у <имя героя> - <количество комментаторов>"
# На склонение давайте не будем обращать обращать внимания в этой задаче.
#
# Гарантируется, что количество уникальных комментаторов у всех наших героев разное.
# Могут быть ситуации, когда у героя нету ни единого комментатора,
# в таком случае все равно нужно выводить информацию о нем.
#
# Sample Input 1:
# Дили: navalny
# Дили: realdonaldtrump
# Били: navalny
# Вили: realdonaldtrump
# Вили: realdonaldtrump
# Били: joebiden
# Дили: joebiden
# конец
# Sample Output 1:
# Количество уникальных комментаторов у Дили - 3
# Количество уникальных комментаторов у Били - 2
# Количество уникальных комментаторов у Вили - 1
#
# Sample Input 2:
# Дили: aaaa
# Дили: aaaa
# Били: aaaa
# Дили: aaaa
# Били: aaa
# конец
# Sample Output 2:
# Количество уникальных комментаторов у Били - 2
# Количество уникальных комментаторов у Дили - 1
# Количество уникальных комментаторов у Вили - 0

dict_ = {'Били': set(), 'Дили': set(), 'Вили': set()}
reversed_dict = {}
while True:
    text = input()
    if text == 'конец':
        break
    name, comment = text.split(': ')
    dict_[name].add(comment)   # or:
    # dict_[name] = d.get(name, set())
    # dict_[name].add(comment)
# print("dict_ ", dict_)

# reversed_dict = {len(val): key for key, val in dict_.items()}
for key, val in dict_.items():
    key, val = val, key
    reversed_dict[len(key)] = val
# print("reversed_dict ", reversed_dict)

for k, v in sorted(reversed_dict.items(), reverse=True):
    print(f"Количество уникальных комментаторов у {v} - {k}")


# dict_[name] = dict_.get(name, []) + [comment]