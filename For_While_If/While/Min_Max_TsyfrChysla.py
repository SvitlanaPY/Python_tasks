"""
Программа принимает на вход одно натуральное число и выводит на экран минимальную
и максимальную цифры данного числа в отдельных строчках.

Sample Input 1:
480
Sample Output 1:
0
8

Sample Input 2:
123
Sample Output 2:
1
3

Sample Input 3:
99
Sample Output 3:
9
9
"""

x = int(input())
max_num = 0
min_num = 9
while x > 0:
    last = x % 10
    if last > max_num:
        max_num = last
    if last < min_num:
        min_num = last
    x = x // 10
print(min_num, max_num, sep='\n')


# b = list(map(int, input().replace('', ' ').strip().split()))
# print(min(b), max(b), sep='\n')
