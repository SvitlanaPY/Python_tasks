"""
ENCAPSULATION/ ІНКАПСУЛЯЦІЯ - підхід/механізм/принцип, що полягає у обмеженні прямого доступу до даних
(полів, проперті, методів, атрибутів...)
тобто дозволяє захищати наші дані від зовнішніх втручань.
"""
class BankAccount1:

    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    def print_public_data(self):
        print(self.name, self.balance, self.passport)


account1 = BankAccount1('Bob', 100000, 4567896541)
account1.print_public_data()   # 'Bob' 100000 4567896541
# outdoor access: доступаємось ззовні до методу print_public_data (до даних наших клієнтів)
# всі ці атрибути публічні: доступні всередині нашого класу і також доступні поза/ззовні класу
print(account1.name)      # 'Bob'
print(account1.balance)   # 100000
print(account1.passport)  # 4567896541
