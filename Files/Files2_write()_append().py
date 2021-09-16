# file4 = open('222.txt', 'a')
# # print(file4.read())
# file4.write('hello\n')
# file4.write('Hi')
# # print(file4.read())
# file4.close()


file5 = open('222.txt', 'r+')
# file5.write('555hello\n')
# file5.write('555hello\n')
# file5.write('555hi\n')
file5.write('999hi\n')
file5.read()
file5.close()


f = open("test.txt", "w")
f.write("test.txt\n")
f.write("HELLO!\n")
f.write("world!\n")
f.write("bye world!")
f.close()


ff = open("test1.txt", "w")
lines = ["Line1", "Line2", "Line3"]
contents = "\n".join(lines)
ff.write(contents)
ff.close()


fff = open("test_append.txt", "a")
fff.write("Hello\n")
fff.close()


t = open("test_write.txt", "w")
t.write("Kine2\n")
t.write("Kine1")
t.close()


# with open("test1.txt") as qqq, open("test1_copy.txt", "r+") as www:
#     for line in qqq:
#         www.write(line)
