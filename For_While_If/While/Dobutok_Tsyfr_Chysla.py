x = int(input())
result = 1
while x > 0:
    last = x % 10
    result *= last
    x = x // 10
print(result)
