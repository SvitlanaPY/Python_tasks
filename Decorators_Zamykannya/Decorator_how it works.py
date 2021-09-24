def decor(func_):
    def wrap(n):
        result = func_(n)
        new_list = [str(el) for el in result]
        return new_list
    return wrap

def func(n):
    return [i for i in range(n)]

wrap_ = decor(func)   # ідемо в decor, передаємо ф-ію func;
# у ф-ії decor в нас нічого не викликалось, ф-ія wrap() у ф-ії decor була лише оголошена;
# і цей decor повернув лише посилання на wrap(), таким чином зробивши замикання.
# результат виклику decor() записуємо у змінну wrap_; змінна wrap_ тепер містить посилання на ф-ію wrap()
# тепер ззовні ми маємо посилання на ф-ію wrap(), яка всередині щось виконує
# і ця ф-ія wrap() буде знати про ф-ію func().
print(wrap_)      # <function decor.<locals>.wrap at 0x7f7395ce4160>
# тепер ми можемо викликати нашу внутрішню ф-ію def wrap(),
# передаючи їй параметр такий як у головній ф-ії def func(n)
# і вже всередині wrap() викликати ф-ію func(n)
print(wrap_(10))


def decor4(ff_):
    def inner():
        nn = int(input('Enter some number: '))
        list_t = ff_(nn)
        print(list_t)
        new_list = [str(elem) for elem in list_t]
        return new_list
    return inner

@decor4    # це те саме, що і запис ff = decor4(ff);
# тобто ми ф-ію ff підміняємо на ф-ію inner, бо decor4(ff) поверне нам посилання на ф-ію inner
def ff(n):   # ff: <function decor4.<locals>.inner at 0x7f5f02e9b1f0>
    return list(range(n + 1))

print(ff())     # викликаючи ff, ми насправді викликаємо ф-ію inner(),
# а вже всередині inner() ми викликаємо дійсно ф-ію ff()
