#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import os
from time import sleep
from sys import exit

# from elasticsearch import Elasticsearch
# from elasticsearch.exceptions import TransportError
# from elasticsearch.helpers import bulk, streaming_bulk

sleepSecond = 1
domain = 'http://www.sidmool.com'
resultArray = []


# python파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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

dept1Link = dept1Soup.select(
    'div.height2 > div.menu_area li > a'
    )

for dl1 in dept1Link:
    # print('sleep ... {0} second'.format(sleepSecond))
    sleep(sleepSecond)

    # print('dept1 desc : {0} {1}'.format(dl1.text, domain + dl1.get('href')))

    dept2Req = requests.get(domain + dl1.get('href'))
    dept2soup = BeautifulSoup(dept2Req.content.decode('euc-kr','replace'), 'html.parser')
    dept2Link = dept2soup.select(
        'div.product_list > ul > li div.shoplist_title > a'
        )

    for dl2 in dept2Link:
        # print('sleep ... {0} second'.format(sleepSecond))
        sleep(sleepSecond)

        # print('dept2 desc : {0} {1}'.format(dl2.text, domain + dl2.get('href')))

        ingredients = []
        temp = ''
        searchStart = False
        dept3Req = requests.get(domain + dl2.get('href'))
        dept3Soup = BeautifulSoup(dept3Req.content.decode('euc-kr','replace'), 'html.parser')

        dept3Link = dept3Soup.select(
            'div.shop_detail_area tbody'
            )

        detail = ''
        for d in dept3Link:
            detail = d.text

        # dept3Link1 = dept3Soup.select(
        #     'div.shop_detail_area tbody tbody p'
        #     )
        # dept3Link2 = dept3Soup.select(
        #     'div.shop_detail_area tbody p'
        #     )
        # print('dept3Link1 len {0}'.format(len(dept3Link1)))
        # print('dept3Link2 len {0}'.format(len(dept3Link2)))
        # exit()
        # if len(dept3Link2) > 0:
        #     for dl3 in dept3Link2:
        #         # print('{0}'.format(dl3.text))
        #         if searchStart:
        #             temp = temp + dl3.text
        #         # print('dl3 find Ingredients.... {0}'.format(dl3.text.find('Ingredients')))
        #         if dl3.text.find('Ingredients') > -1:
        #             searchStart = True
        # else:
        #     for dl3 in dept3Link1:
        #         # print('{0}'.format(dl3.text))
        #         if searchStart:
        #             temp = temp + dl3.text
        #         # print('dl3 find Ingredients.... {0}'.format(dl3.text.find('Ingredients')))
        #         if dl3.text.find('Ingredients') > -1:
        #             searchStart = True
        
        print('{0}|{1}|{2}'.format(dl1.text, dl2.text, detail.strip()))

        resultArray.append({"igrd":dl1.text, "name":dl2.text, "desc":detail.strip()})
        # break
    
    break


# with open(os.path.join(BASE_DIR, 'result.json'), 'w+') as json_file:
#     json.dump(data, json_file)