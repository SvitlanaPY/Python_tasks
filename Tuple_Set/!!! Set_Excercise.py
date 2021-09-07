# dict_ = {'Bill': set()}
# while True:
#     text = input()
#     if text == 'q':
#         break
#     name, comments = text.split(': ')
#     dict_[name].add(comments)


d = {}
while True:
    text = input()
    if text == 'q':
        break
    name, comments = text.split(': ')
    d[name] = d.get(name, set())
    print(d)
    print(d[name])
    d[name].add(comments)
    print(d)
print(d)
