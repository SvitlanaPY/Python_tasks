def first():
    print('start first')
    print('finish first')

print('hello')
first()

#
# def first1():
#     print('start first')
#     1 / 0
#     print('finish first')
#
# print('hello1')
# first1()
# we will see two error messages: the first about error in our main code where the function is called: line 15, in <module> first()
# the second error: about the line with error line 11, in first 1 / 0


# def first2():
#     print('start one')
#     print('finish one')
#
# def second2():
#     print("start two")
#     second2()
#     print('finish two')
#
# print('-----------------------')
# print('hello2')
# first2()


# here is an example of THREE error messages in Traceback
# def first3():
#     print('start one')
#     second3()
#     print('finish one')
#
# def second3():
#     print("start two")
#     1/0
#     print('finish two')
#
# print('-----------------------')
# print('hello3')
# first3()


# here is an example of FOUR error messages in Traceback
# def third4():
#     print('start third')
#     1/0
#     print('finish third')
#
# def second4():
#     print("start two")
#     third4()
#     print('finish two')
#
# def first4():
#     print('start one')
#     second4()
#     print('finish one')
#
# print('-----------------------')
# print('hello4')
# first4()


#  Handling error
# def third5():
#     print('start third')
#     try:
#         1/0
#     except ZeroDivisionError:
#         print("HANDLING ERROR")
#     print('finish third')
#
# def second5():
#     print("start two")
#     third5()
#     print('finish two')
#
# def first5():
#     print('start one')
#     second5()
#     print('finish one')
#
# print('-----------------------')
# print('hello5')
# first5()

# VKLADENIST'
def third6():
    print('start third')
    1/0
    print('finish third')

def second6():
    print("start two")
    third6()
    print('finish two')

def first6():
    print('start one')
    try:
        second6()
    except ZeroDivisionError:
        print('HANDLING ERROR IN FIRST()')
    print('finish one')

print('-----------------------')
print('hello6')
first6()

