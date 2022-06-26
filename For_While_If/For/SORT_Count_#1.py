"""
Давайте на практике применим метод подсчета
На вход вашей программе поступает положительное целое число n,
а ваша задача вывести в порядке возрастания все цифры,bvкоторые встречались в этом числе,
и напротив каждого также необходимо вывести сколько раз данная цифра встречалась в числе n.

Sample Input 1:
45654
Sample Output 1:
4 2
5 2
6 1

Sample Input 2:
11111
Sample Output 2:
1 5
"""


# n = '45654'
# n = list(map(int, input().replace('', ' ').strip().split()))  => list(map(int, input()))
n = list(map(int, input()))
print(n)
# [4, 5, 6, 5, 4]
count = [0] * 10
for i in n:
    count[i] += 1
print(count)
# [0, 0, 0, 0, 2, 2, 1, 0, 0, 0]
for i in range(10):
    if count[i] > 0:
        print(i, count[i])


# arr = list(map(int, input()))
# maxx = max(arr)
# new_arr = [0] * (maxx + 1)
# for elem in arr:
#     new_arr[elem] = new_arr[elem] + 1
# arr.clear()
# for i in range(len(new_arr)):
#     arr = arr + [i] * new_arr[i]
#     if new_arr[i] > 0:
#         print(i, new_arr[i])
