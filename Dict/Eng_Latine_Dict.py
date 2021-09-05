# Задача «Англо-латинский словарь»
# Однажды, разбирая старые книги на чердаке, школьник Вася нашёл англо-латинский словарь.
# Английский он к тому времени знал в совершенстве, и его мечтой было изучить латынь.
# Поэтому попавшийся словарь был как раз кстати.
#
# К сожалению, для полноценного изучения языка недостаточно только одного словаря:
# кроме англо-латинского необходим латинско-английский.
# За неимением лучшего он решил сделать второй словарь из первого.
#
# Как известно, словарь состоит из переводимых слов, к каждому из которых приводится несколько слов-переводов.
# Для каждого латинского слова, встречающегося где-либо в словаре, Вася предлагает найти все его переводы
# (то есть все английские слова, для которых наше латинское встречалось в его списке переводов),
# и считать их и только их переводами этого латинского слова.
#
# Помогите Васе выполнить работу по созданию латинско-английского словаря из англо-латинского.
#
# В первой строке содержится единственное целое число N — количество английских слов в словаре.
# Далее следует N описаний. Каждое описание содержится в отдельной строке,
# в которой записано сначала английское слово, затем отделённый пробелами дефис,
# затем разделённые запятыми с пробелами переводы этого английского слова на латинский.
# Все слова состоят только из маленьких латинских букв.
# Переводы отсортированы в лексикографическом порядке.
# Порядок следования английских слов в словаре также лексикографический.
# Выведите соответствующий данному латинско-английский словарь, в точности соблюдая формат входных данных.
# В частности, первым должен идти перевод лексикографически минимального латинского слова,
# далее — второго в этом порядке и т.д.
# Внутри перевода английские слова должны быть также отсортированы лексикографически.

# Inputs1:
# 3
# apple - malum, pomum, popula
# fruit - baca, bacca, popum
# punishment - malum, multa
# Outputs1:
# 7
# baca - fruit
# bacca - fruit
# malum - punishment, apple
# multa - punishment
# pomum - apple
# popula - apple
# popum - fruit

n = int(input())
eng_lat = {}
lat_eng = {}
text = ''
for i in range(n):
    text = input().split(' - ')
    text = [text[0]] + text[1].split(', ')
    eng_lat[text[0]] = eng_lat.get(text[0], []) + text[1:]
for key, val in eng_lat.items():
    for word in val:
        lat_eng[word] = lat_eng.get(word, []) + [key]
print(len(lat_eng))
for key, val in sorted(lat_eng.items()):
    print(key, '-', (', ').join(val))


# РОЗБІР:
# n = int(input())
# eng_lat = {}
# lat_eng = {}
# text = ''
# for i in range(n):
#     text = input().split(' - ')
#     # text = ['apple', 'malum, pomum, popula']
#     # text[0] = 'apple';  text[1] = 'malum, pomum, popula's
#     text = [text[0]] + text[1].split(', ')
#     # text = ['apple', 'malum', 'pomum', 'popula']
# #    key = text[0]
#     eng_lat[text[0]] = eng_lat.get(text[0], []) + text[1:]
# # eng_lat dict:  {'apple': ['malum', 'pomum', 'popula'], 'fruit': ['baca', 'bacca', 'popum'], 'punishment': ['malum', 'multa']}
#
# for key, val in eng_lat.items():
#     # key: 'apple';  val: ['malum', 'pomum', 'popula']
#     for word in val:
#         # word: 'malum'
# #        key2 = word
#         lat_eng[word] = lat_eng.get(word, []) + [key]
# # lat_eng dict: {'malum': ['apple', 'punishment'], 'pomum': ['apple'], 'popula': ['apple'], 'baca': ['fruit'], 'bacca': ['fruit'], 'popum': ['fruit'], 'multa': ['punishment']}
#
# for key, val in sorted(lat_eng.items()):
#     print(key, '-', (', ').join(val))
