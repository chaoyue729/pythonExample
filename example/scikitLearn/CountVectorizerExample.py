'''
https://datascienceschool.net/view-notebook/3e7aadbf88ed4f0d87a76f9ddc925d69/

CountVectorizer는 다음과 같은 세가지 작업을 수행한다.
    1. 문서를 토큰 리스트로 변환한다.
    2. 각 문서에서 토큰의 출현 빈도를 센다.
    3. 각 문서를 BOW 인코딩 벡터로 변환한다.

CountVectorizer는 이러한 작업을 하기 위한 다음과 같은 인수를 가질 수 있다.
    stop_words : 문자열 {‘english’}, 리스트 또는 None (디폴트)
    stop words 목록.‘english’이면 영어용 스탑 워드 사용.
    analyzer : 문자열 {‘word’, ‘char’, ‘char_wb’} 또는 함수
    단어 n-그램, 문자 n-그램, 단어 내의 문자 n-그램
    token_pattern : string
    토큰 정의용 정규 표현식
    tokenizer : 함수 또는 None (디폴트)
    토큰 생성 함수 .
    ngram_range : (min_n, max_n) 튜플
    n-그램 범위
    max_df : 정수 또는 [0.0, 1.0] 사이의 실수. 디폴트 1
    단어장에 포함되기 위한 최대 빈도
    min_df : 정수 또는 [0.0, 1.0] 사이의 실수. 디폴트 1
    단어장에 포함되기 위한 최소 빈도
'''
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
# {'document': 1, 'and': 0, 'third': 8, 'one': 5, 'last': 4, 'second': 6, 'is': 3, 'this': 9, 'the': 7, 'first': 2}

print(vect.transform(['This is the second document.']).toarray())
# [[0 1 0 1 0 0 1 1 0 1]]

print(vect.transform(corpus).toarray())
# [[0 1 1 1 0 0 0 1 0 1]
#  [0 1 0 1 0 0 2 1 0 1]
#  [1 0 0 0 0 1 0 1 1 0]
#  [0 1 1 1 0 0 0 1 0 1]
#  [0 1 0 0 1 0 0 1 0 0]]
exit()

vect = CountVectorizer(stop_words=["and", "is", "the", "this"]).fit(corpus)
print(vect.vocabulary_)
print(vect.transform(['This is the second document.']).toarray())
# {'one': 3, 'first': 1, 'last': 2, 'document': 0, 'third': 5, 'second': 4}
# [[1 0 0 0 1 0]]

vect = CountVectorizer(stop_words="english").fit(corpus)
print(vect.vocabulary_)
# {'document': 0, 'second': 1}

vect = CountVectorizer(token_pattern="t\w+").fit(corpus)
print(vect.vocabulary_)
# {'this': 2, 'the': 0, 'third': 1}

vect = CountVectorizer(ngram_range=(2, 2)).fit(corpus)
print(vect.vocabulary_)
# {'this is': 12,
#  'is the': 2,
#  'the first': 7,
#  'first document': 1,
#  'the second': 9,
#  'second second': 6,
#  'second document': 5,
#  'and the': 0,
#  'the third': 10,
#  'third one': 11,
#  'is this': 3,
#  'this the': 13,
#  'the last': 8,
#  'last document': 4}

vect = CountVectorizer(ngram_range=(1, 2), token_pattern="t\w+").fit(corpus)
print(vect.vocabulary_)
# {'this': 3, 'the': 0, 'this the': 4, 'third': 2, 'the third': 1}

'''
max_df, min_df 인수를 사용하여 문서에서 토큰이 나타난 횟수를 기준으로 단어장을 구성할 수도 있다. 토큰의 빈도가 max_df로 지정한 값을 초과 하거나 min_df로 지정한 값보다 작은 경우에는 무시한다. 인수 값은 정수인 경우 횟수, 부동소수점인 경우 비중을 뜻한다.
'''
vect = CountVectorizer(max_df=4, min_df=2).fit(corpus)
print(vect.vocabulary_, vect.stop_words_)
# ({'this': 3, 'is': 2, 'first': 1, 'document': 0},
#  {'and', 'last', 'one', 'second', 'the', 'third'})

print(vect.transform(corpus).toarray().sum(axis=0))
# array([4, 2, 3, 3])