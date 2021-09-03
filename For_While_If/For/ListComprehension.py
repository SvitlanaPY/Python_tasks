st = 'Create a list of the first letters of every word in this string'
st = st.split(' ')
print(st)
a = []
for i in st:
    a.append(i[0])
print(a)


stt = 'Create a list of the first letters of every word in this string'
aa = [i[0] for i in stt.split(' ')]
print(aa)