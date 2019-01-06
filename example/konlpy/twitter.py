# -*- coding: utf-8 -*-

from __future__ import division, unicode_literals
from konlpy.tag import Twitter

_twitter = Twitter()

if __name__ == '__main__':
    print(_twitter.morphs('단독입찰보다 복수입찰의 경우'))
    print(_twitter.nouns('유일하게 항공기 체계 종합개발 경험을 갖고 있는 KAI는'))
    print(_twitter.pos('유일하게 항공기 체계 종합개발 경험을 갖고 있는 KAI는'))
