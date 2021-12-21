n = 12345
# print(len(str(n)))

# summ = 0
for i in range(1, len(str(n))+1):
    print('i =', i)
    print(f"{n} % 10 = ", int(n % 10))
    print(f"{n} // 10 = ", int(n // 10))
    n = n // 10
    print()


# print(summ)
# print(n % 10)
