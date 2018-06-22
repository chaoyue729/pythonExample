# -*- coding: utf-8 -*-
# 코드 내부에 한글을 사용가능 하게 해주는 부분입니다.

#pandas 라이브러리를 불러옵니다.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sys import exit

#피마 인디언 당뇨병 데이터셋을 불러옵니다. 불러올 때 각 컬럼에 해당하는 이름을 지정합니다.
df = pd.read_csv('./dataset/meta_20180425235959_daejun_48.csv',
               names = ["stttaid", "c1", "c2", "c3", "c4", "center", "comp", "p1", "p2", "p3", "p4", "s1", "s2", "s3", "s4", "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8"], delimiter = "|")

# print(df.head(10))
# print(df[2000:2010])

for index, row in df.ix[2000:2010].iterrows():
    print(row['s1'], row['e8'])

exit()


# print(df.index)
x, y = [], []
for index, row in df.head(10).iterrows():
    # print(index, row['s1'], str(row['e8']).replace(';', ' '))
    x.append(row['s1'])
    y.append(str(row['e8']).replace(';', ' '))

print(x)
print(y)

print(df.groupby(['s1']).size())
print(df.groupby(['s1']).size().reset_index(name='counts'))

#처음 5줄을 봅니다.
print(df.head(5))


#데이터의 전반적인 정보를 확인해 봅니다.
print(df.info())

#각 정보별 특징을 좀더 자세히 출력합니다.
print(df.describe())


