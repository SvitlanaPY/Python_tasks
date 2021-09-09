# ф-ія isinstance() дозволяє перевірити, до якого типу об"єкта належить ваше значення:
# першим параметром ф-ія приймає саме значення, яке ми хочемо перевірити,
# а другим параметром іде тип, на який ми перевіряємо наше значення
# якщо потрібно перевірити значення на кілька типів одночасно, то в другий параметр передаємо кортеж з типами
# isinstance(val, (int, float)).

a = [5, 3, (77,), 'hello', [3, 4], ' world', [5], 10.5, (1, 3, 6), 12.27]
# for i in a:
#     print(type(i))

# <class 'int'>
# <class 'int'>
# <class 'str'>
# <class 'list'>
# <class 'str'>
# <class 'list'>
# <class 'float'>
# <class 'tuple'>

s_str = ''
s_list = []
s_tpl = ()
summ_ = 0
for j in a:
    if isinstance(j, str):
        s_str += j
    elif isinstance(j, list):
        s_list += j
    elif isinstance(j, tuple):
        s_tpl += j
    elif isinstance(j, (int, float)):
        summ_ += j
print(s_str)    # hello world
print(s_list)   # [3, 4, 5]
print(s_tpl)    # (77, 1, 3, 6)
print(summ_)    # 30.77


for k in a:
    if isinstance(k, (float, int)):
        print(f"{k} - {type(k)}")
# 5 - <class 'int'>
# 3 - <class 'int'>
# 10.5 - <class 'float'>
# 12.27 - <class 'float'>


print()
# 4*. Check the type of the objects by using isinstance.
# int_a = 55
# str_b = 'cursor'
# set_c = {1, 2, 3}
# lst_d = [1, 2, 3]
# dict_e = {'a': 1, 'b': 2, 'c': 3}
# def type_definition(v):
#     if isinstance(v, str):
#         print('type is str')
#     elif isinstance(v, int):
#         print('type is int')
#     elif isinstance(v, list):
#         print('type is list')
#     elif isinstance(v, dict):
#         print('type is dict')
#     elif isinstance(v, set):
#         print('type is set')
#     elif isinstance(v, tuple):
#         print('type is tuple')
#     elif isinstance(v, float):
#         print('type is float')
#
# type_definition(int_a)    # OUTPUT: type is str
# type_definition(str_b)    # OUTPUT: type is int
# type_definition(set_c)    # OUTPUT: type is set
# type_definition(lst_d)    # OUTPUT: type is list
# type_definition(dict_e)   # OUTPUT: type is dict
#