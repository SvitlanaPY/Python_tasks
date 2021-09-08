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


def example():
    print(1)
    print(2)
    return 'hello'
    print(3)
    print(4)
# весь код після return НЕ буде виконуватись;
# return працює як break в циклі: як тільки ми попадаємо на return, то відбувається вихід з функції
# і якщо у ф-ії є кілька return-ів, то виконається перший з них;
a = example()
print(a)
# 1
# 2
# hello