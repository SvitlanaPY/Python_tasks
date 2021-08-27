def ss():
    # local
    print(w)   # UnboundLocalError: local variable 'w' referenced before assignment
    a, b, c = 1,2,3
    w = 'HELLO'
    print(a, b, c, w)   # 1 2 3 HELLO

# global
w = 'hello'

ss()
print(w)   # hello


# але якщо ми закоментуємо стрічку №20: w = 'HELLO', тоді вже стрічка №18 не буде викликати UnboundLocalError
def ss():
    # local
    print(w)   # роздрукується hello; а UnboundLocalError: ... вже не буде
    a, b, c = 1,2,3
    # w = 'HELLO'
    print(a, b, c, w)   # 1 2 3 hello

# global
w = 'hello'

ss()
print(w)   # hello