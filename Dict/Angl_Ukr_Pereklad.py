words = {}
while True:
    s = input()
    if s == "Q":
        break
    elif s in words:
        print(f"Слово {s} перекладається як {words[s]}")
    else:
        print(f"Введіть переклад слова - {s}")
        words[s] = input()
print(words)
