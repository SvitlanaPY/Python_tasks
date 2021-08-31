# Видалити зі списку усі елементи, значення яких = 3
a = [1, 2, 3] * 5
print(a)

while 3 in a:
    a.remove(3)
    print(a)