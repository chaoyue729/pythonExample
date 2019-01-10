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
_stopwords = ["아", "휴", "아이구", "아이쿠", "아이고", "어", "나", "우리", "저희", "따라", "의해", "을", "를", "에", "의", "가", "으로", "로", "에게", "뿐이다", "의거하여", "근거하여", "입각하여", "기준으로", "예하면", "예를", "들면", "들자면", "저", "소인", "소생", "저희", "지말고", "하지마", "하지마라", "다른", "물론", "또한", "그리고", "비길수", "없다", "해서는", "안된다", "뿐만", "아니라", "만이", "아니다", "만은", "아니다", "막론하고", "관계없이", "그치지", "않다", "그러나", "그런데", "하지만", "든간에", "논하지", "않다", "따지지", "않다", "설사", "비록", "더라도", "아니면", "만", "못하다", "하는", "편이", "낫다", "불문하고", "향하여", "향해서", "향하다", "쪽으로", "틈타", "이용하여", "타다", "오르다", "제외하고", "이", "외에", "이", "밖에", "하여야", "비로소", "한다면", "몰라도", "외에도", "이곳", "여기", "부터", "기점으로", "따라서", "할", "생각이다", "하려고하다", "이리하여", "그리하여", "그렇게", "함으로써", "하지만", "일때", "할때", "앞에서", "중에서", "보는데서", "으로써", "로써", "까지", "해야한다", "일것이다", "반드시", "할줄알다", "할수있다", "할수있어", "임에", "틀림없다", "한다면", "등", "등등", "제", "겨우", "단지", "다만", "할뿐", "딩동", "댕그", "대해서", "대하여", "대하면", "훨씬", "얼마나", "얼마만큼", "얼마큼", "남짓", "여", "얼마간", "약간", "다소", "좀", "조금", "다수", "몇", "얼마", "지만", "하물며", "또한", "그러나", "그렇지만", "하지만", "이외에도", "대해", "말하자면", "뿐이다", "다음에", "반대로", "반대로", "말하자면", "이와", "반대로", "바꾸어서", "말하면", "바꾸어서", "한다면", "만약", "그렇지않으면", "까악", "툭", "딱", "삐걱거리다", "보드득", "비걱거리다", "꽈당", "응당", "해야한다", "에", "가서", "각", "각각", "여러분", "각종", "각자", "제각기", "하도록하다", "와", "과", "그러므로", "그래서", "고로", "한", "까닭에", "하기", "때문에", "거니와", "이지만", "대하여", "관하여", "관한", "과연", "실로", "아니나다를가", "생각한대로", "진짜로", "한적이있다", "하곤하였다", "하", "하하", "허허", "아하", "거바", "와", "오", "왜", "어째서", "무엇때문에", "어찌", "하겠는가", "무슨", "어디", "어느곳", "더군다나", "하물며", "더욱이는", "어느때", "언제", "야", "이봐", "어이", "여보시오", "흐흐", "흥", "휴", "헉헉", "헐떡헐떡", "영차", "여차", "어기여차", "끙끙", "아야", "앗", "아야", "콸콸", "졸졸", "좍좍", "뚝뚝", "주룩주룩", "솨", "우르르", "그래도", "또", "그리고", "바꾸어말하면", "바꾸어말하자면", "혹은", "혹시", "답다", "및", "그에", "따르는", "때가", "되어", "즉", "지든지", "설령", "가령", "하더라도", "할지라도", "일지라도", "지든지", "몇", "거의", "하마터면", "인젠", "이젠", "된바에야", "된이상", "만큼 어찌됏든", "그위에", "게다가", "점에서", "보아", "비추어", "보아", "고려하면", "하게될것이다", "일것이다", "비교적", "좀", "보다더", "비하면", "시키다", "하게하다", "할만하다", "의해서", "연이서", "이어서", "잇따라", "뒤따라", "뒤이어", "결국", "의지하여", "기대여", "통하여", "자마자", "더욱더", "불구하고", "얼마든지", "마음대로", "주저하지", "않고", "곧", "즉시", "바로", "당장", "하자마자", "밖에", "안된다", "하면된다", "그래", "그렇지", "요컨대", "다시", "말하자면", "바꿔", "말하면", "즉", "구체적으로", "말하자면", "시작하여", "시초에", "이상", "허", "헉", "허걱", "바와같이", "해도좋다", "해도된다", "게다가", "더구나", "하물며", "와르르", "팍", "퍽", "펄렁", "동안", "이래", "하고있었다", "이었다", "에서", "로부터", "까지", "예하면", "했어요", "해요", "함께", "같이", "더불어", "마저", "마저도", "양자", "모두", "습니다", "가까스로", "하려고하다", "즈음하여", "다른", "다른", "방면으로", "해봐요", "습니까", "했어요", "말할것도", "없고", "무릎쓰고", "개의치않고", "하는것만", "못하다", "하는것이", "낫다", "매", "매번", "들", "모", "어느것", "어느", "로써", "갖고말하자면", "어디", "어느쪽", "어느것", "어느해", "어느", "년도", "라", "해도", "언젠가", "어떤것", "어느것", "저기", "저쪽", "저것", "그때", "그럼", "그러면", "요만한걸", "그래", "그때", "저것만큼", "그저", "이르기까지", "할", "줄", "안다", "할", "힘이", "있다", "너", "너희", "당신", "어찌", "설마", "차라리", "할지언정", "할지라도", "할망정", "할지언정", "구토하다", "게우다", "토하다", "메쓰겁다", "옆사람", "퉤", "쳇", "의거하여", "근거하여", "의해", "따라", "힘입어", "그", "다음", "버금", "두번째로", "기타", "첫번째로", "나머지는", "그중에서", "견지에서", "형식으로", "쓰여", "입장에서", "위해서", "단지", "의해되다", "하도록시키다", "뿐만아니라", "반대로", "전후", "전자", "앞의것", "잠시", "잠깐", "하면서", "그렇지만", "다음에", "그러한즉", "그런즉", "남들", "아무거나", "어찌하든지", "같다", "비슷하다", "예컨대", "이럴정도로", "어떻게", "만약", "만일", "위에서", "서술한바와같이", "인", "듯하다", "하지", "않는다면", "만약에", "무엇", "무슨", "어느", "어떤", "아래윗", "조차", "한데", "그럼에도", "불구하고", "여전히", "심지어", "까지도", "조차도", "하지", "않도록", "않기", "위하여", "때", "시각", "무렵", "시간", "동안", "어때", "어떠한", "하여금", "네", "예", "우선", "누구", "누가", "알겠는가", "아무도", "줄은모른다", "줄은", "몰랏다", "하는", "김에", "겸사겸사", "하는바", "그런", "까닭에", "한", "이유는", "그러니", "그러니까", "때문에", "그", "너희", "그들", "너희들", "타인", "것", "것들", "너", "위하여", "공동으로", "동시에", "하기", "위하여", "어찌하여", "무엇때문에", "붕붕", "윙윙", "나", "우리", "엉엉", "휘익", "윙윙", "오호", "아하", "어쨋든", "만", "못하다    하기보다는", "차라리", "하는", "편이", "낫다", "흐흐", "놀라다", "상대적으로", "말하자면", "마치", "아니라면", "쉿", "그렇지", "않으면", "그렇지", "않다면", "안", "그러면", "아니었다면", "하든지", "아니면", "이라면", "좋아", "알았어", "하는것도", "그만이다", "어쩔수", "없다", "하나", "일", "일반적으로", "일단", "한켠으로는", "오자마자", "이렇게되면", "이와같다면", "전부", "한마디", "한항목", "근거로", "하기에", "아울러", "하지", "않도록", "않기", "위해서", "이르기까지", "이", "되다", "로", "인하여", "까닭으로", "이유만으로", "이로", "인하여", "그래서", "이", "때문에", "그러므로", "그런", "까닭에", "알", "수", "있다", "결론을", "낼", "수", "있다", "으로", "인하여", "있다", "어떤것", "관계가", "있다", "관련이", "있다", "연관되다", "어떤것들", "에", "대해", "이리하여", "그리하여", "여부", "하기보다는", "하느니", "하면", "할수록", "운운", "이러이러하다", "하구나", "하도다", "다시말하면", "다음으로", "에", "있다", "에", "달려", "있다", "우리", "우리들", "오히려", "하기는한데", "어떻게", "어떻해", "어찌됏어", "어때", "어째서", "본대로", "자", "이", "이쪽", "여기", "이것", "이번", "이렇게말하자면", "이런", "이러한", "이와", "같은", "요만큼", "요만한", "것", "얼마", "안", "되는", "것", "이만큼", "이", "정도의", "이렇게", "많은", "것", "이와", "같다", "이때", "이렇구나", "것과", "같이", "끼익", "삐걱", "따위", "와", "같은", "사람들", "부류의", "사람들", "왜냐하면", "중의하나", "오직", "오로지", "에", "한하다", "하기만", "하면", "도착하다", "까지", "미치다", "도달하다", "정도에", "이르다", "할", "지경이다", "결과에", "이르다", "관해서는", "여러분", "하고", "있다", "한", "후", "혼자", "자기", "자기집", "자신", "우에", "종합한것과같이", "총적으로", "보면", "총적으로", "말하면", "총적으로", "대로", "하다", "으로서", "참", "그만이다", "할", "따름이다", "쿵", "탕탕", "쾅쾅", "둥둥", "봐", "봐라", "아이야", "아니", "와아", "응", "아이", "참나", "년", "월", "일", "령", "영", "일", "이", "삼", "사", "오", "육", "륙", "칠", "팔", "구", "이천육", "이천칠", "이천팔", "이천구", "하나", "둘", "셋", "넷", "다섯", "여섯", "일곱", "여덟", "아홉", "령", "영"]


def xplit(value):
    return re.split('(?:(?<=[^0-9])\.|\n|(?:\;))', value)


def get_sentences(text):
    candidates = xplit(text.strip())
    sentences = []
    index = 0
    for candidate in candidates:
        while len(candidate) and (candidate[-1] == '.' or candidate[-1] == ' '):
            candidate = candidate.strip(' ').strip('.')
        if len(candidate):
            sentences.append(Sentence(candidate + '.', index))
            index += 1

    return sentences


def build_graph(sentences):
    graph = networkx.Graph()
    graph.add_nodes_from(sentences)
    pairs = list(itertools.combinations(sentences, 2))
    for pair in pairs:
        weight = co_occurrence(pair[0], pair[1])
        if weight:
            graph.add_edge(pair[0], pair[1], weight=weight)
    return graph


def co_occurrence(sentence1, sentence2):
    p = sum((sentence1.bow & sentence2.bow).values())
    q = sum((sentence1.bow | sentence2.bow).values())
    return p / q if q else 0


class Sentence:

    def __init__(self, text, index=0):
        self.index = index
        self.text = text
        self.nouns = [noun for noun in _kkma.nouns(self.text) if noun not in _stopwords]
        self.bow = collections.Counter(self.nouns)

    def __unicode__(self):
        return self.text

    def __str__(self):
        return str(self.index)

    def __repr__(self):
        print('__repr__ {0} : '.format(self.text))
        try:
            return self.text.encode('utf-8')
        except:
            return self.text

    def __eq__(self, another):
        return hasattr(another, 'index') and self.index == another.index

    def __hash__(self):
        return self.index

class TextRank:

    def __init__(self, text):
        self.sentences = get_sentences(text)
        self.graph = build_graph(self.sentences)
        self.pagerank = networkx.pagerank(self.graph, weight='weight')
        self.reordered = sorted(self.pagerank, key=self.pagerank.get, reverse=True)
        self.nouns = []
        for sentence in self.sentences:
            self.nouns += sentence.nouns
        self.bow = collections.Counter(self.nouns)

    def summarize(self, count=3):
        if not hasattr(self, 'reordered'):
            return ""
        candidates = self.reordered[:count]
        candidates = sorted(candidates, key=lambda sentence: sentence.index)
        return '\n'.join([candidate.text for candidate in candidates])

def _format_time(end_time):
    return '{:02d}:{:02d}:{:02d}'.format(end_time // 3600, (end_time % 3600 // 60), end_time % 60)


if __name__ == '__main__':


    # return if test
    # for v in itertools.combinations([1,2,0,-1,-2,0], 2):
    #     print('{0}, {1}, {2}'.format(v[0], v[1], v[0] / v[1] if v[1] else 0))
    # exit()

    text = "꿈을 이루는 케이비 국민 은행 장영순입니다;예;알겠습니다;아 예;안녕하세요;네;는 김포 지점이구요;출금 정지 만원 그렇습니까;네;만원인데네;살아 있어요;잠시만 그 거래 내역 한번 잠깐 확인 좀 할께요;네;;카드 거래 카드가 잘 안 나요;네;전화 드렸거든요;네;잠시만요;네;음;네;일단은 정상적으로 거래 건 맞구요;신고일 확인 후에 반환해 주시겠습니다;알겠습니다;사십시오 네"
    sentences = get_sentences(text)
    # graph = build_graph(sentences)
    # networkx.draw(graph)
    # plt.show()
    # pagerank = networkx.pagerank(graph, weight='weight')
    # reordered = sorted(pagerank, key=pagerank.get, reverse=True)
    # for v in reordered:
    #     print(v.text)

    # TextRank test
    # text = "트위터, \"정보당국에 데이터 분석자료 팔지 않겠다\". 트위터가 수많은 트윗을 분석해 정보를 판매하는 서비스를 미국 정보당국에는 제공하지 않기로 했다. 월스트리트저널은 미국 정보당국 관계자 등을 인용해 데이터마이너(Dataminer)가 정보당국에 대한 서비스는 중단하기로 했다고 9일(현지시간) 보도했다. 트위터가 5% 지분을 가진 데이터마이너는 소셜미디어상 자료를 분석해 고객이 의사결정을 하도록 정보를 제공하는 기업이다. 트위터에 올라오는 트윗에 실시간으로 접근해 분석한 자료를 고객에게 팔 수 있는 독점권을 갖고 있다. 정보당국은 이 회사로부터 구매한 자료로 테러나 정치적 불안정 등과 관련된 정보를 획득했다. 이 회사가 정보당국에 서비스를 판매하지 않기로 한 것은 트위터의 결정인 것으로 알려졌다. 데이터마이너 경영진은 최근 “트위터가 정보당국에 서비스하는 것을 원치 않는다”고 밝혔다고 이 신문은 전했다. 트위터도 성명을 내고 “정보당국 감시용으로 데이터를 팔지 않는 것은 트위터의 오래된 정책”이라며 “트위터 자료는 대체로 공개적이고 미국 정부도 다른 사용자처럼 공개된 어카운트를 살펴볼 수 있다”고 해명했다. 그러나 이는 이 회사가 2년 동안 정보당국에 서비스를 제공해 온 데 대해서는 타당한 설명이 되지 않는다. 트위터의 이번 결정은 미국의 정보기술(IT)기업과 정보당국 간 갈등의 연장 선상에서 이뤄진 것으로 여겨지고 있다. IT기업은 이용자 프라이버시에 무게 중심을 두는 데 비해 정보당국은 공공안전을 우선시해 차이가 있었다. 특히 애플은 캘리포니아 주 샌버너디노 총격범의 아이폰에 저장된 정보를 보겠다며 데이터 잠금장치 해제를 요구하는 미 연방수사국(FBI)과 소송까지 진행했다. 정보당국 고위 관계자도 “트위터가 정보당국과 너무 가까워 보이는 것을 우려하는 것 같다”고 말했다. 데이터마이너는 금융기관이나, 언론사 등 정보당국을 제외한 고객에 대한 서비스는 계속할 계획이다."
    # print(TextRank(text).summarize())
    # exit()

    # strip, for in if test
    # stopwords = ['꿈', '케이', '케이비', '비']
    # arr = ['꿈을 이루는 케이비 국민 은행 장영순입니다 ', '예', '알겠습니다.', '아 예', '안녕하세요', '네', '는 김포 지점이구요', '출금 정지 만원 그렇습니까', '네', '만원인데네', '살아 있어요', '잠시만 그 거래 내역 한번 잠깐 확인 좀 할께요', '네', '', '카드 거래 카드가 잘 안 나요', '네', '전화 드렸거든요', '네', '잠시만요', '네', '음', '네', '일단은 정상적으로 거래 건 맞구요', '신고일 확인 후에 반환해 주시겠습니다', '알겠습니다', '사십시오 네']
    # for s in arr:
        # print('>{0}< : >{1}< : >{2}<'.format(s, s.strip(' '), s.strip('.')))
        # for noun in _kkma.nouns(a) if noun not in _stopwords:
    # exit()
    # start_time = time.time()
    # print([noun for noun in _kkma.nouns(arr[0]) if noun not in stopwords])
    # print(_format_time(int(time.time() - start_time)))
    # exit()

    # kkma.nouns 퍼포먼스 테스트
    # start_time = time.time()
    # print([noun for noun in _kkma.nouns(arr[0]) if noun not in stopwords])
    # print(_format_time(int(time.time() - start_time)))
    #
    # start_time = time.time()
    # print([noun for noun in _kkma.nouns(arr[1]) if noun not in stopwords])
    # print(_format_time(int(time.time() - start_time)))
    #
    # start_time = time.time()
    # print([noun for noun in _kkma.nouns(arr[0]) if noun not in stopwords])
    # print(_format_time(int(time.time() - start_time)))
    #
    # start_time = time.time()
    # print([noun for noun in _kkma.nouns(arr[11]) if noun not in stopwords])
    # print(_format_time(int(time.time() - start_time)))
    #
    # exit()

    # jaccard index test
    # _twitter = Twitter()
    # start_time = time.time()
    # bow1 = collections.Counter(_twitter.nouns("미쿠 미쿠 하게 해줄게"))
    # bow2 = collections.Counter(_twitter.nouns("미쿠 머리카락 맛있겠다"))
    # j_index = sum((bow1 & bow2).values()) / sum((bow1 | bow2).values())
    # print(j_index)
    # print(_format_time(int(time.time() - start_time)))
    #
    # print(bow1)
    # print(bow2)
    # print(bow1 | bow2)
    # print((bow1 | bow2).values())
    # print(sum((bow1 | bow2).values()))
    #
    # exit()