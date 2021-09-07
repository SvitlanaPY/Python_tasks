my_dict = {'Били': set(), 'Дили': set(), 'Вили': set()}
while True:
    text = input()
    if text == 'конец':
        break
    key, val = text.split(': ')
    my_dict[key].add(val)

for val in sorted(my_dict.values(), key=len, reverse=True):
    for key in my_dict:
        if my_dict[key] == val:
            print(f'Количество уникальных комментаторов у {key} - {len(val)}')