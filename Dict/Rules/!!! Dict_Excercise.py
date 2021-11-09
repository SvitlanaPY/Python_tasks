person = {}
str_ = "Ivanov Ivan Samara SGU 5 4 3 5 5 4 3 5"
str_ = str_.split(' ')
print("str_: ", str_)
# str_:  ['Ivanov', 'Ivan', 'Samara', 'SGU', '5', '4', '3', '5', '5', '4', '3', '5']
person['lastName'] = str_[0]
person['firstName'] = str_[1]
person['city'] = str_[2]
person['University'] = str_[3]
person['marks'] = []
# person['marks'] = set()
print(person)
# person = {'lastName': 'Ivanov', 'firstName': 'Ivan', 'city': 'Samara', 'University': 'SGU', 'marks': []}
for i in str_[4:]:
    person['marks'].append(int(i))
    # person['marks'].add(int(i))
print(person)
# person = {'lastName': 'Ivanov', 'firstName': 'Ivan', 'city': 'Samara', 'University': 'SGU', 'marks': [5, 4, 3, 5, 5, 4, 3, 5]}
