# метод write() - перезатре вміст файлу новим текстом
file = open("111_write().txt", 'w')
file.write("hello")
file.write("hello\n")
file.write("hello")
# hellohello
# hello

file_ = open("111_write().txt", 'a')
file.write("\nhi")
# hellohello
# hello
# hi


file2 = open("333_write()_append().txt", "a+")
file2.write("\nhi")
file2.read()


file.close()
file_.close()
file2.close()
