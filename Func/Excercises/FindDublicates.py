# Ваша задача написать функция find_duplicate, которая принимает один аргумент - список чисел.
# Функция должна возвращать список из дублей, каждый дубль нужно брать только один раз в том порядке,
# в котором они встречаются в исходном списке. Под дублем будем подразумевать число,
# которое присутствовало в списке несколько раз.
#
# Ваша задача написать только определение функции

def find_duplicate(list_):
    duplicates_list_ = []
    for i in list_:
        if i not in duplicates_list_ and list_.count(i) > 1:
            duplicates_list_.append(i)
    return duplicates_list_

print(find_duplicate([1, 2, 3]))