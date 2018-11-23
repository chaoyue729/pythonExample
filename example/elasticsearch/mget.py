#!/usr/bin/env python

import elasticsearch
import json

es_client = elasticsearch.Elasticsearch("localhost:9200")


docs = es_client.mget(index = 'bank_version1', doc_type = 'account', body = {'ids': ['new_id_0', 'new_id_2']})
# print(docs['_source'])

for doc in docs['docs']:
    print('state is {0}'.format(doc['_source']['state']))
