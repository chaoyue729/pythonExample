'''
https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html
'''

from sklearn.feature_extraction.text import HashingVectorizer
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]
vectorizer = HashingVectorizer(n_features=2**4)
X = vectorizer.fit_transform(corpus)
print(X.shape)
print(X.toarray())
print(vectorizer.build_analyzer())



# decode_error = 'ignore',
# hv = HashingVectorizer(n_features = 2**15)
# twenty = fetch_20newsgroups()
# text = open('lotte_ctgr_data.csv').read()
# text = text.split()
# hv.fit_transform(text)

# hv = HashingVectorizer(n_features = len(arr[0]))
# arr = hv.fit_transform(arr)
# print(len(arr))