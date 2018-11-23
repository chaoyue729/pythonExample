#!/usr/bin/env python

import elasticsearch
import logging
import json

def connect_elasticsearch():
    _es = None
    # _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    _es = elasticsearch.Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Yay Connect')
    else:
        print('Awww it could not connect!')
    return _es

if __name__ == '__main__':
    # logging.basicConfig(level=logging.ERROR)
    logging.basicConfig(level=logging.DEBUG)
    es = connect_elasticsearch()

    docs = es.search(
        index = 'bank_version1',
        doc_type = 'account',
        body = {
            'query': {
                'match': {
                   'state': 'NY'
                }
            }
        })

    print(json.dumps(docs, indent = 2))
