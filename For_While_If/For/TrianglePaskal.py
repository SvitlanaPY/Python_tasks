n = int(input())
triangle = []
# [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
for i in range(n+1):
    triangle.append([1] + [0]*n)

for i in triangle:
    print(i)
