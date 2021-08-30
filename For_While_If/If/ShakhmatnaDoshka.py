str_ = '_abcdefgh'
coord_1 = input()     # 'a3'
letter = coord_1[0]   # a
column_1 = str_.find(letter)   # 1
row_1 = int(coord_1[1])   # 3
print(row_1, column_1)    # 3 1
coord_2 = input()     # 'f4'
letter2 = coord_2[0]   # 4
column_2 = str_.find(letter2)   # 6
row_2 = int(coord_2[1])   # 4
print(row_2, column_2)    # 4 6

if ((row_1 + column_1) % 2 == 0 and (row_2 + column_2) % 2 == 0) or ((row_1 + column_1) % 2 == 1 and (row_2 + column_2) % 2 == 1):
    print("YES")
else:
    print("NO")

# if ((column_1 % 2 == 0 and row_1 % 2 == 0) and (column_2 % 2 == 0 and row_2 % 2 == 0)) \
#         or ((column_1 % 2 == 0 and row_1 % 2 == 0) and (column_2 % 2 == 1 and row_2 % 2 == 1)) \
#         or ((column_1 % 2 == 1 and row_1 % 2 == 1) and (column_2 % 2 == 1 and row_2 % 2 == 1)) \
#         or ((column_1 % 2 == 1 and row_1 % 2 == 1) and (column_2 % 2 == 0 and row_2 % 2 == 0)):
#     print("YES")
# else:
#     print("NO")
