person = {'lastName': 'Ivanov', 'firstName': 'Ivan', 'city': 'Samara', 'University': 'SGU', 'marks': [5, 4, 3, 5, 5, 4, 3, 5]}
d = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}

print("Довжина словника person: ", len(person))
# Довжина словника person:  5

print('University' in person)
# True
print(5 in d)
# False

print("d before creating d[5]: ", d)
# d before creating d[5]:  {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
if not 5 in d:
    d[5] = 'five'
else:
    print(d[5])
print("d after creating d[5]: ", d)
# d after creating d[5]:  {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}


for key in person:
    print(key, '-', person[key])
# lastName - Ivanov
# firstName - Ivan
# city - Samara
# University - SGU
# marks - [5, 4, 3, 5, 5, 4, 3, 5]



d = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
print("d before del:  ", d)
# d before del:   {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
del d[1]
print("d after del (1:'one') -   ", d)
# d after del (1:'one') -    {2: 'two', 3: 'three', 4: 'four'}
