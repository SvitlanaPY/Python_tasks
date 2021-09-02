# for i in range(3):
#     for j in range(5):
#         print(i, end='')
#         # print(j, end='')
#     print()
# 00000
# 11111
# 22222


# for i in range(3):
#     for j in range(5):
#         print(j, end='')
#     print()
# 01234
# 01234
# 01234


# for i in range(6):
#     for j in range(i+1):
#         print(j, end='')
#     print()
# 0
# 01
# 012
# 0123
# 01234
# 012345


# for i in range(1, 4):
#     for j in range(10, 13):
#         print(i, ' ', j)
# 1   10
# 1   11
# 1   12
# 2   10
# 2   11
# 2   12
# 3   10
# 3   11
# 3   12


from string import printable
print(printable)
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# 