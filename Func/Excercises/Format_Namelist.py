# Ваша задача написать функцию format_namelist, которая принимает список словарей,
# у каждого словаря в списке есть только ключ name
#
# Функция format_namelist должна вернуть отформатированную строку,
# в которой все имена из списка разделяются запятой кроме последних двух имен,
# они должны быть разделены союзом "и".
# Если в списке нет ни одного имени, функция должна вернуть пустую строку. Ниже представлены примеры:
#
# format_namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# # returns 'Bart, Lisa и Maggie'
#
# format_namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# # returns 'Bart и Lisa'
#
# format_namelist([ {'name': 'Bart'} ])
# # returns 'Bart'
#
# format_namelist([])
# # returns ''

def format_namelist(dictionary):
    list_ = []
    for i in dictionary:
        for key, val in i.items():
            list_.append(val)
    print(list_)
    if len(list_) > 1:
        return (', '.join(list_[:-1])) + ' и ' + list_[-1]
    elif len(list_) == 1:
        return list_[0]
    else:
        return ''


print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
# Bart, Lisa и Maggie
print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
# Bart и Lisa
print(format_namelist([{'name': 'Bart'}]))
# Bart
print(format_namelist([]))
# ''
