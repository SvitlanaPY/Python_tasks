"""
https://uk.wikipedia.org/wiki/%D0%A2%D1%80%D0%B8%D0%BA%D1%83%D1%82%D0%BD%D0%B8%D0%BA_%D0%9F%D0%B0%D1%81%D0%BA%D0%B0%D0%BB%D1%8F#/media/%D0%A4%D0%B0%D0%B9%D0%BB:PascalTriangleAnimated2.gif
1  0  0  0  0  0  0  0
1  1  0  0  0  0  0  0
1  2  1  0  0  0  0  0
1  3  3  1  0  0  0  0
1  4  6  4  1  0  0  0
1  5 10 10  5  1  0  0
1  6 15 20 15  6  1  0
1  7 21 35 35  21 7  1
перший(нульовий) стовпець - всі '1'-нички
кожен наступний рядок формується за правилом:
елемент рядка  - це сума сусідніх верхніх елементів.
Приклад заповнення остнаннього рядка:
1  6 15 20 15  6  1  0
1  7 21 35 35  21 7  1
7 - це 1 + 6
21 = 6 + 15
35 = 15 + 20
35 = 20 + 15
21 = 15 + 6
7 = 6 + 1
1 = 1 + 0
"""

n = int(input())
triangle = []
for i in range(n + 1):
    triangle.append([1] + [0] * n)
print(triangle)   # [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]

for i in triangle:
    print(i)
# [1, 0, 0, 0, 0]
# [1, 0, 0, 0, 0]
# [1, 0, 0, 0, 0]
# [1, 0, 0, 0, 0]
# [1, 0, 0, 0, 0]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]

for i in range(0, n + 1):
    for j in range(0, n + 1):
        print(triangle[i][j], end=' ')
    print()
# 1 0 0 0 0
# 1 1 0 0 0
# 1 2 1 0 0
# 1 3 3 1 0
# 1 4 6 4 1
