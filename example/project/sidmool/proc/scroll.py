#!/usr/bin/env python
from __future__ import division, unicode_literals

import elasticsearch
import json
from sys import exit
from collections import Counter
import re
import time
import operator

es_client = elasticsearch.Elasticsearch("localhost:9200")

ingredients = {}

def _format_time(end_time):
    return '{:02d}:{:02d}:{:02d}'.format(end_time // 3600, (end_time % 3600 // 60), end_time % 60)

def parsingDesc(**options):
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
                # print('{0} > {1} - {2}'.format(d['_source']['groupname'], d['_source']['name'], desc))
                ingredients = Counter(ingredients) + desc   # 누적 dict 생성
            else:
                print(desc.count('Ingredients'))

if __name__ == '__main__':
    start_time = time.time()

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
        size = 10)

    scroll_id = docs['_scroll_id']
    num_docs = len(docs['hits']['hits'])

    # print("{0} docs retrieved".format(num_docs))
    # parsingDesc(docs = docs['hits']['hits'])
    # exit()


    while num_docs > 0:
        # print("{0} docs retrieved".format(num_docs))
        parsingDesc(docs = docs['hits']['hits'])

        docs = es_client.scroll(
            scroll_id = scroll_id,
            scroll = '1m')
        num_docs = len(docs['hits']['hits'])

    # print('ingredients : {0}'.format(dict(ingredients)))
    # print(ingredients.items())
    ingredients = [kv for kv in dict(ingredients).items() if int(kv[1]) > 10]
    # print(ingredients)
    # ingredients = sorted(ingredients, key=lambda kv: kv[1])
    # ingredients = sorted(ingredients, key=operator.itemgetter(1))
    ingredients = sorted(ingredients, key=lambda kv: kv[0])
    print(ingredients)
    # print('ingredients : {0}'.format(dict(ingredients)))



    print('finish time : {0}'.format(_format_time(int(time.time() - start_time))))
