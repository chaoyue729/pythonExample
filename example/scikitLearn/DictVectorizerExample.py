'''
https://datascienceschool.net/view-notebook/3e7aadbf88ed4f0d87a76f9ddc925d69/

각 단어의 수를 세어놓은 사전에서 BOW 벡터를 만든다.

DictVectorizer는 feature_extraction 서브 패키지에서 제공한다. 문서에서 단어의 사용 빈도를 나타내는 딕셔너리 정보를 입력받아 BOW 인코딩한 수치 벡터로 변환한다.
'''
from sklearn.feature_extraction import DictVectorizer

V = DictVectorizer(sparse=False)
D = [{'A': 1, 'B': 2}, {'B': 3, 'C': 1}]
X = V.fit_transform(D)

print(X)
# array([[1., 2., 0.],
#        [0., 3., 1.]])

print(V.feature_names_)
# ['A', 'B', 'C']

print(V.transform({'C': 4, 'D': 3}))
# array([[0., 0., 4.]])