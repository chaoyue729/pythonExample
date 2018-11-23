#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import elasticsearch
from elasticsearch import helpers
import json
import os
from time import sleep
from sys import exit
import csv
import json
import timeit
import logging

# logging level 설정
# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)

# 변수 선언
sleepSecond = 2
domain = 'http://www.sidmool.com'
csvPath = '/Users/whitexozu/dev/pycharm_workspace/pythonExample/example/soup/'

# python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# elasticsearch client
def connectElasticsearch():
    _es = None
    # _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    _es = elasticsearch.Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Connect')
    else:
        print('it could not connect!')
    return _es

def scrapingBeautifulSoup():
    _rs = []

    # HTTP GET Request
    dept1Req = requests.get('http://www.sidmool.com/shop/shopbrand.html?xcode=020&mcode=012&type=Y')
    # HTML 소스 가져오기
    # html = req.text
    # HTTP Header 가져오기
    # header = req.headers
    # HTTP Status 가져오기 (200: 정상)
    # status = req.status_code
    # HTTP가 정상적으로 되었는지 (True/False)
    # is_ok = req.ok

    # BeautifulSoup으로 html소스를 python객체로 변환하기
    # 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
    # 이 글에서는 Python 내장 html.parser를 이용했다.
    # soup = BeautifulSoup(html, 'html.parser')
    dept1Soup = BeautifulSoup(dept1Req.content.decode('euc-kr','replace'), 'html.parser')

    # 제품 전체보기 > 성분라인별 목록
    dept1Linkt = dept1Soup.select('div.menu_area')[1].select('li > a')

    exit()

    for dl1 in dept1Link:
        print('sleep ... {0} second'.format(sleepSecond))
        sleep(sleepSecond)

        print('dept1 desc : {0} {1}'.format(dl1.text, domain + dl1.get('href')))

        dept2Req = requests.get(domain + dl1.get('href'))
        dept2soup = BeautifulSoup(dept2Req.content.decode('euc-kr','replace'), 'html.parser')
        # 성분라인별 이미지 목록
        dept2Link = dept2soup.select(
            'div.product_list > ul > li div.shoplist_title > a'
            )

        for dl2 in dept2Link:
            print('sleep ... {0} second'.format(sleepSecond))
            sleep(sleepSecond)

            print('dept2 desc : {0} {1}'.format(dl2.text, domain + dl2.get('href')))

            ingredients = []
            temp = ''
            searchStart = False
            dept3Req = requests.get(domain + dl2.get('href'))
            dept3Soup = BeautifulSoup(dept3Req.content.decode('euc-kr','replace'), 'html.parser')

            # 상품ID (branduid)
            branduid = dept3Soup.find('input', {'name':'branduid'})['value']

            # 구분코드1 (xcode)
            xcode = dept3Soup.find('input', {'name':'xcode'})['value']

            # 구분코드2 (mcode)
            mcode = dept3Soup.find('input', {'name':'mcode'})['value']

            # price
            price = dept3Soup.find('input', {'name':'price'})['value']

            # 상세내용
            dept3Link = dept3Soup.select(
                'div.shop_detail_area tbody'
                )

            detail = ''
            for d in dept3Link:
                detail = d.text

            # print('{0}|{1}|{2}'.format(dl1.text, dl2.text, detail.strip()))

            # 상품 그룹명 | 상품명 | 상품 상세설명
            _rs.append({'branduid': branduid, 'groupname':dl1.text, 'name':dl2.text, 'xcode':xcode, 'mcode':mcode, 'price':price, 'desc':detail.strip()})

            # break

        # break

    return _rs

if __name__ == '__main__':

    elasticsearchClient = connectElasticsearch()
    resultArray = scrapingBeautifulSoup()


    # for rs in resultArray:
    #     print('>>>> {0}'.format(rs))

    # create csv
    # with open('/Users/whitexozu/dev/pycharm_workspace/pythonExample/example/soup/temp.csv', 'w') as csvfile:
    #     fieldnames = ['groupname', 'name', 'desc']
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='|')
    #     writer.writerow({'groupname':'111', 'name':'222', 'desc':'333'})
    #     writer.writerow({'groupname':'aaaa', 'name':'가가가가', 'desc':'나나나나 나난2'})

    # create json
    # with open(BASE_DIR + '/' + jsonFile, 'w') as fp:
        # fp.write(json.dumps(resultArray, ensure_ascii=False))

    # elasticsearch bulk
    docs = []
    for idx, obj in enumerate(resultArray):
        docs.append({
            '_index': 'sidmool',
            '_type': 'goods',
            '_id': obj.get('branduid', None),
            '_source': {
                'groupname': obj.get('groupname', None),
                'name': obj.get('name', None),
                'xcode': obj.get('xcode', None),
                'mcode': obj.get('mcode', None),
                'price': obj.get('price', None),
                'desc': obj.get('desc', None)
            }
        })

    elasticsearch.helpers.bulk(elasticsearchClient, docs)
