"""
Щоб створити захищений атрибут, перед іменем атрибуту потрібно додати одне нижнє підкреслення
"""
class BankAccount2:

    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport

    def print_protected_data(self):
        print(self._name, self._balance, self._passport)


account2 = BankAccount2('Ted', 200000, 5555555555)
account2.print_protected_data()  # 'Ted' 200000 5555555555

""" 
доступ до захищених атрибутів класу ззовні (outdoor access) зберігся і захищені/protected змінні не вирішують проблеми захисту даних.
Але це ознака/вказівка того, що атрибут НЕ варто використовувати/доступатись ззовні класу
"""
print(account2._name)       # 'Ted'
print(account2._balance)    # 200000
print(account2._passport)   # 555555555

"""
# для чого тоді такі змінні...?
# в пайтоні принято ставити нижнє підкреслення і так позначати/вказувати, що даний атрибут захищений, 
і не варто до нього доступатись/використовувати ззовні класу 
# на рівні узгодження між розробниками
"""
