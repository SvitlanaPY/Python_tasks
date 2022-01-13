listt = []

for i in range(20):
    listt.append(lambda x: x + i)
    r = listt[i](3)
    print("r: ", r)
    print("i= ", i)


print("listt: ", listt)
print("listt len: ", len(listt))
print(listt[12], listt[2])

r = listt[0](3)
print(r)
# 22

