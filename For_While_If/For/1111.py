z = int(input())
summ = 0
while z > 0:
    last_num = z % 10
    summ = summ + last_num
    z = z // 10
print(summ)

