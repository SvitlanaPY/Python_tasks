"""
Property - для читання і зміни захищених(private) атрибутів. Потрібні, щоб працювати з полями/атрибутами класу.
Декоратор Property дозволяє нам створити властивості/Property, які будуть виглядати як атрибути в класі.
При читанні цих атрибутів викликається метод getter, при записі нового атрибуту чи значення - метод setter,
при видаленні - deletter.
getter - метод, що дозволяє вичитати якісь дані,
setter - можуть порівнювати вхідні дані на коректність і викликати якийсь додаткоий метод
(при встановленні якоїсь картинки на екрані, додаткову перевірку віку...).

Ім"я getter-а та ім"я setter-а мають бути однакові і такими ж як ім"я property:
getter name == setter name == property name
Ф-ія setter як правило призначена для встановлення/запису нового значення атрибуту,
отже, в якості параметра вона повинна приймати аргумент (нове значення).

Доступ до проперті відбувається як до атрибуту об"єкту.
"""

class BankAcc:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance        # private атрибут

    def get_balance(self):       # GETTER
        return self.__balance

    def set_balance(self, value):     # SETTER
        if not isinstance(value, (int, float)):
            raise ValueError('Balance should be numeric')
        self.__balance = value

    def delete_balance(self):   # DELETTER
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)

    # balance - ім"я проперті
    # fget=get_balance, де get_balance - ф-ія getter
    # fset=set_balance, де set_balance - ф-ія setter
    # fdel=delete_balance, де delete_balance - ф-ія deletter


a = BankAcc('Ivan', 100)
b = BankAcc('Vasya', 100)
print(b.get_balance())   # get_balance() - call method get_balance
b.set_balance(400)
print(b.get_balance())
c = BankAcc('Tanya', 200)
# c.set_balance('hello')   # set_balance() - call method set_balance
print(c.get_balance())
x = property
print(x)   # <class 'property'>

d = BankAcc('Misha', 400)
print(d.balance)   # balance - it is a PROPERTY;  # call getter
d.balance = 700     # call setter
print(d.balance)    # 777
# add delete function/method
w = BankAcc('Misha', 400)
print(w.balance)
# del w.balance
# print(w.balance)     # call getter
# w.balance = 999      # call setter
# print(w.balance)
x = property()
print(x)  # <property object at 0x7fb0e9794770>


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
"""

class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, new_mail):
        if new_mail.count('@') == 1:
            index_ = new_mail.find('@')
            if '.' in new_mail[index_:]:
                self.__email = new_mail
            else:
                print('Ошибочная почта')
        else:
            print('Ошибочная почта')

    email = property(fget=get_email, fset=set_email)
    # email  - це ім"я property
    # <ім"я property> = property(fget=<метод гетер>, fset=<метод сеттер>, fdel=<метод делітер>)
    # fget - обов"язковий, fset i fdel - optional, якщо fset немає, тоді це read-only property.


k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)        # (call getter)
# prince@wait.you
k.email = [1, 2, 3]   # (call setter)
# Ошибочная почта
k.email = 'prince@still@.wait'   # (call setter)
# Ошибочная почта
k.email = 'prince@still.wait'    # (call setter)
print(k.email)        # (call getter)
# prince@still.wait
k.email = 'prince@stillwait'     # (call setter)
print(k.email)        # (call getter)


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


# ПРЕДСТАВЛЕННЯ property ЧЕРЕЗ ДЕКОРАТОР-property
print('\n########## 9 ##########')
# class Person:
#     """
#     Change the value of the age property of the person object
#     """
#     name = "John"
#     age = 36
#     country = "USA"

class Person:
    def __init__(self, name, country, years_old=0):
        self.name = name
        self.country = country
        self.__years_old = years_old

    @property
    def age(self):                # GETTER
        print('Get age')
        return self.__years_old

    @age.setter                   # SETTER
    def age(self, new_age):
        print('Set age')
        self.__years_old = new_age

# ім"я getter-а та ім"я setter-а мають бути однакові і такими ж як ім"я property (person.age = 25, тут age і є нашою property)
# !!!!! ім"я getter-а = ім"я setter-а = ім"я property-і)

person = Person('John', 'USA', 36)
print(person.age)    # тут age і є нашою property; (call getter)
# OUTPUT: 36
person.age = 25   # save value in property "age" (call setter)
print('new age=', person.age)    # (call getter)
# OUTPUT: new age= 25


# READ-ONLY PROPERTY
print('\n########## 11* ##########')
# class Celsius:
#     """
#     By using @property convert the celsius to fahrenheit
#     Hint: (temperature * 1.8) + 32)
#     """
#     def __init__(self, temperature=0):
#         self._temperature = temperature
#
#
# # create an object
# {obj} = ...
#
# print({obj}.temperature)

class Celsius:
    def __init__(self, temperature=0):
        self.__temperature = temperature

    @property       # getter
    def celsius_to_farenheit(self):
        return (self.__temperature * 1.8) + 32

temp = Celsius(35)
print('temp. in fahrenheit:', temp.celsius_to_farenheit)    # (call getter)
# celsius_to_farenheit  - ім"я property
# OUTPUT: temp. in fahrenheit: 95.0


print('\n########## 5* ##########')
# class Concert:
#     """
#     Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50
#     """

class Concert:

    max_visitors_num = 0

    def __init__(self, visitors_count = 0):
        self.__visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self.__visitors_count

    @visitors_count.setter
    def visitors_count(self, count):
        self.__visitors_count = count if count <= Concert.max_visitors_num else Concert.max_visitors_num

Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 10
print(concert.visitors_count)
# OUTPUT: 50
Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 10
print(concert.visitors_count)
# OUTPUT: 10
