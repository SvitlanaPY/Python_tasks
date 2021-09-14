file2 = open('222.txt')

for row in file2:
    print(row)
    # print(repr(row))


print()
file3 = open('333.txt')
for row in file3:
    for letter in row:
        print(letter)


print()
file1 = open('111.txt')
s = file1.readlines()
print("s: ", s)


file1.close()
file2.close()
file3.close()


file4 = open("333.txt")
for line in file4:
    print(repr(line))
# 'First Line\n'
# 'Second Line\n'
# 'Third Line'


print()
file44 = open("333.txt")
for line in file44:
    line = line.rstrip()
    print(repr(line))
# 'First Line'
# 'Second Line'
# 'Third Line'

file4.close()
file44.close()
