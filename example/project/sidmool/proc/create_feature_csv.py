#!/usr/bin/env python
from __future__ import division, unicode_literals

import elasticsearch
import json
from sys import exit
from collections import Counter
import re
import time
import operator

import pandas as pd
import numpy
import os
import matplotlib.pyplot as plt
import csv

es_client = elasticsearch.Elasticsearch("localhost:9200")

ingredients = {}
usedProd = []

seed = 0
numpy.random.seed(seed)
# tf.set_random_seed(seed)

def _format_time(end_time):
    return '{:02d}:{:02d}:{:02d}'.format(end_time // 3600, (end_time % 3600 // 60), end_time % 60)

def parsingAll(**options):
    global ingredients;
    for d in options['docs']:
        desc = d['_source']['desc']
        if 'Ingredients' in desc:
            if desc.count('Ingredients') == 1:
                desc = desc[desc.find('Ingredients'):]  # 내용중 Ingredients 이후 내영만 사용
                desc = desc.replace('\n', '')  # 뉴라인 치환
                desc = desc.replace('\r', '')  # 뭔지 모르지만 치환
                desc = desc.replace('\xa0', '') # 뭔지 모르지만 치황
                desc = re.sub(' +', ' ', desc)  # 한칸이상의 스페이스를 한칸으로 치환
                desc = desc.replace('Ingredients ', '') # Ingredients 삭제
                desc = Counter([igrds.strip() for igrds in desc.lower().split(',')]) # 배열로 변경 후 Counter 사용하여 dict 로 변경
                ingredients = Counter(ingredients) + desc   # 누적 dict 생성
            else:
                print(desc.count('Ingredients'))

def parsingChoose(**options):
    global usedProd;
    for d in options['docs']:
        desc = d['_source']['desc']
        if 'Ingredients' in desc:
            if desc.count('Ingredients') == 1:
                desc = desc[desc.find('Ingredients'):]  # 내용중 Ingredients 이후 내영만 사용
                desc = desc.replace('\n', '')  # 뉴라인 치환
                desc = desc.replace('\r', '')  # 뭔지 모르지만 치환
                desc = desc.replace('\xa0', '') # 뭔지 모르지만 치황
                desc = re.sub(' +', ' ', desc)  # 한칸이상의 스페이스를 한칸으로 치환
                desc = desc.replace('Ingredients ', '') # Ingredients 삭제
                desc = [igrds.strip() for igrds in desc.lower().split(',')] # 배열로 변경 dict 로 변경
                usedProd.append({'name': d['_source']['name'].strip(), 'desc': desc})
            else:
                print(desc.count('Ingredients'))
        else:
            print('{0} is Ingredients empty!!'.format(d['_source']['name']))
if __name__ == '__main__':
    # elasticsearch search 전체상품
    docs = es_client.search(
        index = 'sidmool',
        doc_type = 'goods',
        body = {
            'query': {
                'bool': {
                    'must_not' : [
                        { "match": { "desc": "" } }
                    ]
                }
            }
        },
        scroll = '1m',
        size = 1000)

    scroll_id = docs['_scroll_id']
    num_docs = len(docs['hits']['hits'])

    while num_docs > 0:
        parsingAll(docs = docs['hits']['hits'])

        docs = es_client.scroll(
            scroll_id = scroll_id,
            scroll = '1m')
        num_docs = len(docs['hits']['hits'])

    # 전체 상품의 성분 사용건수 중 10개 초과만 filter
    ingredients = [kv for kv in dict(ingredients).items() if int(kv[1]) > 10]
    # 성분명으로 소팅
    ingredients = sorted(ingredients, key=lambda kv: kv[0])
    # 성분명만 배열로 생성 (피처 선정)
    ingredients = [k[0] for k in ingredients]

    print('ingredients count {0}'.format(len(ingredients)))

    # 테스트 했던 상품 정보 등록
    goods = [
        ["마다가스카르 병풀 스킨", 1],
        ["마다가스카르 울트라 모이스춰 크림", 1],
        ["닥터트럽  징크크림", 1],
        ["병풀 흔적 수딩바", 1],
        ["아토 수딩 크림", 0],
        ["아크바이™ 로션", 0],
        ["갈라톡사이드 리얼 펩타이드 장벽 수분크림", 0]
    ]
    # elasticsearch query body 생성
    shoulds = []
    for g in goods:
        shoulds.append({ "match_phrase": { "name": g[0] } })

    # elasticsearch search 선택상품
    docs = es_client.search(
        index = 'sidmool',
        doc_type = 'goods',
        body = {
            "query": {
                "bool": {
                    "should": shoulds
                }
            }
        },
        scroll = '1m',
        size = 1000)

    print('goods total count {0}'.format(docs['hits']['total']))

    scroll_id = docs['_scroll_id']
    num_docs = len(docs['hits']['hits'])

    while num_docs > 0:
        parsingChoose(docs = docs['hits']['hits'])

        docs = es_client.scroll(
            scroll_id = scroll_id,
            scroll = '1m')
        num_docs = len(docs['hits']['hits'])

    print('userProd count {0}'.format(len(usedProd)))

    # csv 파일 생성을 위한 데이터 가공, 성분과 상품 데이터로 학습데이터 생성
    features = []
    for good in goods:
        for prod in usedProd:
            # print('{0} - {1}'.format(good[0], prod['name']))
            if prod['name'].count(good[0]) > 0:
                # print(prod['name'].count(good[0]) > 0)
                # print('{0} - {1}'.format(good[0], prod['name']))
                temp = [1 if kwd in prod['desc'] else 0 for kwd in ingredients]
                temp.append(good[1])
                features.append(temp)

    # csv 파일 생성
    f = open('output.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    for feature in features:
        wr.writerow(feature)
    f.close()
