'''
https://brownbears.tistory.com/238

ProcessPoolExecutor 을 사용할 경우 함수들이 모두 위에 있어야 한다
'''

import numpy as np
from time import time
from concurrent.futures import ProcessPoolExecutor

def gcd2(a, b):
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

def npTest(npData):
    n = 0
    for v in npData:
        n = n + v
    return n

start = time()
pool = ProcessPoolExecutor(max_workers=2)

# 병렬성이 없으므로 이 함수를 순서대로 실행하면 시간이 선형적으로 증가
numbers = [(1963309, 2265973), (2030677, 3814172), (1551645, 2229620),
           (2039045, 2020802)]
results = list(pool.map(gcd, numbers))
print(results)

numbers1 = [1963309, 2030677, 1551645]
numbers2 = [2265973, 3814172, 2229620]
results = list(pool.map(gcd2, numbers1, numbers2)) # 인자값이 2개 이상인 경우 zip 으로 전달
print(results)

npData = np.full((2,3), 5)
results = list(pool.map(npTest, npData))
print(results)

end = time()
print('Took %.3f seconds' % (end - start))

# 결과
# Took 0.533 seconds