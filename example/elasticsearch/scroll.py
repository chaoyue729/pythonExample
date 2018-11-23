#!/usr/bin/env python
#-*- encoding: utf8 -*-

import elasticsearch
import json


es_client = elasticsearch.Elasticsearch("localhost:9200")


docs = es_client.search(index = 'bank_version1',
                       doc_type = 'account',
                       body = {
                           'query': {
                               'match': {
                                   'state': 'NY'
                               }
                           }
                       },
                       scroll = '1m',   # scroll 정보를 1분 유지
                       size = 3) # 한번에 fetch해올 문서를 2개로 지정
                                 # 실제 사용 시에는 1,000 정도로 주면 좋다
scroll_id = docs['_scroll_id']
print('scroll_id : {0}'.format(scroll_id))

num_docs = len(docs['hits']['hits'])
print("{0} docs retrieved".format(num_docs))

while num_docs > 0:
    docs = es_client.scroll(scroll_id = scroll_id,
                            scroll = '1m')

    num_docs = len(docs['hits']['hits'])
    print("{0} docs retrieved".format(num_docs))
