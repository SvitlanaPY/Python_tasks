# Задача «Номер появления слова»
# В единственной строке записан текст.
# Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# INPUTS:
# one two one tho three two one three one two

text = input().split()
d = {}
for word in text:
    d[word] = d.get(word, 0) + 1  # або розписати в два рядки 5-6:
    # d[word] = d.get(word, 0)
    # d[word] += 1
    print(d[word] - 1, end=' ')


# №2:
# text = input().split()
# d = dict()
# for elem in text:
#     if elem in d:
#         d[elem] += 1
#     else:
#         d[elem] = 0
#     print(d[elem], end=' ')


# №3:
# d = {}
# text = input().split()
# for word in text:
#     key = word
#     val = d.get(word)
#     d[key] = val
#     if val == None:
#         d[key] = 0
#         print(d[key], end=' ')
#     else:
#         d[key] = d[key] + 1
#         print(d[key], end=' ')
