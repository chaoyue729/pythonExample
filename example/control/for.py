a = [None] * 10
for i, v in enumerate(a):
    print(i, v)

for i in range(0, 11):
    print(i)

b = range(1, 4)
# c = [i * 2 for i in b]
# print(c)
for i in [i * 2 for i in b]:
    print(i)

