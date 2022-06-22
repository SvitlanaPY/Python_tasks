"""
Гипотеза Коллатца
Сиракузская последовательность, или последовательность Коллатца, строится так: возьмём натуральное число n;
если оно чётное, то заменим его числом n/2; если же оно нечётное, то заменим его числом 3n+1.
Получившееся число — следующее в сиракузской последовательности после числа n.
Затем заменяем получившееся число по тому же правилу, и так далее.
Определите, сколько шагов потребуется сиракузской последовательности, стартующей с заданного числа, чтобы прийти к 1.

Обычно, если проделать такую замену достаточно много раз, мы приходим к числу 1 (за которым следует снова 1). Например:

8 → 4 → 2 → 1 или 10 → 5 → 16 → 8 → 4 → 2 → 1.

Определите, сколько шагов потребуется сиракузской последовательности,
стартующей с заданного числа, чтобы прийти к 1.

Если вы обнаружите число, сиракузская последовательность от которого не приходит к 1, то... вы, скорее всего, ошиблись.
Но если нет, то поздравляем: вы прославитесь, ведь вопрос о том,
всегда ли сиракузская последовательность приходит к 1
(независимо от начального числа), давно будоражит умы математиков.

Формат ввода
Вводится одно натуральное число n.

Формат вывода
Выводится одно число — количество шагов, необходимое стартующей от n сиракузской последовательности,
чтобы впервые дойти до 1.

Sample Input 1:
10
Sample Output 1:
6

Sample Input 2:
16
Sample Output 2:
4
"""


n = int(input())
amount = 0
while True:
    if n % 2 == 0:
        n = int(n // 2)
        amount += 1
    else:
        n = 3 * n + 1
        amount += 1
    if n == 1:
        break
print(amount)

# №2:
# n = int(input())
# amount = 0
# while n != 1:
#     if n % 2 == 0:
#         n = int(n // 2)
#         amount += 1
#     else:
#         n = 3 * n + 1
#         amount += 1
# print(amount)