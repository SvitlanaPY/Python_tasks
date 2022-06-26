# "Правильная скобочная последовательность" (Stack LIFO = Last In First Out)
# Наша программа принимает на вход последовательность скобочных символов.
# Ваша задача определить является ли введенная скобочная последовательность правильной.
# Правильная скобочная последовательность (ПСП) называется строка, состоящая только из символов "скобки",
# где каждой закрывающей скобке найдётся соответствующая открывающая (причём того же типа).
# При этом учитывайте, что:
    # Пустая последовательность является правильной.
    # Если A – правильная скобочная последовательность, то (A), [A] и {A} – правильные скобочные последовательности.
    # Если A и B – правильные скобочные последовательности, то AB – правильная скобочная последовательность.
# Если введенная строка является ПСП, выведите YES, в противном случае - NO.

# Sample Input 1:
# []
# Sample Output 1:
# YES

# Sample Input 2:
# [(])
# Sample Output 2:
# NO

# Sample Input 3:
# {[]}()
# Sample Output 3:
# YES

# STEPS:
s = input()
stack = []
is_fit = True
for i in s:
    if i in '({[':
        stack.append(i)
    elif i in ')}]':
        open_bracket = stack.pop()
        if open_bracket == '(' and i == ')':
            continue
        if open_bracket == '{' and i == '}':
            continue
        if open_bracket == '[' and i == ']':
            continue
        is_fit = False
        break
if is_fit:
    print('YES')
else:
    print('NO')



s = input()
stack = []
is_fit = True
for i in s:
    if i in '({[':
        stack.append(i)
    elif i in ')}]':
        if len(stack) == 0:   # ситуація, коли стек порожній, а закриваючий елемент ще існує: (())))
            is_fit = False
            break
        open_bracket = stack.pop()
        if open_bracket == '(' and i == ')':
            continue
        if open_bracket == '{' and i == '}':
            continue
        if open_bracket == '[' and i == ']':
            continue
        is_fit = False
        break
if is_fit and len(stack) == 0:   # ситуація, коли в стеку залишився елемент, який немає з чим порівнювати: (((())
    print('YES')
else:
    print('NO')
