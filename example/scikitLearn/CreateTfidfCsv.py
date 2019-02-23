import pandas as pd
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.preprocessing import LabelEncoder
from sys import exit
import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np
# from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import stopwatch

sw = stopwatch.stopWatch()
pool = ProcessPoolExecutor(max_workers=4)
# pool = ThreadPoolExecutor(max_workers=10)

# 메타 파일 경로
metaFilePath = '/Users/whitexozu/dev/project/lgu+/data/lotte_data/lotte_ctgr_data_small.csv'
# metaFilePath = '/Users/whitexozu/dev/project/lgu+/data/lotte_data/lotte_ctgr_data_medium.csv'
# metaFilePath = '/Users/whitexozu/dev/project/lgu+/data/lotte_data/lotte_ctgr_data.csv'
# tfidf 최소값 (최소값 이상으로 정제 하기 위해 사용)
tfidfMinimum = 0.1
# 불용어
unusedWord = ['지금', '롯데는', '주십시오', '아예', '그래서', '그리고']
# 모든 call 데이터 저장용 list
corpus = []
# 모든 분류 데이터 저장용 list
categoryList = []
categoryListLE = [] # LavelEncoder 적용
# call 전체 건수
lineCount = 0
# call 전체 데이터중 tfidf 최소값 이상의 word를 category별로 취합하기 위한 변수
wordByCategory = {}
wordByCategoryReFined = {}  # 정제

# 메타 데이터 로딩 후 콜배열, 분류배열 에 각각 저장
sw.start('open file')
with open(metaFilePath) as metaFile:
    metaReader = csv.reader(metaFile, delimiter='\t')
    for row in metaReader:
        categoryList.append(row[1])
        corpus.append(row[2])
        lineCount += 1
    # print('lineCount : ', lineCount)
sw.stop('open file')

sw.start('label encoder')
le = LabelEncoder()
le.fit(categoryList)
# print(le.classes_)
categoryListLE = le.transform(categoryList)
# print(categoryListLE)
# print(categoryList[0], le.inverse_transform(6))
sw.stop('label encoder')

# 통계 데이터를 위해 분류별 가중치 이상의 단어들을 담을 dict 생성
vectOverWeight = [None] * lineCount

# 문서전체의 토큰 리스트 생성
sw.start('create token list')
vect = CountVectorizer(stop_words=unusedWord)
vect.fit(corpus)
vectSort = sorted(vect.vocabulary_.items(), key=lambda kv: kv[1])
# print('vectSort len : ', len(vectSort))
# print('vectSort : ', vectSort)
sw.stop('create token list')

# call 별 tfidf 추출
sw.start('transform tfidf')
tfidv = TfidfVectorizer(stop_words=unusedWord).fit(corpus)
# ifidfTransList = tfidv.transform(corpus).toarray().tolist()
ifidfTransList = []
for i, c in enumerate(corpus):
    ifidfTransList.append(tfidv.transform([c]).toarray()[0])
sw.stop('transform tfidf')

# sw.start('create hashing vectorizer')
# hv = HashingVectorizer(n_features=len(vectSort), encoding='utf-8')
# ifidfTransList = hv.fit_transform(ifidfTransList)
# sw.stop('create hashing vectorizer')


# for i, t in enumerate(ifidfTransList):
    # print(i, 'ifidfTransList : ', len([w for w in t if w >  tfidfMinimum]))
    # print([w for w in t if w >  tfidfMinimum])


# sw.start('create vectOverWeight numpy')
# numpyVectSort = np.array(vectSort)
# numPyVectOverWeight = [None] * lineCount
# numpyTfidfList = np.array(ifidfTransList)
# for callIdx, tfidfCall in enumerate(numpyTfidfList):
#     numPyVectOverWeight[callIdx] = {'category': categoryList[callIdx], 'wordNValues': np.array([]), 'wordCount': 0}
#     for wordIdx, tfidfWord in enumerate(np.array(tfidfCall)):
#         if tfidfWord > tfidfMinimum:
#             np.append(numPyVectOverWeight[callIdx]['wordNValues'], ((numpyVectSort[wordIdx][0], tfidfWord)))
#             numPyVectOverWeight[callIdx]['wordCount'] = len(numPyVectOverWeight[callIdx]['wordNValues'])
# sw.stop('create vectOverWeight numpy')

# tfidf 최소값 초과의 값을 저장
# sw.start('create vectOverWeight')
# for callIdx, tfidfCall in enumerate(ifidfTransList):
#     # 분류 정보로 초기화
#     vectOverWeight[callIdx] = {'category': categoryList[callIdx], 'wordNValues': [], 'wordCount': 0}
#     # vectOverWeight[callIdx] = {'category': categoryListLE[callIdx], 'wordNValues': [], 'wordCount': 0}
#     for wordIdx, tfidfWord in enumerate(tfidfCall):
#         if tfidfWord > tfidfMinimum:
#             vectOverWeight[callIdx]['wordNValues'].append((vectSort[wordIdx][0], tfidfWord))
#             vectOverWeight[callIdx]['wordCount'] = len(vectOverWeight[callIdx]['wordNValues'])
# sw.stop('create vectOverWeight')

def createVectOverWeight(pair):
    callIdx, tfidfCall = pair
    # 분류 정보로 초기화
    rtnDict = {'category': categoryList[callIdx], 'wordNValues': [], 'wordCount': 0}
    for wordIdx, tfidfWord in enumerate(tfidfCall):
        if tfidfWord > tfidfMinimum:
            rtnDict['wordNValues'].append((vectSort[wordIdx][0], tfidfWord))
    rtnDict['wordCount'] = len(rtnDict['wordNValues'])
    return callIdx, rtnDict

# tfidf 최소값 초과의 값을 저장
sw.start('create vectOverWeight')
vectOverWeight = list(pool.map(createVectOverWeight, enumerate(ifidfTransList)))
for r in results:
    vectOverWeight[r[0]] = r[1]
sw.stop('create vectOverWeight')

# category 별 join
sw.start('join category')
for rf in vectOverWeight:
    if rf['category'] not in wordByCategory:
        wordByCategory[rf['category']] = []
    wordByCategory[rf['category']] = wordByCategory[rf['category']] + rf['wordNValues']
sw.stop('join category')

# 중복 키워드 삭제
sw.start('delete duplication word')
wordByCategoryDupIndex = {}
for wcKey, wcValue in wordByCategory.items():
    wordByCategoryDupIndex = []
    for fi, fv in enumerate(wcValue):
        for si, sv in enumerate(wcValue):
            # if fi != si and fv[0] == sv[0]:
            #     print(wcKey, fi, fv, si, sv)
            if fi != si and fv[0] == sv[0] and fv[1] > sv[1]:
                wordByCategoryDupIndex.append(si)
    wordByCategoryDupIndex = list(set(wordByCategoryDupIndex))
    wordByCategoryDupIndex = sorted(wordByCategoryDupIndex, key=lambda idx: idx, reverse=True)
    # print(wordByCategoryDupIndex)
    for di in wordByCategoryDupIndex:
        del wcValue[di]
    # print(wcKey, len(wcValue))
    # wordByCategoryReFined[wcKey] = vect.transform([' '.join(wcValue)]).toarray()[0]
sw.stop('delete duplication word')

# sw.prettyPrint()
# exit()

# 구분별 키워드 보고서
sw.start('report word by category')
for wcKey, wcValue in wordByCategory.items():
    print(wcKey, [w[0] for w in wcValue])
    print('-----------------------------------------------')
# print(wcKey, [w[0] for w in wcValue])
# print('-----------------------------------------------')
sw.stop('report word by category')

# feature 선정
sw.start('create feature')
feature = []
weight = []
for wcKey, wcValue in wordByCategory.items():
    # print(wcKey)
    # print(le.transform([wcKey])[0])
    # print(le.inverse_transform(le.transform([wcKey])))
    # print(dict(vectSort)[wcValue[0]])
    feature = feature + [w[0] for w in wcValue]
# print(len(feature))
# print(len(set(feature)))
feature = set(feature)
sw.stop('create feature')

# 구분별 키워드 도식화
# sw.start('view chart word by category')
# for wcKey, wcValue in wordByCategory.items():
#     weight.append([])
#     for f in feature:
#         temp = 0
#         for w in wcValue:
#             if f == w[0]:
#                 temp = w[1]
#                 break
#         weight[len(weight) - 1].append(temp)
# feature = [w for w in range(0, 423)]
# for i, w in enumerate(weight):
#     print(len(feature), len(w))
#     plt.plot(feature, w, color='C' + str(i % 10))
# plt.xlabel('Countries')
# plt.ylabel('Population in million')
# plt.title('Pakistan India Population till 2010')
# plt.show()
# sw.stop('view chart word by category')



print('-----------------------------------------------')
sw.prettyPrint()

