try:
    a + b
    1 / 0
    print('1/0')
    int('aaa')
    print("int('aaa')")
except ValueError:
    print('error: ValueError')
except ZeroDivisionError:
    print('error: ZeroDivisionError')
except NameError:
    print('error: NameError')



s = 'hello'
try:
    s[7]
except IndexError:
    print('error: IndexError')


s = 'hello'
try:
    s[6]
except LookupError:
    print('error: IndexError2 from LookupError')


s = 'hello'
d = {}
try:
    d['key']
except LookupError:
    print('error: IndexError3 from LookupError')


s = 'hello'
d = {}
try:
    d['key']
except KeyError:
    print('error: KeyError')
except LookupError:
    print('error: IndexError3')


s = 'hello'
d = {}
try:
    d['key']
except:  # = except BaseException:   but it is not correct
    print('error: BaseException')


s = 'hello'
d = {}
try:
    d['key']
except Exception:
    print('error')
finally:
    print('the END')


s = 'hello'
d = {}
try:
   4 + 8   # NO errors but finally is executed in any case
except Exception:
    print('error')
finally:
    print('the END2')


# in case when error happens but it is not caught by except:,
# then in finally block we can write file.close() to avoid memory leak, but error will occur anyway
# ex(1)
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


try:
    1/5
except (KeyError, IndexError):
    print('LookupErrors: KeyError or IndexError')
else:
    print('GOOD')
finally:
    print('END end END')


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