"""
Создайте класс UserMail, у которого есть:

конструктор __init__, принимающий 2 аргумента: логин и почтовый адрес.
Их необходимо сохранить в экземпляр как атрибуты login и __email (обратите внимание, защищенный атрибут)
метод геттер get_email, которое возвращает защищенный атрибут __email ;
метод сеттер set_email, которое принимает в виде строки новую почту.
Метод должен проверять, что в новой почте есть только один символ @ и после нее есть точка.
Если данные условия выполняются, новая почта сохраняется в атрибут __email,
в противном случае выведите сообщение "Ошибочная почта";
создайте свойство email, у которого геттером будет метод get_email, а сеттером - метод set_email

k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3] # Ошибочная почта
k.email = 'prince@still@.wait'  # Ошибочная почта
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait
"""


class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):       # GETTER
        return self.__email

    def set_email(self, new_mail):        # SETTER
        if new_mail.count('@') == 1:
            index_ = new_mail.find('@')
            if '.' in new_mail[index_:]:
                self.__email = new_mail
            else:
                print('Ошибочная почта')
        else:
            print('Ошибочная почта')

    email = property(fget=get_email, fset=set_email)
    # email  - це ім"я PROPERTY
    # <ім"я property> = property(fget=<метод гетер>, fset=<метод сеттер>, fdel=<метод делітер>)
    # fget - обов"язковий, fset i fdel - optional, якщо fset немає, тоді це read-only property.

k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)
# prince@wait.you
k.email = [1, 2, 3]
# Ошибочная почта
k.email = 'prince@still@.wait'
# Ошибочная почта
k.email = 'prince@still.wait'
print(k.email)
# prince@still.wait
k.email = 'prince@stillwait'
print(k.email)


print('----- ДЕКОРАТОР  PROPERTY -----')
class UserMailPropertyDecor:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    @property
    def e_mail(self):
        return self.__email

    @e_mail.setter
    def e_mail(self, new_mail):
        if new_mail.count('@') == 1:
            index_ = new_mail.find('@')
            if '.' in new_mail[index_:]:
                self.__email = new_mail
            else:
                print('Ошибочная почта')
        else:
            print('Ошибочная почта')


k_ = UserMailPropertyDecor('belosnezhka', 'prince@wait.you')
print(k_.e_mail)
# prince@wait.you
k_.e_mail = [1, 2, 3]
# Ошибочная почта
k_.e_mail = 'prince@still@.wait'
# Ошибочная почта
k_.e_mail = 'prince@still.wait'
print(k_.e_mail)
# prince@still.wait
k_.e_mail = 'prince@stillwait'
print(k_.e_mail)


