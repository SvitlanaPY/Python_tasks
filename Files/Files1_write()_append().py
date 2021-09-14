# file4 = open('222.txt', 'a')
# # print(file4.read())
# file4.write('hello\n')
# file4.write('hello\n')
# file4.write('hello\n')
# file4.write('Hi')
# # print(file4.read())

file5 = open('../../HWs/Context_Manager/222.txt', 'r+')
# file5.write('555hello\n')
# file5.write('555hello\n')
# file5.write('555hi\n')
file5.write('999hi\n')
file5.read()

file5.close()

f = open("../../HWs/Context_Manager/test.txt", "w")
f.write("test.txt\n")
f.write("HELLO!\n")
f.write("world!\n")
f.write("bye world!")

ff = open("../../HWs/Context_Manager/test1.txt", "w")
lines = ["Line1", "Line2", "Line3"]
contents = "\n".join(lines)
ff.write(contents)

fff = open("../../HWs/Context_Manager/test_append.txt", "a")
fff.write("Hello\n")

t = open("../../HWs/Context_Manager/test_write.txt", "w")
t.write("Kine2\n")
t.write("Kine1")

# with open("test1.txt") as qqq, open("test1_copy.txt", "r+") as www:
#     for line in qqq:
#         www.write(line)


f.close()
