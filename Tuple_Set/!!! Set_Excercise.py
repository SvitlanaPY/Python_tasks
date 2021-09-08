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
    d[name].add(comments)
print(d)


# d = {}
# while True:
#     text = input()
#     if text == 'q':
#         break
#     name, comments = text.split(': ')
#     d[name] = d.get(name, [])
#     d[name].append(comments)
#     # above two rows can be replaced with the below one:
#     # d[name] = d.get(name, []) + [comments]
# print(d)
