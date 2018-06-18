import numpy as np
import itertools
# from itertools import ifilter
# print (list(ifilter(lambda x: x < 10, [1, 4, 6, 7, 11, 34, 66, 100, 1])))

a = np.array([1,2,3,4,5,6,7,8,9])
index=[2,3,6]
# a = np.array(list(itertools.compress(a, [i not in index for i in range(len(a))])))
a = np.array(list(itertools.filterfalse(lambda x: x > 6, a)))
print (a)

print (list((1,2,[3,4])))
print (list(index))

b = np.array(range(20)).reshape((4,5))
print(b)

for arr in b:
    print( np.array(list(itertools.filterfalse(lambda x: x > 6, arr))) )