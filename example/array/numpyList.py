#-*- coding: utf-8 -*-

import numpy as np
import collections
from sys import exit

# ar = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(type(ar))
# for i in ar:
#     print(i)

# a = np.arange(15).reshape(3, 5)
# print(a)
# print(a.T)
# print(np.transpose(a))

# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(np.full((2, len(arr)), arr))

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
for a1 in a:
    for idx, n in enumerate(a1):
        print(idx, n)

exit()

test1 = np.array(['111', '222', '333', '111', '555'])
# print(test1 == '111')
# test2 = np.array(test1 == '111')
# print(len(test1[test2]))


mat = np.array([])
for r in test1:
    mat = np.append(mat, r)
print(mat)
# mat = np.array([])
# print(mat)
# print(len(mat))

# print(np.where( mat=='666'))
# print(len(np.where( mat=='666')))
# print(np.where( mat=='111'))
# print(len(np.where( mat=='111')))

print(np.count_nonzero(mat == '111') > 0)
print(np.count_nonzero(mat == '666'))
num_zeros = (mat == '111').sum()
print(num_zeros)




# Arr = np.ndarray((3,4))
# def foo(x):
#     return x * x
# foo = np.vectorize(foo)  # 함수를 적용.  array에 적용가능하도록 변경.
# result = foo(Arr)  # Arr는 array의 이름임.



