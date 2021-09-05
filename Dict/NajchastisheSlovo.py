# Задача «Самое частое слово»
# Дан текст: в первой строке задано число строк, далее идут сами строки.
# Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
#
# Inputs1:
# 1
# apple orange banana banana orange
# Outputs1:
# banana
#
# Inputs2:
# 2
# taia ikm ikm ikm taia taia taia
# ikm ikm ikm
# Outputs2:
# ikm

n = int(input())
d = {}
for i in range(n):
    text = input().split()
    for word in text:
        d[word] = d.get(word, 0) + 1
maxx = max(d.values())
# print("Dict:  ", d)     # Dict:   {'apple': 1, 'orange': 2, 'banana': 2}
# print("maxx= ", maxx)   # maxx=  2
lst = []
for word, d[word] in d.items():
    if d[word] == maxx:
        lst.append(word)
lst.sort()
print(lst[0])    # = print(min(lst))


# или
#lst_new = sorted(lst)
#print(lst_new[0])
