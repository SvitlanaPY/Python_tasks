# сортировки пузырьком.
# Все просто, вам поступает число n - количество элементов в списке, и затем сам список.
# Ваша задача отсортировать список по возрастанию при помощи пузырьковой сортировки,
# в случае если элементы соседние совпадают менять их ненужно.
# В качестве ответа нужно вывести отсортированный список и
# какое количество раз пришлось переставлять элементы в процессе сортировки.

# Sample Input 1:
# 7
# 8 5 3 1 4 7 9
# Sample Output 1:
# 1 3 4 5 7 8 9
# 9

# Sample Input 2:
# 3
# 9 8 -4
# Sample Output 2:
# -4 8 9
# 3


# оптимізований алгоритм виглядатиме наступним чином
n = 6
mas = [5, 7, 4, 3, 8, 2]
count = 0   # к-сть замін
for run in range(n - 1):    # кількість всіх обходів/повторів
    for i in range(n - 1 - run):  # оскільки при кожному проході вспливатиме найбільший елемент, то нам вже не потрібно буде порівнювати з останніми елементами
        print(f"Порівнюємо {mas[i]} із {mas[i + 1]}")
        if mas[i] > mas[i + 1]:
            count += 1
            mas[i], mas[i + 1] = mas[i + 1], mas[i]
    print(*mas)
print("К-сть перестановок: ", count)


# n = int(input())
# mas = list(map(int, input().split()))   # 5 7 4 3 8 2
# беремо елемент і порівнюємо його із сусідом справа
# у останнього елемента немає сусіда справа, тому обхід на 1 менше за n: (n - 1)

# код для ОДНОГО обходу
# n = 6
# mas = [5, 7, 4, 3, 8, 2]
# count = 0   # к-сть замін
# for i in range(n - 1):
#     if mas[i] > mas[i+1]:
#         count += 1
#         mas[i], mas[i + 1] = mas[i+1], mas[i]
# print(mas)
# print(count)


# обходів має бути на 1 менше, ніж к-сть елементів
# n = 6
# mas = [5, 7, 4, 3, 8, 2]
# count = 0   # к-сть замін
# for run in range(n - 1):    # кількість всіх обходів
#     for i in range(n - 1):  # один прохід
#         print(f"Порівнюємо {mas[i]} із {mas[i + 1]}")
#         if mas[i] > mas[i + 1]:
#             count += 1
#             mas[i], mas[i + 1] = mas[i + 1], mas[i]
#     print(*mas)
# print(count)
# Порівнюємо 5 із 7
# Порівнюємо 7 із 4
# Порівнюємо 7 із 3
# Порівнюємо 7 із 8
# Порівнюємо 8 із 2
# 5 4 3 7 2 8
# Порівнюємо 5 із 4
# Порівнюємо 5 із 3
# Порівнюємо 5 із 7
# Порівнюємо 7 із 2
# Порівнюємо 7 із 8
# 4 3 5 2 7 8
# Порівнюємо 4 із 3
# Порівнюємо 4 із 5
# Порівнюємо 5 із 2
# Порівнюємо 5 із 7
# Порівнюємо 7 із 8
# 3 4 2 5 7 8
# Порівнюємо 3 із 4
# Порівнюємо 4 із 2
# Порівнюємо 4 із 5
# Порівнюємо 5 із 7
# Порівнюємо 7 із 8
# 3 2 4 5 7 8
# Порівнюємо 3 із 2
# Порівнюємо 3 із 4
# Порівнюємо 4 із 5
# Порівнюємо 5 із 7
# Порівнюємо 7 із 8
# 2 3 4 5 7 8
# 10
