s = """Hello
world
hi
bye
"""
print("S:", s)
# кожне слово строки s виведеться в окремому рядку
print("REPR(S):", repr(s))   # 'Hello\nworld\nhi\nbye\n'

a = 'abc\ndef'
print("A:", a)
# A: abc
# def
# abc i def виведуться в окремих рядках
print("repr(a)", repr(a))
aa = r'abc\ndef'
print("AA:", aa)
# AA: abc\ndef
print("repr(aa)", repr(aa))   # 'abc\\ndef'


b = 'abc\tdef'
print("B:", b)   # \t  means tabulation:   B: abc	def
print(repr(b))   # 'abc\tdef'

c = 'abc\nre\tgfd\ngfd'
print('c=', c)
# c= abc
# re	gfd
# gfd

cc = r'abc\nre\tgfd\ngfd'
print('cc=', cc)   # cc= abc\nre\tgfd\ngfd
# літера r перед строкою вказує Python-у, щоб всі службові символи в строці НЕ екранувались,
# а лишались символами і так і друкувались
