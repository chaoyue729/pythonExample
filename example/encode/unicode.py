#-*- coding: utf-8 -*-

# a = u'한글'
# print(a)
# print(a.decode('utf-8'))
# print(a.decode('utf-8').encode('utf-8'))


# s = '한글'
# print(s)
# print(str(s))
# print(str(s).encode('utf-8'))


# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
#
# s = '한글'
# print str(unicode(s))


# 유니코드로 다루기 예제1
hoo = unicode('한글', 'utf-8')
print(hoo)
print(str(hoo.encode('utf-8')))

# 유니코드로 다루기 예제2
bar = '한글'.decode('utf-8')
print(bar.encode('utf-8'))

# 유니코드로 다루기 예제3
foo = u'한글'
print(str(foo.encode('utf-8')))