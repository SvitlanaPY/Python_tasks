"""
Всередині try: - ми пишемо блок/код, який ми будемо обробляти, після блоку дій на рівні з try іде except,
після except вказується тип виключення, який ми хочемо обробити/відловити: except ValueError:
всередині except теж є блок, в якому ми описуємо, що ми будемо робити, якщо винекне дане виключення.
З блоком try ми можемо використовувати скільки-завгодно блоків except.
Також в try можуть бути блоки else та finally:
блок else відпрацюється в тому випадку, коли в try немає виключення.
блок finally - виконається незалежно, чи в блоці try було виключення, чи не було.
Можна використовувати try з finally без except і без else.
А можна - try з except, без finally і без else.

Після except в дужках можна вказати кілька типів виключень: except (KeyError, IndexError)

"""
print("1. ")
try:
    a + b
    1 / 0
    print('1/0')
    int('aaa')
    print("int('aaa')")
except ValueError:
    print("int('aaa'): ValueError")
except ZeroDivisionError:
    print('1/0: ZeroDivisionError')
except NameError:
    print('a + b: NameError')


print("2. ", "- "*20)
"""
СПОСОБИ, як відловити IndexError
"""
"""
1. після except вказати тип виключення
"""
s = 'hello'
try:
    s[7]   # рівносильно запису 'hello'[7]
except IndexError:
    print('error: IndexError')


"""
2. після except вказати батьківський клас нашого типу виключення
"""
print("3. ", "-- "*20)
s = 'hello'
try:
    s[6]
except LookupError:
    print('error: LookupError - IndexError2')


"""
Тип нашого виключення буде KeyError, 
але оскільки першим зустрінеться LookupError, який є батьківським типом нашого KeyError, то він і виведеться
"""
print("4. ", "+ "*20)
s = 'hello'
d = {}
try:
    d['key']
except LookupError:
    print('error: LookupError - KeyError/IndexError3')
except KeyError:
    print('error: KeyError')


print("= "*20)
s = 'hello'
d = {}
try:
    d['key']
except KeyError:
    print('error: KeyError')
except LookupError:
    print('error: LookupError - KeyError/IndexError3')


"""
3. після except не вказувати типу виключення: якщо НЕ вказувати тип виключення, то візьмуться ВСІ існуючі виключення.
Запис "except:"  аналогічний запису "except BaseException:" 
Але не потрібно писати блок, який обробляє ВСІ виключення, які можуть бути, як мінімум використати "except Exception:",
бо в нього не входять такі системні виключення як SystemExit, GeneratorExit, KeyboardInterrupt, які НЕ варто обробляти.
"""
print("# "*20)
s = 'hello'
d = {}
try:
    d['key']
except:  # = except BaseException:   but it is not correct
    print('error: BaseException')


"""
Блок finally: - він буде виконуватись ЗАВЖДИ, незалежно, чи в блоці try було виключення, чи не було.
"""
print("^ "*20)
s = 'hello'
d = {}
try:
    d['key']
except Exception:
    print('error')
finally:
    print('the END')


print("@ "*20)
s = 'hello'
d = {}
try:
   4 + 8   # NO errors but finally is executed in any case
except Exception:
    print('error')
finally:
    print('the END2')


"""
Блок finally як правило використовується, коли ми працюємо з файлом. 
При роботі з файлом можуть виникнути помилки, які ми не хочемо обробляти.
І у випадку, якщо виникне помилка, то відкритий файл збережеться в пам"яті, а це нам не потрібно.
І щоб уникнути Memory Leak і закрити файл, ми можемо в блоці finally закрити файл вручну.
"""
# in case when error happens but it is not caught by except:,
# then in finally block we can write file.close() to avoid memory leak, but error will occur anyway
# ex(1)
# print("$ "*20)
# f = open("123.txt")
# try:
#    execute(f)
# finally:
#     print('the END3!!!')
#     f.close()
#
# ex(2): error appears but block finally will be executed as well
# try:
#     1/0
# finally:
#     print('the END4')


"""
Після except в дужках можна вказати кілька типів виключень: except (KeyError, IndexError)
Блок else: відпрацюється в тому випадку, коли в try немає виключення.
"""
print("% "*20)
try:
    1/5
except (KeyError, IndexError):
    print('LookupErrors: KeyError or IndexError')
else:
    print('GOOD')
finally:
    print('END end END')


print("** "*20)
try:
    1/0
except (KeyError, IndexError):
    print('LookupErrors: KeyError or IndexError')
except ZeroDivisionError:
    print('ZeroDivisionError!!!')
else:
    print('GOOD')
finally:
    print('END end END')

"""
Під час написання виключень кожному типу виключення можна дати свій псевдонім. 
Для цього після типу виключення пишемо інструкцію as і далі даємо ім"я вказаному типу виключення:
except ZeroDivisionError as err
Якщо в калькуляторі представити змінну err до строкового типу: str(err) -> містить текст "division by zero"
Якщо подивитись на repr змінної err: repr(err) -> маємо сам клас помилки "ZeroDivisionError" і 
всередині нього вказується цей текст "division by zero".
Цю змінну err ми можемо тепер використовувати далі в коді, напр. наступним чином:
print(f"Logging error: {err} {repr(err)}") --> Logging error: division by zero ZeroDivisionError('division by zero'),
отже, виводиться спершу текст "division by zero", а потім сам клас помилки з текстом помилки: ZeroDivisionError('division by zero')
"""
print("- "*20)
try:
    1/0
except ZeroDivisionError as err:
    print("Zero Division Error happened!")    # Zero Division Error happened!
    print(f"Logging error: {err} {repr(err)}")   # Logging error: division by zero ZeroDivisionError('division by zero')


"""
Можна давати псевдонім одразу кульком питам виключень:
except (KeyError, IndexError) as error
При KeyError - у вигляді тексту ми отримаємо сам ключ, по якому і виникла помилка, 
а далі сам клас помилки з текстом цієї помилки.
При IndexError - у вигляді тексту ми отримаємо 'list index out of range', а далі - сам клас помилки з текстом цієї помилки.
"""
print("!-"*20)
ss = 'hello'
dd = {}
try:
    # dd['key']
    [1, 2, 3][10]
except (KeyError, IndexError) as error:
    print("Multiple errors: Lookup Error")    # Multiple errors: Lookup Error
    print(f"Logging error: {error} {repr(error)}")   # Logging error: 'key' KeyError('key')
    # Logging error: list index out of range IndexError('list index out of range')
