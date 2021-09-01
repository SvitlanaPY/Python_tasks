# В первый день спортсмен пробежал X километров.
# В каждый последующий день он увеличивал пробег на 15% от предыдущего дня.
# Вам необходимо определить номер дня, в который пробег спортсмена составил не менее Y километров.
# Само число Y будем поступать на вход программе.

# Входные данные:
# Программа получает на вход два положительных вещественных числа X и Y (X,Y ≤ 1000).
# Выходные данные:
# Выведите целое число – номер дня, в который спортсмен пробежал не менее Y километров.

# Sample Input 1:
# 10 20
# Sample Output 1:
# 6

# Sample Input 2:
# 1 1000
# Sample Output 2:
# 51

x, y = map(int, input().split())
day = 1
while x <= y:
    x = x + (15 * x) / 100
    day += 1
print(day)