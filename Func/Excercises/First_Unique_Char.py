# Напишите функцию first_unique_char, которая принимает строку символов и
# возвращает позицию первого уникального символа в строке.
# В случае, если уникальных символов в переданной строке нет, верните -1.
# Регистр символов не учитывайте.
#
# Sample Input 1:
# python
# Sample Output 1:
# 0
#
# Sample Input 2:
# abracadabra
# Sample Output 2:
# 4
#
# Sample Input 3:
# abcabc
# Sample Output 3:
# -1


def first_unique_char(text):
    text = text.lower()
    for elem in text:
        elem_count = text.count(elem)
        if elem_count > 1:
            continue
        return text.find(elem)
    return -1
print(first_unique_char(input()))


# def first_unique_char(text):
#     text = text.lower()
#     i = 0
#     for elem in text:
#         if text.count(elem) > 1:
#             i += 1
#         elif text.count(elem) == 1:
#             return i
#     return -1
# print(first_unique_char(input()))