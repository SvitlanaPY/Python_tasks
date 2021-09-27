def decor(func_):
    def wrap(n):
        result = func_(n)
        new_list = [str(el) for el in result]
        return new_list
    return wrap
# return wrap а не return wrap(), бо написавши дужки ми одразу викличемо ф-ію wrap,
# а return wrap повертає посилання на wrap без її виклику
def func(n):
    return [i for i in range(n)]

wrap_ = decor(func)   # ідемо в decor, передаємо ф-ію func;
# у ф-ії decor в нас нічого не викликалось, ф-ія wrap() у ф-ії decor була лише оголошена;
# і цей decor повернув лише посилання на wrap(), таким чином зробивши замикання.
# результат виклику decor() записуємо у змінну wrap_; змінна wrap_ тепер містить посилання на ф-ію wrap()
# тепер ззовні ми маємо посилання на ф-ію wrap(), яка всередині щось виконує
# і ця ф-ія wrap() буде знати про ф-ію func().
# print(wrap_)      # <function decor.<locals>.wrap at 0x7f7395ce4160>
# тепер ми можемо викликати нашу внутрішню ф-ію def wrap(),
# передаючи їй параметр(и)/аргумент(и), які ми хочемо передати у ф-ію def func(n)
# і вже всередині wrap() викликати ф-ію func(n), отримали результат, який повернула ф-ія,
# попрацювали з цим результатом (обробили його, допрацювали) і повернули результат всього назовні
res = wrap_(10)
print(res)
# ф-ію wrap_(10) можемо викликати лише завдяки тому, що decor(func) повернув посилання на неї
# передаємо функцію у декоратор, аргументи ф-ії передаємо у врапер-ф-ію і всередину їх з"єднуємо
# ОТЖЕ:
# декор отримав ф-ію (def decor(func_)),
# повернув посилання на wrap();
# wrap() отримав аргументи(які приймає ф-ія), з"єднав ф-ію з аргументами,
# попрацював з результатом виконання цієї ф-ії, і повернув те, що він доповнив.



def decor4(ffunc_):
    def inner():
        nn = int(input('Enter some number: '))
        list_t = ffunc_(nn)
        print(list_t)
        new_list = [str(elem) for elem in list_t]
        return new_list
    return inner

@decor4
def ffunc(n):   # ffunc: <function decor4.<locals>.inner at 0x7f5f02e9b1f0>
    return list(range(n + 1))

print(ffunc())     # викликаючи ffunc(), ми насправді викликаємо ф-ію inner(),
# а вже всередині inner() ми викликаємо дійсно ф-ію ffunc()

# # @decor4 над функцією ffunc() можна розписати наступним чином:
# inner_ = decor4(ffunc)
# result = inner_()
# print(result)

# @decor4 над ф-ією ffunc - це те саме, що і запис ffunc = decor4(ffunc);
# тобто ми ф-ію ffunc підміняємо на ф-ію inner, бо decor4(ffunc)/@decor4 повертає нам посилання на ф-ію inner;
# ffunc: <function decor4.<locals>.inner at 0x7f5f02e9b1f0>
