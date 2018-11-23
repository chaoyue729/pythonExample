# -*- coding: utf-8 -*-

from __future__ import division, unicode_literals

import re
import itertools
import networkx
import collections

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from konlpy.tag import Kkma
from konlpy.tag import Twitter

from sys import exit

import time

_kkma = Kkma()
_stopwords = ["아", "휴", "아이구", "아이쿠", "아이고", "어", "나", "우리", "저희", "따라", "의해"]
_text = "꿈을 이루는 케이비 국민 은행 장영순입니다;예;알겠습니다;아 예;안녕하세요;네;는 김포 지점이구요;출금 정지 만원 그렇습니까;네;만원인데네;살아 있어요;잠시만 그 거래 내역 한번 잠깐 확인 좀 할께요;네;;카드 거래 카드가 잘 안 나요;네;전화 드렸거든요;네;잠시만요;네;음;네;일단은 정상적으로 거래 건 맞구요;신고일 확인 후에 반환해 주시겠습니다;알겠습니다;사십시오 네"

if __name__ == '__main__':
    # self.nouns = [noun for noun in _kkma.nouns(self.text) if noun not in _stopwords]
    # print(_kkma.sentences('네, 안녕하세요. 반갑습니다.'))
    print(_kkma.nouns('질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요.'))
