# описовий блок програми (описуються функції, класи, процедури ...)
# описовий блок сам по собі не виконується, він мусить бути викликаний,
# і виклик функцій/процедур/класів відбувається в основному коді даної програми чи в ін модулі,
# який імпортує даний модуль

def sum(a, b):
    return a + b


# все нижче (що іде після описово блоку) є основним кодом програми
print("Modele code")
print(__name__)
print("Sum from main code in Module: ", sum(1, 2))

if __name__ == "__main__":
    print("It is a module")
    print("Call inside module. Sum=", sum(4, 6))


# якщо даний файл буде запускатись самостійно, чи з консолі, чи при імпорті його в ін. файл як модуль,
# то буде виконуватись/запускатись основний код програми

# щоб уникнути виконання основного коду програми, ми цей основний код загортаємо у конструкцію
# if __name__ == "__main__":
# (і при імпорті даного файла як модуля, його код,
# який лежить в конструкції "if __name__ == "__main__": ... " НЕ буде запускатись)
