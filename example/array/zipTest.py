
a = [1,2,3,4,5]
b = ['a','b','c','d','e']
cs = zip(a,b)
for x,y in cs:
	print(str(x) + ", " + str(y))
print('1')
print(cs)
for x,y in zip(a,b):
	print(str(x) + ", " + str(y))
print('2')
for c in zip(a,b):
	print(str(c[0]) + ", " + str(c[1]))
