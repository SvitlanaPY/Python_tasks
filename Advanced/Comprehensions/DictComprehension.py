a = {word: len(word) for word in ['hello', 'hi', 'bye']}
print("dict 'a': ", a)
# dict 'a':  {'hello': 5, 'hi': 2, 'bye': 3}

aa = {}
for word in ['hello', 'hi', 'bye']:
    aa[word] = len(word)
print("dict 'aa': ", aa)
# dict 'aa':  {'hello': 5, 'hi': 2, 'bye': 3}


# забрати зі слів всі великі букви окрім перших, перевести строку з цифр у integer
data = {'Джеф БеЗос': '177',
        'Ілон Маск': '126',
        'БерНар АрнО': '150',
        'БілЛ ГеЙтС': '124'}
new_data = {key.title(): int(val) for key,val in data.items()}
print("dict 'new_data': ", new_data)
# dict 'new_data':  {'Джеф Безос': 177, 'Ілон Маск': 126, 'Бернар Арно': 150, 'Білл Гейтс': 124}

new_data2 = {}
for key, val in data.items():
    new_data2[key.title()] = int(val)
print("dict 'new_data2': ", new_data2)
# dict 'new_data2':  {'Джеф Безос': 177, 'Ілон Маск': 126, 'Бернар Арно': 150, 'Білл Гейтс': 124}


# робимо словник юзерів, де ключами будуть id, а значеннями - список із імені користувача та пароля
users = [
    [10, 'Bob', 'password'],
    [11, "Tom", "python"],
    [12, "John", "overflow"],
    [13, "Stas", "pwd312"],
    [151, "Andrew", "qwerty123"]
]
new_users = {user[0]: user[1:] for user in users}
print("dict 'new_users': ", new_users)
# dict 'new_users':  {10: ['Bob', 'password'], 11: ['Tom', 'python'], 12: ['John', 'overflow'], 13: ['Stas', 'pwd312'], 151: ['Andrew', 'qwerty123']}


people = [
    ['Amy Smith', '694.322.8133x22426'],
    ['Brian Shaw', '593.662.5217x338'],
    ['Christian Sharp', '118.197.8810'],
    ['Sean Schmidt', '9722527521'],
    ['Thomas Long', '163.814.9938'],
    ['Joshua Willis', '+1-978-530-6971x601']
]
phone_book = {person[1]: person[0] for person in people}
print("dict 'phone_book': ", phone_book)   #  в качестве ключей хранится номера телефонов, а значениями есть имена владельцев

