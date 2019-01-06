#!/usr/bin/env python

from __future__ import division, unicode_literals
from konlpy.tag import Twitter
import elasticsearch
import json
from sys import exit

'''
https://datascienceschool.net/view-notebook/70ce46db4ced4a999c6ec349df0f4eb0/

{'Adjective': '형용사',
 'Adverb': '부사',
 'Alpha': '알파벳',
 'Conjunction': '접속사',
 'Determiner': '관형사',
 'Eomi': '어미',
 'Exclamation': '감탄사',
 'Foreign': '외국어, 한자 및 기타기호',
 'Hashtag': '트위터 해쉬태그',
 'Josa': '조사',
 'KoreanParticle': '(ex: ㅋㅋ)',
 'Noun': '명사',
 'Number': '숫자',
 'PreEomi': '선어말어미',
 'Punctuation': '구두점',
 'ScreenName': '트위터 아이디',
 'Suffix': '접미사',
 'Unknown': '미등록어',
 'Verb': '동사'}
'''

if __name__ == '__main__':

    # 형태소분석 사용여부
    morphology = False
    if (morphology):   
        # 품사태깅
        _twitter = Twitter()
        spos = _twitter.pos('기간 만료되지 않은 연금 가지고 계십니까')
        print(spos)

        # 명사추출
        sk = []
        for p in spos:
            # if p[1] == 'Noun' or p[1] == 'Verb':
            if p[1] == 'Noun':
                sk.append(p[0])
        print(sk)

    es_client = elasticsearch.Elasticsearch('localhost:9200')

    sk = ['기간', '만료', '연금', '가지']

    qShould = []
    for k in sk:
        # qShould.append({ 'match_phrase': { 'q_title': k } })
        qShould.append({ 'match': { 'q_title': k } })

    print(qShould)

    # es_client = elasticsearch.Elasticsearch('localhost:9200')

    docs = es_client.search(index = 'lg',
                            doc_type = 'script_correct_data',
                            body = {
                                'from': 0,
                                'size': 3,
                                'sort': ['_score'],
                                'query': {
                                    'bool': {
                                        # 'should': [
                                        #     { 'match_phrase': { 'q_title': '번호이동' } },
                                        #     { 'match_phrase': { 'q_title': '기존' } }
                                        # ]
                                        'should': qShould
                                    }
                                }
                            })

    # print(json.dumps(docs, indent = 2))
    # print(docs)
    for doc in docs['hits']['hits']:
        print('q_title : ', doc['_source']['q_title'])
        print('contents : ', doc['_source']['contents'])
        print('--------------------------------------------')


