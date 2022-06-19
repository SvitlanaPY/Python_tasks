# create list:
c = (1, 2, 3)
cc = list(c)
print(cc, type(cc))   # print(list((1, 2, 3)))
# [1, 2, 3] <class 'list'>


a = 'hellohi'
aa = list(a)
print(aa, type(aa))
# ['h', 'e', 'l', 'l', 'o', 'h', 'i'] <class 'list'>


b = [1, 2, 3]
a_a, b_b, c_c = b
print('a_a=', a_a, 'b_b=', b_b, 'c_c=', c_c)


# a = list(map(str, input().upper().split()))
# a = list(map(int, input("Enter (3 4 5 2 1): ").split()))
# print(a)

# s = input().split()
# print(s)
# print('\n'.join(s))

# ss = input()
# print(ss)
# print('\n'.join(ss.split()))
