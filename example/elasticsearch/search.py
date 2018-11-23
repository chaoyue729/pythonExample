#!/usr/bin/env python

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
                       })

print(json.dumps(docs, indent = 2))
