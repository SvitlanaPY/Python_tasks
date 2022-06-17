# create list:
c = (1, 2, 3)
cc = list(c)
print(cc, type(cc))   # print(list((1, 2, 3)))
# [1, 2, 3] <class 'list'>


a = 'hellohi'
aa = list(a)
print(aa, type(aa))
# ['h', 'e', 'l', 'l', 'o', 'h', 'i'] <class 'list'>


# a = list(map(str, input().upper().split()))
# print(a)

# s = input().split()
# print(s)
# print('\n'.join(s))

ss = input()
print(ss)
print('\n'.join(ss.split()))
