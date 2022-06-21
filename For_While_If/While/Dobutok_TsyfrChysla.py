"""
Програма приймає на вхід одне натуральне число і виводить на екран добуток цифр даного числа.

Sample Input 1:
415
Sample Output 1:
20

Sample Input 2:
102
Sample Output 2:
0
"""

x = int(input())
result = 1
while x > 0:
    last = x % 10
    result *= last
    x = x // 10
print(result)
