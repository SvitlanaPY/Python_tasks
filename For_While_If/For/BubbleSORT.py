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

n = int(input())
mas = list(map(int, input().split()))
count = 0
for run in range(n - 1):
    for i in range(n - 1 - run):
        if mas[i] > mas[i + 1]:
            count += 1
            mas[i], mas[i + 1] = mas[i + 1], mas[i]
print(*mas)
print(count)
