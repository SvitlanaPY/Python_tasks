# Задача «Самое частое слово»
# Дан текст: в первой строке задано число строк, далее идут сами строки.
# Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
# Inputs1:
# 1
# apple orange banana banana orange
# Outputs1:
# banana

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
lst = []
for word, d[word] in d.items():
    if d[word] == maxx:
        lst.append(word)
lst.sort()
print(lst[0])
# или
#lst_new = sorted(lst)
#print(lst_new[0])
# или
# print(min(lst))


# print(d.keys())   # dict_keys(['orange','banana','apple'])
# print(sorted(d.keys()))  # ['apple', 'banana', 'orange']

# maxx = max(d.values())  # search for max value in dict: maxx = 2
# print(maxx)
# for word in sorted(d.keys()):   # sorting by keys: ['apple', 'banana', 'orange']
#     if d[word] == maxx:
#         print(word)
#         break
