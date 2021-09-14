# with open("test1.txt") as qqq, open("test1_copy.txt", "w") as sss:
#     for line in qqq:
#         sss.write(line)

# ff = open("test1.txt", "w")
# lines = ["Line1", "Line2", "Line3"]
# contents = "\n".join(lines)
# ff.write(contents)


with open("../../HWs/Context_Manager/txt1.txt") as aaa, open("txt1_copy.txt", "w") as sss:
    print(aaa.read().splitlines())
    l = line[::-1]
    sss.write(line[::-1])
    for line in aaa:
        sss.write(line[::-1])
    # for i in aaa:
    # s = y.reverse()
    # print(y)
    # print(s)




# open("txt2.txt") as bbb:
#     content = aaa.read().splitlines()
    # for line in aaa:
    #     bbb.write(content)

