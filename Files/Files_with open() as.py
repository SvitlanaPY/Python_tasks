print("Ex1")
ff = open("test_lines.txt", "w")
lines = ["Line1", "Line2", "Line3"]
contents = "\n".join(lines)
ff.write(contents)
# ff.write(str(lines))
ff.close()
#
# with open("test_1.txt") as qqq, open("test_1_copy.txt", "w") as sss:
#     for line in qqq:
#         sss.write(line)


# print("Ex2")
# with open("txt1.txt") as file, open("txt1_copy.txt", "a+") as w:
#     list_ = file.read().splitlines()
#     # print(list_)
#     for i in list_:
#         w.write(i[::-1] + '\n')


# print("Ex3")
# with open("test2.txt") as b, open("test2_copy.txt", 'a+') as a:
#     content = b.read().splitlines()
#     for elem in content:
#         a.write(elem + '\n')
