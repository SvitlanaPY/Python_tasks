def fact(n):
    pr=1
    a=[]
    for i in range(1,n+1):
        pr=pr*i
        a.append(pr)
    return a

print(fact(10))
