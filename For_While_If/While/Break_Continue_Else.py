# вивести YES, якщо ВСІ числа в списку парні. Якщо хоча б одне число непарне - виводимо NO
# блок else НЕ виконується, коли цикл завершується по break-у!)
a = [54, 32, 65, 756, 32, 543]
while len(a) > 0:
    last = a.pop()
    if last % 2 != 0:
        print("NO")
        break
else:
    print("YES")
print("STOP")
# NO
# STOP

# вивести YES, якщо ВСІ числа в списку парні. Якщо хоча б одне число непарне - виводимо NO
# блок else виконується лише тоді, коли цикл завершується сам по собі (коли break НЕ виконався!)
aa = [22, 10, 4, 6, 14]
while len(aa) > 0:
    last = aa.pop()
    if last % 2 != 0:
        print("NO")
        break
else:
    print("YES")
print("STOP")
# YES
# STOP



# while True:
#     a = input()
#     if a == 'exit':
#         break
#         print("Good bye")
#     if len(a) < 5:
#         continue
#         print("Continue")
#     print(a, len(a))
# print("The END")