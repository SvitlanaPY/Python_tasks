import datetime

date = datetime.datetime.now()

name = 'Svitlana'

with open("email_template.txt") as f:
    template = f.read()        # повернеться строка, а до строки можна застосовувати форматування
    # print(type(template))    # <class 'str'>
    mail = template.format(name, date)

print(mail)
