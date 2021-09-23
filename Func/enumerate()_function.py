# Python program to illustrate
# enumerate function in loops
l1 = ["eat", "sleep", "repeat"]
y = enumerate(l1)
print("enumerated l1:", list(y))
# enumerated l1: [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]

# printing the tuples in object directly
# for ele in enumerate(l1):  # ele = (0, 'eat'), (1, 'sleep'), (2, 'repeat')
# 	print(ele)
# print(list(enumerate(l1)))

# changing index and printing separately
# for count, ele in enumerate(l1, 100):  # count = 100, 101, 102; ele = eat, sleep, repeat
# 	print(count, ele)

# # getting desired output from tuple
for count, ele in enumerate(l1):
	print(count)
	print(ele)