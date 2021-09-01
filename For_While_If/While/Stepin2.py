n = int(input("Enter some number: "))
print(f"You entered: {n}")
i = 0
while 2 ** i < n:
    # print(i, f":  2 ** {i} =", 2 ** i)
    i += 1
if 2 ** i == n:
    print(i, f":  2 ** {i} =", 2 ** i)
    print(f"{n} є ступенем двійки")
else:
    print("NO")
    print(f"{n} НЕ є ступенем двійки")
