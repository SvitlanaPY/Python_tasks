import json
from datetime import datetime
from random import randint

str_json = """
{
"response": {
    "count": 5961777,
    "users": [{
        "userId": "krish",
        "jobTitle": "Developer",
        "firstName": "КРІШ",
        "lastName": "Lee",
        "employeeCode": "E1",
        "region": "CA",
        "phoneNumber": "123456",
        "emailAddress": "krish.lee@learningcontainer.com"
    }, {
        "userId": "devid",
        "jobTitle": "Developer",
        "firstName": "Devid",
        "lastName": "Rome",
        "employeeCode": "E2",
        "region": "CA",
        "phoneNumber": "1111111",
        "emailAddress": "devid.rome@learningcontainer.com"
    }, {
        "userId": "tin",
        "jobTitle": "Program Manager",
        "firstName": "tin",
        "lastName": "jonson",
        "employeeCode": "E3",
        "region": "CA",
        "phoneNumber": "2222222",
        "emailAddress": "tin.jonson@learningcontainer.com"
    } ]
}
}
"""
###   L O A D S   ###
print("str_json:", str_json)   # строка 'str_json' у форматі json
print("type 'str_json'=", type(str_json))   # <class 'str'>

data = json.loads(str_json)   # зчитує строку 'str_json' у форматі .json і конвертує у python-об"єкт data (у нашому випадку це буде <class 'dict'>)
print("type 'data'=", type(data))   # <class 'dict'>

print('Словник data =', data)
print('----------------------------')
print()


#####   ПРАЦЮЄМО ТЕПЕР З 'data' - ЯКИЙ Є СЛОВНИКОМ в python і редагуємо його   #####
print('del employeeCode and add likes and userAge:')
print('ALL USERS:', data['response']['users'])
for elem in data['response']['users']:
    print('___________________')
    print(elem['firstName'], elem['lastName'])
    del elem['employeeCode']
    print("Словник 'data' без 'employeeCode'=", data['response']['users'])
    elem['likes'] = randint(100, 300)
    print("Словник 'data' з 'LIKES'=", data['response']['users'])
    elem['userAge'] = randint(18, 65)
    print("Словник 'data' з 'userAge'=", data['response']['users'])
    elem['date_now'] = datetime.now().strftime('%d/%m/%y')
    print("Словник 'data' з 'date_now'=", data['response']['users'])
    elem['canAccess'] = True
    elem['Null_None'] = None

print('++++++++++++++++++++++++++++++++')
print('Словник data після редагування', data['response']['users'])
print()


###   D U M P S   ###
##### НАШ python-СЛОВНИК 'data', ЯКИЙ МИ ПОРЕДАГУВАЛИ ТРІШКИ, ПЕРЕВОДИМО У СТРОКУ 'new_json' ФОРМАТУ json
# тобто СТРОКА 'new_json' БУДЕ тепер МІСТИТИ ДАНІ ФОРМАТУ json
new_json = json.dumps(data, indent=2)    # створює строку формату .json
print("new_json after editing 'data'=", new_json)
print("type for 'new_json' = ", type(new_json))   # <class 'str'>


# переводимо строку формату json у python-об"єкт (dict)
new_json_again = json.loads(new_json)
print(type(new_json_again))   # <class 'dict'>



###   РОБОТА З ФАЙЛОМ, ЩО МІСТИТЬ json-ДАНІ   ###
# створюємо файл у форматі .json
#with open('my_json.json', 'w') as ffile:
#    json.dump(data, ffile, indent=3)

# відкриваємо/зчитуємо файл у форматі .json
#with open('my_json.json', 'r') as ffile:
#    data = json.load(ffile)
#print(data)
