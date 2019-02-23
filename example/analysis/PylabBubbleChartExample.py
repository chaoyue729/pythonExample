'''
https://datascienceschool.net/view-notebook/6e71dbff254542d9b0a054a7c98b34ec/
https://datascienceschool.net/view-notebook/6e71dbff254542d9b0a054a7c98b34ec/

데이터가 2차원이 아니라 3차원 혹은 4차원인 경우에는 점 하나의 크기 혹은 색깔을 이용하여 다른 데이터 값을 나타낼 수도 있다. 이런 차트를 버블 차트(bubble chart)라고 한다. 크기는 s 인수로 색깔은 c 인수로 지정한다.
'''

import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np

N = 5
np.random.seed(0)
x = np.random.rand(N)
y1 = np.random.rand(N)
y2 = np.random.rand(N)
y3 = np.pi * (15 * np.random.rand(N))**2

print(x)
print(y1)
print(y2)
print(y3)

# x = [x for x in range(0, N)]
# y1 = [x for x in range(0, N)]
# y2 = [x for x in range(0, N)]
# y3 = [x for x in range(0, N)]

plt.title("Bubble Chart")
plt.scatter(x, y1, c=y2, s=y3)
plt.show()