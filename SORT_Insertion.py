# Сортировка вставками (лінійний алгоритм)
# лінійний, бо час виконання лінійний - к-сть циклів виконання залежить від змінної n
# Это еще один вид сортировки, который реализуется при помощи вложенных циклов

# Программа получает на вход число n - количество элементов в списке, и затем в следующей строке сам список.
# Ваша задача отсортировать список по возрастанию при помощи сортировки вставками,
# в случае если элементы соседние совпадают менять их ненужно.
# В качестве ответа нужно вывести отсортированный список.
#
# Sample Input 1:
# 6
# 5 4 2 15 6 6
# Sample Output 1:
# 2 4 5 6 6 15

# Sample Input 2:
# 5
# 11 2 8 1 5
# Sample Output 2:
# 1 2 5 8 11

count = 0
n = 10
mas = [12, 14, 5, 7, 4, 3, 8, -15, 2, -7]
for i in range(1, n):
    save = mas[i]    # у змінну save записуємо елемент для вставки; індекс елемента = № обходу; save - як підмасив
    while i != 0 and mas[i - 1] > save:   # порвняння елементу, записаного в save із попереднім елементом
        count += 1
        mas[i] = mas[i - 1]   # переміщення/зсув вправо елемента, більшого за save
        i -= 1   # зміщення циклу вліво (зменшення)
    mas[i] = save   # вставляємо менший елемент у потрібну позицію
print(mas)
print(count)


# count = 0
# n = 10
# mas = [12, -4, 5, 7, 4, 3, 8, -15, 2, -7]
# for i in range(1, n):
#     save = mas[i]    # у змінну save записуємо елемент для вставки; індекс елемента = № обходу
#     j = i
#     while j != 0 and mas[j - 1] > save:
#         count += 1
#         mas[j] = mas[j - 1]
#         j -= 1
#     mas[j] = save
# print(mas)
# print(count)
