print("Ex1")
ff = open("test_lines.txt", "w")
lines = ["Line1", "Line2", "Line3"]
contents = "\n".join(lines)
print("contents: ", contents)
# contents:  Line1
# Line2
# Line3
print("repr contents: ", repr(contents))
# repr contents:  'Line1\nLine2\nLine3'
ff.write(contents)   # список lines записуємо у файл "test_lines.txt"
# ff.write(str(lines))
ff.close()
#
#
# with open("test_1.txt") as qqq, open("test_1_copy.txt", "w") as sss:
#     for line in qqq:
#         sss.write(line)
#
#
# print("Ex2")
# with open("txt1.txt") as file, open("txt1_copy.txt", "a+") as w:
#     list_ = file.read().splitlines()
#     # print(list_)
#     for i in list_:
#         w.write(i[::-1] + '\n')
#
#
# print("Ex3")
# with open("test2.txt") as b, open("test2_copy.txt", 'a+') as a:
#     content = b.read().splitlines()
#     for elem in content:
#         a.write(elem + '\n')
#
#
# print("Ex4")
# test_links = []
# with open("links_for_test") as f_:
#     test_links = f_.readlines()
# print("test_links: ", test_links)
# #  test_links:  ['https://stepik.org/lesson/236895/step/1\n', 'https://stepik.org/lesson/236896/step/1\n', 'https://stepik.org/lesson/236897/step/1\n', 'https://stepik.org/lesson/236898/step/1\n', 'https://stepik.org/lesson/236899/step/1\n', 'https://stepik.org/lesson/236903/step/1\n', 'https://stepik.org/lesson/236904/step/1\n', 'https://stepik.org/lesson/236905/step/1']
# test_links = [line.rstrip() for line in test_links]
#
#