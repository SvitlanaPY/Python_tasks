text = input()

a = set()
while text != '':
    slova = text.split()
    a.update(slova)
    print(a)
    text = input()
print(a)
