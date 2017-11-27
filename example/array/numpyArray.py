#-*- coding: utf-8 -*-

import numpy as np

ar = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(type(ar))

for i in ar:
    print(i)

a = np.arange(15).reshape(3, 5)
print(a)
print(a.T)
print(np.transpose(a))


test1 = np.array(['111', '222', '333', '111', '555'])
print(test1 == '111')
test2 = np.array(test1 == '111')
print(len(test1[test2]))

# Arr = np.ndarray((3,4))
# def foo(x):
#     return x * x
# foo = np.vectorize(foo)  # 함수를 적용.  array에 적용가능하도록 변경.
# result = foo(Arr)  # Arr는 array의 이름임.