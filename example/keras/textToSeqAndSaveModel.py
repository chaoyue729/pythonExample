# -*- encoding:utf-8 -*-
import os
import json
import pickle
import numpy as np
import operator

from keras.datasets import reuters
from keras.models import Sequential
from keras.layers import Dense, LSTM, Embedding
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint,EarlyStopping

import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from sys import exit
import time
import itertools

seed = 0
np.random.seed(seed)
tf.set_random_seed(seed)
np.random.seed(0)

TRAIN_JOSNL = "snli_1.0_train.jsonl"
SEQUENCES_PICKLE = "sequences.temp.pickle"
TOKENIZER_PICKLE = "tokenizer.temp.pickle"

MAX_NB_WEIGHT = 1000
MAX_NB_WORDS = 100
NB_CLASSES = 3

label2class = {'entailment': 0, 'contradiction': 1, 'neutral': 2}

def _format_time(end_time):
    return '{:02d}:{:02d}:{:02d}'.format(end_time // 3600, (end_time % 3600 // 60), end_time % 60)

def _format_tuple(line):
    row = json.loads(line)
    x = row['sentence1']
    y = label2class[row['gold_label']]
    return x, y

def _create_pickle(debug=True):

    x_test, y_test, X_test = [], [], []

    start_time = time.time()

    with open("snli_1.0_test.jsonl", encoding='utf8') as fp:
        for line in fp:
            try:
                x, y = _format_tuple(line)
                x_test.append(x)
                y_test.append(y)
            except KeyError:
                continue

    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(x_test)

    x_test = tokenizer.texts_to_sequences(x_test)

    # sequences 가중치 중 최대값 이상은 제거
    # X_test = np.array(list(itertools.compress(X_test, [i < MAX_NB_WEIGHT + 1 for i in X_test])))
    # X_test = np.array(list(itertools.ifilter(lambda x: x < 10, X_test)))
    for arr in x_test:
        X_test.append(np.array(list(itertools.filterfalse(lambda x: x > MAX_NB_WEIGHT, arr))))

    # print(X_test)


    # MAX_SEQUENCE_LENGTH 최대값 지정 로직 추가
    MAX_SEQUENCE_LENGTH = max([len(seq) for seq in X_test])

    if debug:
        print('{}'.format(len(X_test[0])))
        print('{}'.format(X_test[0]))
        print("MAX_SEQUENCE_LENGTH: {}".format(MAX_SEQUENCE_LENGTH))
        print("MAX_NB_WORDS: {}".format(MAX_NB_WORDS))

    #
    X_test = sequence.pad_sequences(X_test, maxlen=MAX_NB_WORDS)
    #
    Y_test = np_utils.to_categorical(y_test, NB_CLASSES)


    if os.path.exists(SEQUENCES_PICKLE):
        os.remove(SEQUENCES_PICKLE)
    if os.path.exists(TOKENIZER_PICKLE):
        os.remove(TOKENIZER_PICKLE)

    #
    with open(SEQUENCES_PICKLE, 'wb') as fp:
        pickle.dump((X_test, Y_test), fp)
    #
    with open(TOKENIZER_PICKLE, 'wb') as fp:
        pickle.dump(tokenizer, fp)

    print(_format_time(int(time.time() - start_time)))

    return (X_test, Y_test)

def save_sequences_tokenizer():
    _create_pickle()

def load_sequences():
    with open(SEQUENCES_PICKLE, 'rb') as fp:
        X_test, Y_test = pickle.load(fp)
    return (X_test, Y_test)

def load_tokenizer():
    with open(TOKENIZER_PICKLE, 'rb') as fp:
        tokenizer = pickle.load(fp)
    return tokenizer

def save_model(tp):
    (X_test, Y_test) = tp

    x_train, x_test, y_train, y_test = train_test_split(X_test, Y_test, test_size=0.3, random_state=seed)

    if True:
        print(x_train[26])
        print(x_train[27])
        print(x_train[28])
        print(y_train[27])

    # exit()

    model = Sequential()
    model.add(Embedding(1001, 100))
    model.add(LSTM(100, activation='tanh'))
    model.add(Dense(3, activation='softmax'))

    # 모델의 컴파일
    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    # 모델 저장 폴더 만들기
    MODEL_DIR = './model/'
    if not os.path.exists(MODEL_DIR):
        os.mkdir(MODEL_DIR)

    modelpath = "./model/{epoch:02d}-{val_loss:.4f}.hdf5"

    # 모델 업데이트 및 저장
    checkpointer = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=1, save_best_only=True)

    # 학습 자동 중단 설정
    early_stopping_callback = EarlyStopping(monitor='val_loss', patience=100)

    # 모델의 실행
    history = model.fit(x_train, y_train, validation_split=0.2, batch_size=100, epochs=10, verbose=0, validation_data=(x_test, y_test), callbacks=[early_stopping_callback, checkpointer])

    # y_vloss에 테스트셋으로 실험 결과의 오차 값을 저장
    y_vloss = history.history['val_loss']

    # y_acc 에 학습 셋으로 측정한 정확도의 값을 저장
    y_acc = history.history['acc']

    # x값을 지정하고 정확도를 파란색으로, 오차를 빨간색으로 표시
    x_len = np.arange(len(y_acc))
    plt.plot(x_len, y_vloss, "o", c="red", markersize=3)
    plt.plot(x_len, y_acc, "o", c="blue", markersize=3)

    plt.show()

    # 테스트 정확도 출력
    print("\n Test Accuracy: %.4f" % (model.evaluate(x_test, y_test)[1]))


if __name__ == "__main__":
    # save_sequences_tokenizer()
    # print('>>> {}'.format(save_sequences_tokenizer()))
    # (X_test, Y_test) = load_sequences()
    save_model(load_sequences())


