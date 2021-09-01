n, m = map(int, input().split())
a = 0
count = 0
while a**2 <= n:
    b = n - a**2
    if b >= 0 and a + b ** 2 == m:
        count += 1
        # print(a, b)
    a += 1
print(count)
