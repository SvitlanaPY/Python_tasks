# Напишите функцию check_password, которая проверяет переданный ей пароль на сложность
# и печатает на экран результат проверки.
# Сложным паролем будет считаться комбинация символов, в которой :
# Есть хотя бы 3 цифры
# Есть хотя бы одна заглавная буква
# Есть хотя бы один символ из следующего набора "!@#$%*"
# Общая длина не менее 10 символов
# Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password",
# в противном случае - "Easy peasy".
# Вам необходимо написать только определение функции
#
# Sample Input 1:
# qwerty
# Sample Output 1:
# Easy peasy
#
# Sample Input 2:
# Qwerty1357!
# Sample Output 2:
# Perfect password

def check_password(password):
    symbols ="!@#$%*"
    is_symbol = 0
    is_digit = 0
    is_upper = 0
    for elem in password:
        if elem in symbols:
            is_symbol += 1
        if elem.isdigit():
            is_digit += 1
        if elem.isupper():
            is_upper += 1
    if is_symbol >= 1 and len(password) >= 10 and is_digit >= 3 and is_upper >= 1:
        print("Perfect password")
    else:
        print("Easy peasy")

check_password("Q!werty1357")
check_password("test1357")
