
person = {'lastName': 'Ivanov', 'firstName': 'Ivan', 'city': 'Samara', 'University': 'SGU', 'marks': [5, 4, 3, 5, 5, 4, 3, 5]}
q = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

# .clear()
print("q before clear(): ", q)
# q before clear():  {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
q.clear()
print("q after clear(): ", q)   # q after clear():  {}

# .get()   - повертає значення по ключу, якщо ключ є; якщо ключа немає - поверне None, або передане значення
print("\n.GET() method:")
q = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
print(q.get(5))    # поверне five по ключу 5
print(q.get(5, 'New five'))
print(q.get(6))    # поверне None по замовчуванню, оск ключа 6 в словнику немає
print(q.get(7, "No such key"))   # поверне передане значення No such key по ключу 7, якого в словнику немає


print("\n.SETDEFAULT() method:")
# .setdefault()   - не лише поверне значення по ключу, але і може створити нову пару ключ-значення
# створює ключ, якщо його немає в словнику, якщо є - повертає значення по ключу
print("q before setdefault(): ", q)
# q before setdefault():  {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
q.setdefault(6, "New key")    # створить пару -  6: 'New key'
q.setdefault(7)   # створить пару -  7: None
print("q after setdefault(): ", q)
# q after setdefault():  {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'New key', 7: None}


print("\n.POP() method:")
# методу .pop() потрібно передати значення ключа; метод видаляє пару по заданому ключу;
# якщо ключа неіснує, то буде KeyError; а TypeError - виникає, якщо викликати метод .рор() без параметра
print("q before pop(): ", q)
# q before pop():  {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'New key', 7: None}
pop_ = q.pop(6)   # поверне значення New key по ключу 6 і запише в змінну pop_, але саме значення видалить зі словника
print("pop_ = ", pop_)   # pop_ =  New key
print("q after .pop(6): ", q)
# q after .pop(7):  {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 7: None}


print("\n.POPitem() method:")
# не приймає параметрів і видаляє випадкові значення зі словника, пвертаючи саму пару
# popitem_ = q.popitem()
# print("popitem_ = ", popitem_)   # popitem_ =  (7, None)
# popitem_ = q.popitem()
# print("popitem_ = ", popitem_)    # popitem_ =  (5, 'five')


print("\n.keys() method:")
# повертає колекцію всіх ключів словника
print(q.keys())
# dict_keys([1, 2, 3, 4, 5, 7])


print("\n.values() method:")
# повертає колекцію значень
print(person.values())
# dict_values(['Ivanov', 'Ivan', 'Samara', 'SGU', [5, 4, 3, 5, 5, 4, 3, 5]])


print("\n.items() method:")
# повертає колекцію, в якій містяться всі пари словника
print(q.items())
# dict_items([(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'), (7, None)])


print("\nВикористання методів: .keys()/.values()/.items()")
for key in person.keys():
    print(key)
# lastName
# firstName
# city
# University
# marks

print()
for val in person.values():
    print(val)
# Ivanov
# Ivan
# Samara
# SGU
# [5, 4, 3, 5, 5, 4, 3, 5]

print()
for key in person.keys():
    print(key, person[key])
# lastName Ivanov
# firstName Ivan
# city Samara
# University SGU
# marks [5, 4, 3, 5, 5, 4, 3, 5]

print()
for key, val in person.items():
    print(key)
    print(val)
# lastName
# Ivanov
# firstName
# Ivan
# city
# Samara
# University
# SGU
# marks
# [5, 4, 3, 5, 5, 4, 3, 5]

print()
for para in person.items():
    print(para)
# ('lastName', 'Ivanov')
# ('firstName', 'Ivan')
# ('city', 'Samara')
# ('University', 'SGU')
# ('marks', [5, 4, 3, 5, 5, 4, 3, 5])

print()
for para in person.items():
    print(para[0], '-', para[1])
print(person.items())
