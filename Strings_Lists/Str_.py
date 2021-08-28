print("""test1
test2
test3""")
# or
print('''test1
test2
test3''')
# or
print("test1\ntest2\ntest3")
# OUTPUTS:
# test1
# test2
# test3

# КОНКАТЕНАЦІЯ
a = 'abc'
b = 'def'
c = 'W'
print(a+b)   # abcdef
print('abc'+(str(3)))   # abc3
# ПОВТОРЕННЯ (МНОЖЕННЯ)
print(c*5)   # WWWWW

# len() - ДОВЖИНА СТРОКИ
# print(len(a))   # 3
# S = input()
# print("You entered", len(S), "symbols")   # You entered S symbols

m = "!@#$%^&*.,/?"
print('@' in m)   # True

# ord()   - asci code of character
print(ord('1'), ord('A'), ord('№'))   # 49 65 8470

print(ord('a'), ord('r'))   # 97 114
print('a' > 'r')   # False

print('abc' < 'abcd')   # True
print('input' == 'input ')   # False

print('''Лев Николаевич Толстой написал "Война и мир"''')
