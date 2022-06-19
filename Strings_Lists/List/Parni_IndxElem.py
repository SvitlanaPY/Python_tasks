print("Выведите все элементы списка с четными индексами (то есть A[0], A[2], A[4], ...).")
# a = input().split()
a = ['1', '2', '3', '4', '5']
print("a: ", a)
for i in range(0, len(a), 2):
    print(a[i])


print("\nВыведите все элементы списка с четными индексами")
b = ['1', '2', '3', '4', '5']
print("b: ", b)
for i in range(len(b)):
    if i % 2 == 0:
        print(b[i])


print("\nВыведите все четные элементы списка. "
      "При этом используйте цикл for, перебирающий элементы списка, а не их индексы")
# aa = input().split()
aa = ['1', '2', '2', '3', '3', '3', '4']
print("aa: ", aa)
for i in aa:
   if int(i) % 2 == 0:
       print(i, end=' ')


print("\nВыведите все четные элементы списка. "
      "При этом используйте цикл for, перебирающий элементы списка, а не их индексы")
# c = [int(i) for i in input().split()]   # create list input().split() with string elements and convert elements into integer by int(i)
c = list(map(int, input("Enter few numbers: 2 4 6 7 9 8").split()))
print("c: ", c)
for ii in c:
    if ii % 2 == 0:
        print(ii, end=' ')
