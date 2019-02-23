'''
https://datascienceschool.net/view-notebook/3e7aadbf88ed4f0d87a76f9ddc925d69/

TF-IDF(Term Frequency – Inverse Document Frequency) 인코딩은 단어를 갯수 그대로 카운트하지 않고 모든 문서에 공통적으로 들어있는 단어의 경우 문서 구별 능력이 떨어진다고 보아 가중치를 축소하는 방법이다.

구제적으로는 문서  𝑑 (document)와 단어  𝑡  에 대해 다음과 같이 계산한다.

tf-idf(𝑑,𝑡)=tf(𝑑,𝑡)⋅idf(𝑡)
 
여기에서

tf(𝑑,𝑡) : term frequency. 특정한 단어의 빈도수
idf(𝑡)  : inverse document frequency. 특정한 단어가 들어 있는 문서의 수에 반비례하는 수

idf(𝑑,𝑡)=log𝑛1+df(𝑡)
 
𝑛  : 전체 문서의 수

df(𝑡) : 단어  𝑡 를 가진 문서의 수

결과값
tf-idf값이 높을수록 다른 문서에 잘 언급되지 않은 단어(my, love, hate, hobby, is, passion)인 것을 알 수 있다.
tf-idf값이 낮을수록 다른 문서에 잘 언급하는 단어(I, dogs, and, knitting)인 것을 알 수 있다.
'''
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sys import exit
corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
    'The last document?',    
]
vect = CountVectorizer()
vect.fit(corpus)
print(vect.vocabulary_)
print(sorted(vect.vocabulary_.items(), key=lambda kv: kv[1]))
tfidv = TfidfVectorizer().fit(corpus)

for c in corpus:
    print(tfidv.transform([c]).toarray()[0])
# print(tfidv.transform(corpus).toarray())
# array([[0.        , 0.38947624, 0.55775063, 0.4629834 , 0.        ,
#         0.        , 0.        , 0.32941651, 0.        , 0.4629834 ],
#        [0.        , 0.24151532, 0.        , 0.28709733, 0.        ,
#         0.        , 0.85737594, 0.20427211, 0.        , 0.28709733],
#        [0.55666851, 0.        , 0.        , 0.        , 0.        ,
#         0.55666851, 0.        , 0.26525553, 0.55666851, 0.        ],
#        [0.        , 0.38947624, 0.55775063, 0.4629834 , 0.        ,
#         0.        , 0.        , 0.32941651, 0.        , 0.4629834 ],
#        [0.        , 0.45333103, 0.        , 0.        , 0.80465933,
#         0.        , 0.        , 0.38342448, 0.        , 0.        ]])