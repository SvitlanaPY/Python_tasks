# r = row: якщо є r перед строкою (r"ab\ncd\nef"), це означає, що в строці НЕмає службових символів,
# які потрібно екранувати і строка виводиться так, як є (з усіма символами у ній)
w = r"ab\ncd\nef"
print("row-cтрока: ", w)   # row-cтрока:  ab\ncd\nef
print("Довжина row-cтроки: ", len(w))   # 10

# якщо перед строкою НЕмає r ("ab\ncd\nef"), а строка містить службові символи, то вони застосуються до строки:
t = "ab\ncd\nef"
print("НЕ row-cтрока1: ", t)   # НЕ row-cтрока1:  ab
# cd
# ef
print("Довжина НЕ row-cтроки1: ", len(t))   # Довжина НЕ row-cтроки1:  8

t2 = "abc\tdef"
print("НЕ row-cтрока2: ", t2)   # НЕ row-cтрока2:  abc	def
print("Довжина НЕ row-cтроки2: ", len(t2))    # Довжина НЕ row-cтроки2:  7

print("======================== ONE MORE EXAMPLE ===========================")
a = r"ab\ncd\nef"
print(a)   # ab\ncd\nef
aa = "ab\ncd\nef"
print(aa)
# ab
# cd
# ef


print("---------------------------")
s = """hello
world
bye
see you!"""
print(s)
# hello
# world
# bye
# see you
print(repr(s))   # 'hello\nworld\nbye\nsee you!'


path1 = r"D:\Application\McAfee\Packages\default"
print("path1: ", path1)   # D:\Application\McAfee\Packages\default
print(repr(path1))   # 'D:\\Application\\McAfee\\Packages\\default'

path2 = "D:\Application\McAfee\Packages\default"
print("path2: ", path2)   # D:\Application\McAfee\Packages\default
print(repr(path2))   # 'D:\\Application\\McAfee\\Packages\\default'

path3 = r"D:\\Application\\McAfee\\Packages\\default"
print("path3:", path3)
print(repr(path3))

path4 = "D:\\Application\\McAfee\\Packages\\default"
print("path4:", path4)   # D:\Application\McAfee\Packages\default
print(repr(path4))   # 'D:\\Application\\McAfee\\Packages\\default'

# >>> r"D:\Application\McAfee\Packages\default"
# 'D:\\Application\\McAfee\\Packages\\default'
# >>> "D:\Application\McAfee\Packages\default"
# 'D:\\Application\\McAfee\\Packages\\default'
# >>> r"D:\\Application\\McAfee\\Packages\\default"
# 'D:\\\\Application\\\\McAfee\\\\Packages\\\\default'
# >>> "D:\\Application\\McAfee\\Packages\\default"
# 'D:\\Application\\McAfee\\Packages\\default'
