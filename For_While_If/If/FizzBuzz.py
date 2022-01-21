# FizzBuzz
# Ваша программа должна считать одно натуральное число, после чего вывести:
# “Fizz”, если это число делится на 3;
# “Buzz”, если это число делится на 5;
# “FizzBuzz”, если выполнены оба предыдущих условия;
# само это число в остальных случаях.

n = int(input())
if n % 5 != 0 and n % 3 != 0:
    print(n)
elif n % 3 == 0:
    if n % 5 == 0:
        print('FizzBuzz')
    else:
        print('Fizz')
else:
    print('Buzz')


# a=int(input())
# if a%3==0 and a%5==0:
#     print('FizzBuzz')
# elif a%3==0:
#     print('Fizz')
# elif a%5==0:
#     print('Buzz')
# else:
#     print(a)
