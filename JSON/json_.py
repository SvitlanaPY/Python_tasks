import json

student1 = {
    "first_name": "Oleg",
    "last_name": "Dean",
    "scores": [70, 80, 90],   # sum = 240
    "description": "Good job, Greg",
    "certificate": True
}
student2 = {
    "first_name": "Wirl",
    "last_name": "Wood",
    "scores": [60, 80, 80],   # sum = 220
    "description": "Nicely Done",
    "certificate": True
}
# data = [student1, student2]
# print(json.dumps(data, indent=4))  # конвертуємо наш python-об"єкт data(який є list-ом) у json-формат

data = [student1, student2]
data_json = json.dumps(data, indent=4)   # конвертуємо наш python-об"єкт data(який є list-ом) у json-формат і записуємо в змінну data_json
print(data_json)

data_new = json.loads(data_json)    # конвертуємо нашу строку json-формату в python-об"єкт (data_new буде таке ж як і data)
# data_new = data = [student1, student2]
print(sum(data_new[0]["scores"]))
# data_new[0] - доступ до першого елемента списку "data_new", яким є student1, і який є одночасно і словником, а ["scores"] - доступ до значень словника student1 по його ключу ["scores"]

with open("students.json", "w") as file:   # записуємо наш python-об"єкт data(який є list-ом, у json-форматі) в файл з назвою "students.json"
    json.dump(data, file, indent=4)

with open("students.json") as ff:
    file_content = ff.read()
    data_again = json.loads(file_content)
    print(sum(data[1]["scores"]))

# with open("students.json", "r") as ff:   # зчитуємо з файлу дані формату json як python-об"єкт: data_again = data = [student1, student2]
#     data_again = json.load(ff)
#     print(sum(data_again[1]["scores"]))   # 220
