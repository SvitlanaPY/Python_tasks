import re
# re = regular expressions

print(re.match)    # - бере наш шаблон і нашо строку і перевіряє, чи підходить дана строка під даний шаблон
print(re.search)   # - бере нашу строку і знаходить першу підстроку, яка підходить під наш шаблон
print(re.findall)  # - буде знаходити всі підстроки нашої строки, які підходять під даний шаблон
print(re.sub)      # - дозволить нам замінити всі входження підстрок, які підходять під наш шаблон чимось іншим

pattern = r"abc"
string_ = "abc"
match_object = re.match(pattern, string_)
print(match_object)   # <re.Match object; span=(0, 3), match='abc'>

pattern = r"abc"
string_2 = "babc"
match_object = re.match(pattern, string_2)
print(match_object)   # None


pattern = r"abc"
string_3 = "abcdef"
match_object = re.match(pattern, string_3)
print(match_object)   # <re.Match object; span=(0, 3), match='abc'>


pattern = r"abc"
string_4 = "bbbabc"
match_object = re.search(pattern, string_4)
print(match_object)   # <re.Match object; span=(3, 6), match='abc'>


# [] - можна вказати множину підходящих символів
pattern2 = r"a[abcd]c"
string_4 = "aac"   # abc, acc, adc - всі ці строки будуть підходити під наш шаблон
match_object = re.match(pattern2, string_4)
print(match_object)

pattern3 = r"a[abcd]c"
string_5 = "aac, abc, acc, adc, aaa, bbb"
all_inclusions = re.findall(pattern3, string_5)
print("all_inclusions:", all_inclusions)   # ['aac', 'abc', 'acc', 'adc']

fixed_typos = re.sub(pattern3, "abc", string_5)
print("fixed_typos:", fixed_typos)   # abc, abc, abc, abc, aaa, bbb

x1 = "hello\"world"
print(x1)   # hello"world
x2 = r"hello\"world"
print(x2)   # "hello\"world"
