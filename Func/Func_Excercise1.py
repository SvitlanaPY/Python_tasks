if 5 > 1:  # умова виконується
    def pryklad():
        print('hello')
else:
    def pryklad():
        print('HELLO')

pryklad()   # hello


if 5 > 7:   # умова НЕ виконується
    def pryklad():
        print('hello')
else:
    def pryklad():
        print('HELLO')

pryklad()   # HELLO



def primer():
        print('hello')

def primer():
        print('HELLO')

primer()
# оскільки наша програма виконується зверху вниз, то спершу виконається перша ф-ія primer(),
# але потім наша ф-ія primer() перезатирається і тому ми побачимо лише результат виконання другої ф-ії primer()
# - тобто, роздрукується слово HELLO
