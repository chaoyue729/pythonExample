'''
https://gomguard.tistory.com/173
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

lst = [[1,2,3,4,5,6,7],
        [10,15,20,25,50,55,60],
        [0,0,0,0,0,0,0],
        [-1,-20,-30,-45,-50,-55,-70]]

df = pd.DataFrame(lst).T
corr = df.corr()
print(corr)

colormap = plt.cm.gist_heat   #그래프의 색상 구성을 정합니다.
plt.figure(figsize=(8,8))   #그래프의 크기를 정합니다.
# 그래프의 속성을 결정합니다. vmax의 값을 0.5로 지정해 0.5에 가까울 수록 밝은 색으로 표시되게 합니다.
sns.heatmap(df.corr(),linewidths=0.1,vmax=0.5, cmap=colormap, linecolor='white', annot=True)
# sns.pairplot(df, hue='class');
plt.show()
