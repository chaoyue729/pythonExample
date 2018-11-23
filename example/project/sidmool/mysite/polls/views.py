# -*- coding: utf-8 -*-
from __future__ import division, unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.conf import settings
from .models import Choice, Question

import elasticsearch
import numpy
import re
import itertools
import networkx
import collections
from collections import Counter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import time
import jpype
import json
from konlpy.tag import Kkma
from konlpy.tag import Twitter
from sys import exit
import sys

from keras.models import Sequential, load_model
from keras.layers.core import Dense
from sklearn.preprocessing import LabelEncoder
from keras import backend as K


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

'''
summarize
'''
_kkma = Kkma()
_twitter = Twitter()
_stopwords = ["아", "휴", "아이구", "아이쿠", "아이고", "어"]
_model = None
# _kkma.nouns('질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요.')

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

def _format_time(end_time):
    return '{:02d}:{:02d}:{:02d}'.format(end_time // 3600, (end_time % 3600 // 60), end_time % 60)

def summarize(request):
    try:
        start_time = time.time()

        request_context = request.POST['context']
        request_context_summarize = TextRank(request_context).summarize()
        print('request_context_summarize : {0}'.format(request_context_summarize))
        context = {
            'context': request_context,
            'summarize': request_context_summarize
        }

        print('summarize time : {0}'.format(_format_time(int(time.time() - start_time))))
    except:
        return render(request, 'polls/summarize.html', {
            # 'question': question,
            'error_message': "Exception."
        })
    else:
        return render(request, 'polls/summarize.html', context)

'''
cosmetics
'''
def connect_elasticsearch():
    _es = None
    # _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    _es = elasticsearch.Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Yay Connect')
    else:
        print('Awww it could not connect!')
    return _es

def query_goods_all(**options):
    _docs = None
    _docs = options['es'].search(
        index = 'sidmool',
        doc_type = 'goods',
        body = {
            "size": 1000,
            "query" : {
                "bool": {
                    "must_not" : [
                        { "match": { "desc": "" } }
                    ]
                }
            }
        })
    return _docs

def query_goods_id(**options):
    _docs = None
    _docs = options['es'].search(
        index = 'sidmool',
        doc_type = 'goods',
        body = {
            "query" : {
                "match":{
                    "_id": options['id']
                }
            }
        })
    return _docs

def docs_parsing_all(**options):
    _ingredients = None
    for d in options['docs']:
        desc = d['_source']['desc']
        if 'Ingredients' in desc:
            if desc.count('Ingredients') == 1:
                desc = desc[desc.find('Ingredients'):]  # 내용중 Ingredients 이후 내영만 사용
                desc = desc.replace('\n', '')  # 뉴라인 치환
                desc = desc.replace('\r', '')  # 뭔지 모르지만 치환
                desc = desc.replace('\xa0', '') # 뭔지 모르지만 치환
                desc = re.sub(' +', ' ', desc)  # 한칸이상의 스페이스를 한칸으로 치환
                desc = desc.replace('Ingredients ', '') # Ingredients 삭제
                desc = Counter([igrds.strip() for igrds in desc.lower().split(',')]) # 배열로 변경 후 Counter 사용하여 dict 로 변경
                _ingredients = Counter(_ingredients) + desc   # 누적 dict 생성
            else:
                print('[docs_parsing_all] [ingredients duplication] [name : {0}] [count : {1}] '.format(d['_source']['name'], desc.count('Ingredients')))

    return _ingredients

def docs_parsing_choose(**options):
    _usedProd = []
    for d in options['docs']:
        desc = d['_source']['desc']
        if 'Ingredients' in desc:
            if desc.count('Ingredients') == 1:
                desc = desc[desc.find('Ingredients'):]  # 내용중 Ingredients 이후 내영만 사용
                desc = desc.replace('\n', '')  # 뉴라인 치환
                desc = desc.replace('\r', '')  # 뭔지 모르지만 치환
                desc = desc.replace('\xa0', '') # 뭔지 모르지만 치환
                desc = re.sub(' +', ' ', desc)  # 한칸이상의 스페이스를 한칸으로 치환
                desc = desc.replace('Ingredients ', '') # Ingredients 삭제
                desc = [igrds.strip() for igrds in desc.lower().split(',')] # 배열로 변경 dict 로 변경
                _usedProd.append({'name': d['_source']['name'].strip(), 'desc': desc})
            else:
                print(desc.count('Ingredients'))
        else:
            print('{0} is Ingredients empty!!'.format(d['_source']['name']))

    return _usedProd

def cosmetics(request):
    global _model
    try:
        start_time = time.time()

        print('request : {0}'.format('choose' in request.POST))

        es = connect_elasticsearch()

        request_choose_id = ''
        request_choose_name = ''
        choose_accuracy = None

        # 선택한 상품이 있으면 정보 조회
        if 'choose' in request.POST:

            # elasticsearch 에서 전체 상품 조회후 model 생성시 사용한 feature 정보로 가공
            docs = query_goods_all(es = es)
            ingredients = docs_parsing_all(docs = docs['hits']['hits'])
            ingredients = [kv for kv in dict(ingredients).items() if int(kv[1]) > 10]   # 전체 상품의 성분 사용건수 중 10개 초과만 filter
            ingredients = sorted(ingredients, key=lambda kv: kv[0]) # 성분명으로 소팅
            ingredients = [k[0] for k in ingredients]   # 성분명만 배열로 생성 (피처 선정)
            print('ingredients count {0}'.format(len(ingredients)))

            # 선택 데이터 속성정보 조회
            docs = query_goods_id(es = es, id = request.POST['choose'])
            request_choose_name = docs['hits']['hits'][0]['_source']['name']

            # 선텍 데이터 feature 로 변경
            usedProd = docs_parsing_choose(docs = docs['hits']['hits'])

            # model road 후 test
            X_test = []
            Y_test = []
            for prod in usedProd:
                X_test.append([1 if kwd in prod['desc'] else 0 for kwd in ingredients])
                Y_test.append(1)

            print('model is None : {0}'.format(_model == None))
            print('model is context : {0}'.format(_model))
            if _model == None:
                _model = load_model(settings.BASE_DIR + '/polls/model/35-0.5383.hdf5') # 모델을 새로 불러옴

            print('load_model is context : {0}'.format(_model))

            # print(_model.evaluate(numpy.array(X_test), numpy.array(Y_test), verbose=0))
            choose_accuracy = str('%.4f' % _model.evaluate(numpy.array(X_test), numpy.array(Y_test), verbose=0)[1])
            # K.clear_session()   # tensorflow session clear

        # 전체 상품 정보 조회
        docs = es.search(
            index = 'sidmool',
            doc_type = 'goods',
            body = {
                "query": { "match_all": {} },
                "size" : 400,
                "_source": ["groupname", "name"]
            })

        # respose 데이터 셋팅
        context = {
            'choose_id': request_choose_id, # 선택한 화장품 id
            'choose_name': request_choose_name, # 선택한 화장품 명
            'cosmetics_all' : [d['_source'] for d in docs['hits']['hits']],  # 전체 화장품 정보
            'cosmetics_all_to_json' : json.dumps([{'value':d['_id'], 'name':d['_source']['name']} for d in docs['hits']['hits']]), # 전체 화장품의 id와 name 을 json 형식으로 변환, select를 만들기 위해
            'choose_accuracy' : choose_accuracy  # 정확성
        }
        print('summarize time : {0}'.format(_format_time(int(time.time() - start_time))))
    except Exception as err:
        print('error_message : {0}'.format(err))
        print('error_message : {0}'.format(sys.exc_info()[0]))

        return render(request, 'polls/cosmetics.html', {
            # 'question': question,
            'error_message': str(err)
        })
    else:
        return render(request, 'polls/cosmetics.html', context)
