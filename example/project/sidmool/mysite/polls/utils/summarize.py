import re
import itertools
import networkx
import collections
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import jpype
import time
from konlpy.tag import Kkma
from konlpy.tag import Twitter

_kkma = Kkma()
# _twitter = Twitter()
_stopwords = ["아", "휴", "아이구", "아이쿠", "아이고", "어"]

def _format_time(end_time):
    return '{:02d}:{:02d}:{:02d}'.format(end_time // 3600, (end_time % 3600 // 60), end_time % 60)

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
        jpype.attachThreadToJVM()
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

if __name__ == '__main__':
    context = "자유한국당, 바른미래당, 민주평화당, 정의당 등 야 4당이 20일 공공기관 채용비리에 대한 국정조사를 공식 요구했다. 특히 조명래 환경부 장관 임명에 대한 문재인 대통령의 사과, 조국 민정수석 경질, 채용비리 국정조사를 요구하며 국회 일정을 거부 중인 한국당과 바른미래당은 국정조사만 수용되면 국회를 정상화하겠다고 했다. 여당인 더불어민주당은 당내 여론을 수렴해 야당이 협상안으로 내놓은 ‘국정조사 실시-국회 정상화’ 방안의 수용 여부를 결정키로 했다. 이에 따라 민주당의 결정이 예산국회 정상화의 분수령이 될 것으로 보인다. 민주당 홍영표, 한국당 김성태, 바른미래당 김관영, 평화당 장병완, 정의당 윤소하 원내대표 등 여야 5당 원내대표는 이날 국회에서 문희상 국회의장 주재로 회동을 갖고 국회 정상화 방안을 논의했다. 야 4당은 서울교통공사의 고용세습 의혹과 강원랜드 채용비리 의혹을 함께 조사하는 국정조사 수용을 여당에 요구했다. 한국당, 바른미래당은 여당이 국정조사 요구를 수용하면 국회를 정상화하겠다는 뜻을 전했다. 문 의장도 야 4당의 요구가 있는 만큼 조속한 국회 정상화를 위해 여야가 합의해야 한다고 종용한 것으로 알려졌다. 예산안 심사를 앞두고 멈춰 선 국회를 정상화하기 위해 여당이 대승적으로 국정조사를 수용할 필요가 있다는 뜻을 에둘러 전달한 것이라는 해석이 나온다."

    print(TextRank(context).summarize())
