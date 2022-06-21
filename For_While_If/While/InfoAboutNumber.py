x = int(input())
amount_num = 0
amount_parni = 0
amount_neparni = 0
summ_ = 0
dobutok_ = 1
maxx_ = 0
minn_ = 9
while x > 0:
    last_num = x % 10
    # print(last_num)   # - виводимо цифри з кінця
    if last_num % 2 == 0:
        amount_parni += 1
    else:
        amount_neparni += 1
    if last_num > maxx_:
        maxx_ = last_num
    if last_num < minn_:
        minn_ = last_num
    amount_num += 1
    summ_ += last_num
    dobutok_ *= last_num
    x = x // 10
    print(x)
print('Всього цифр у введеному числі: ', amount_num)
print('Всього парних цифр у введеному числі: ', amount_parni)
print('Всього непарних цифр у введеному числі: ', amount_neparni)
print("Сума всіх цифр у введеному числі: ", summ_)
print("Добуток всіх цифр у введеному числі: ", dobutok_)
print("Максимальна цифра у введеному числі: ", maxx_)
print("Мінімальна цифра у введеному числі: ", minn_)

