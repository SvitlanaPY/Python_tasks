"""
Дефиснутая фраза
Вводится два слова через пробел.
Ваша задача преобразовать данную фразу таким образом,
чтобы все буквы стали заглавными и между буквами в каждом слове появились дефисы

Sample Input 1:
Бросай курить
Sample Output 1:
Б-Р-О-С-А-Й К-У-Р-И-Т-Ь

Sample Input 2:
сИдИ дОмА
Sample Output 2:
С-И-Д-И Д-О-М-А
"""

a = input().upper().split()
aa = a[0]
aa = aa.replace('', '-')
bb = a[1]
bb = bb.replace('', '-')
print(aa[1:-1], bb[1:-1])

# №2:
# aa, bb = input().upper().split()
# aa = aa.replace('', '-')
# bb = bb.replace('', '-')
# print(aa[1:-1], bb[1:-1])

# №3:
# a = list(map(str, input().upper().split()))
# print('-'.join(a[0]), '-'.join(a[1]))
