# -*- coding: utf-8 -*-
# 코드 내부에 한글을 사용가능 하게 해주는 부분입니다.

# 로이터 뉴스 데이터셋 불러오기
from keras.datasets import reuters
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding
from keras.preprocessing import sequence
from keras.utils import np_utils

import numpy
import operator
import pickle
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from sys import exit

TEST_PICKLE = "sequences.test.pickle"
TOKENIZER_PICKLE = "tokenizer.pickle"

# seed 값 설정
seed = 0
numpy.random.seed(seed)
tf.set_random_seed(seed)

# 불러온 데이터를 학습셋, 테스트셋으로 나누기
(X_train, Y_train), (X_test, Y_test) = reuters.load_data(num_words=1000, test_split=0.2)


print ('{}'.format(len(X_test)))
print ('{}'.format(len(X_test[0])))
print ('{}'.format(X_test[0]))
# x_train = sequence.pad_sequences(X_train, maxlen=100)
# print ('{}'.format(x_train))
# print ('{}'.format(x_train[0]))
# print ('----------------')
# print ('{}'.format(Y_test))
# print ('----------------')

# with open(TOKENIZER_PICKLE, 'rb') as fp:
#     tokenizer = pickle.load(fp)
# print('{}'.format(tokenizer.word_index))

# tuple 의 최대값 key
# print(max(tokenizer.word_index.items(), key=operator.itemgetter(1))[0])
# tuple 의 최대값 value
# print(max(tokenizer.word_index.items(), key=operator.itemgetter(1))[1])
# MAX_WORD = max(tokenizer.word_index.items(), key=operator.itemgetter(1))[1] - 1
# exit()

with open(TEST_PICKLE, 'rb') as fp:
    X_test_1, X_test_2, Y_test = pickle.load(fp)
print(X_test_1[0])
# print(X_test_2[0])
# print(Y_test)
# print(len(X_test_1))

# exit()


# x_train, x_test, y_train, y_test = train_test_split(X_test_1, Y_test, test_size=0.3, random_state=seed)

# print ('----------------')
# print('{}'.format(x_train[0]))
# print ('----------------')
# print('{}'.format(x_test[0]))
# print ('----------------')
# print('{}'.format(y_train))
# print ('----------------')
# print('{}'.format(y_test))
# print ('----------------')

# exit()

# 데이터 확인하기
category = numpy.max(Y_train) + 1
print(category, '카테고리')
print(len(X_train), '학습용 뉴스 기사')
print(len(X_test), '테스트용 뉴스 기사')
print(X_train[0])

# 데이터 전처리
x_train = sequence.pad_sequences(X_train, maxlen=100)
x_test = sequence.pad_sequences(X_test, maxlen=100)
y_train = np_utils.to_categorical(Y_train)
y_test = np_utils.to_categorical(Y_test)

# 모델의 설정
model = Sequential()
model.add(Embedding(1000, 100))
model.add(LSTM(100, activation='tanh'))
# model.add(Dense(3, activation='softmax'))
model.add(Dense(46, activation='softmax'))

# 모델의 컴파일
model.compile(loss='categorical_crossentropy',
            optimizer='adam',
            metrics=['accuracy'])

# 모델의 실행
# history = model.fit(x_train, y_train, batch_size=100, epochs=20, validation_data=(x_test, y_test))
history = model.fit(x_train, y_train, batch_size=100, epochs=2, validation_data=(x_test, y_test))

# 테스트 정확도 출력
print("\n Test Accuracy: %.4f" % (model.evaluate(x_test, y_test)[1]))

exit()

# 테스트 셋의 오차
y_vloss = history.history['val_loss']

# 학습셋의 오차
y_loss = history.history['loss']

# 그래프로 표현
x_len = numpy.arange(len(y_loss))
plt.plot(x_len, y_vloss, marker='.', c="red", label='Testset_loss')
plt.plot(x_len, y_loss, marker='.', c="blue", label='Trainset_loss')

# 그래프에 그리드를 주고 레이블을 표시
plt.legend(loc='upper right')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()
