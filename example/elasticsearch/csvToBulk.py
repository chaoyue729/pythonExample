#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import elasticsearch
from elasticsearch import helpers

es_client = elasticsearch.Elasticsearch("localhost:9200")

# lg > script_correct_data

# fileName = '/Users/whitexozu/dev/project/lgu+/data/lgscript.min.csv'
fileName = '/Users/whitexozu/dev/project/lgu+/data/lgscript.csv'
f = open(fileName, 'r', encoding='utf-8')
# p = re.compile('\{.*?\}')
p = re.compile('[^ ㄱ-ㅣ가-힣0-9]+')
i = 0
head = []
docs = []
while True:
    line = f.readline().rstrip()
    # print(line)

    if i == 0:
        i += 1
        continue

    if i == 1:
        head = line.split('|')
        head = [h.lower() for h in head]
        i += 1
        continue

    arr = line.split('|')

    if len(arr) != 13:
        print('>>>>>', len(arr))
        print('>>>>>', arr)
        break

    # print(arr)
    # print(arr[5] + '|' + arr[6])
    # print(arr[4])
    # m = p.sub('', arr[4])
    # m = p.findall(arr[6])
    # print(m)

    docs.append({
        '_index': 'lg',
        '_type': 'script_correct_data',
        '_id': arr[0],
        '_source': {
            head[1] : arr[1],
            head[2] : arr[2],
            head[3] : arr[3],
            head[4] : arr[4],
            head[5] : arr[5],
            head[6] : p.sub('', arr[6]),
            head[7] : arr[7],
            head[8] : arr[8],
            head[9] : arr[9],
            head[10] : arr[10],
            head[11] : arr[11],
            head[12] : arr[12]
        }
    })




    # if i > 15: break
    i += 1

    if not line: break
    # print('--------------------------------------------')

print(docs)

elasticsearch.helpers.bulk(es_client, docs)
