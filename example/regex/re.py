import re

'''
참고사이트
https://wikidocs.net/4308
http://blog.naver.com/PostView.nhn?blogId=rookiemodel&logNo=10139446205
'''

# 자주 사용하는 문자 클래스
# [0-9] 또는 [a-zA-Z] 등은 무척 자주 사용하는 정규 표현식이다. 이렇게 자주 사용하는 정규식들은 별도의 표기법으로 표현할 수 있다. 다음을 기억해 두자.
# \d - 숫자와 매치, [0-9]와 동일한 표현식이다.
# \D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
# \s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
# \S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
# \w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9]와 동일한 표현식이다.
# \W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9]와 동일한 표현식이다.
# 대문자로 사용된 것은 소문자의 반대임을 추측할 수 있을 것이다.


# 반복
# *, +, ? 메타문자는 모두 {m, n} 형태로 고쳐쓰는 것이 가능


# 정규식을 이용한 문자열 검색
# match()	문자열의 처음부터 정규식과 매치되는지 조사한다.
# search()	문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
# findall()	정규식과 매치되는 모든 문자열(substring)을 리스트로 리턴한다
# finditer()	정규식과 매치되는 모든 문자열(substring)을 iterator 객체로 리턴한다
p = re.compile('[a-z]+')
m = p.match('string goes here')
print(m.group())

m = p.search('string goes here')
print(m)

m = p.findall('string goes here')
print(m)


# match 객체
# group()	매치된 문자열을 리턴한다.
# start()	매치된 문자열의 시작 위치를 리턴한다.
# end()	매치된 문자열의 끝 위치를 리턴한다.
# span()	매치된 문자열의 (시작, 끝) 에 해당되는 튜플을 리턴한다.


# 축약
m = re.match('[a-z]{1,3}', 'python is very easy')
print(m.group())


# compile option
# DOTALL(S) - . 이 줄바꿈 문자를 포함하여 모든 문자와 매치할 수 있도록 한다.
# IGNORECASE(I) - 대소문자에 관계없이 매치할 수 있도록 한다.
# MULTILINE(M) - 여러줄과 매치할 수 있도록 한다. (^, $ 메타문자의 사용과 관계가 있는 옵션이다)
# VERBOSE(X) - verbose 모드를 사용할 수 있도록 한다. (정규식을 보기 편하게 만들수 있고 주석등을 사용할 수 있게된다.)
p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)

p = re.compile('[a-z]', re.I)
print(p.match('python'))

p = re.compile("^python\s\w+")
data = """python one
life is too short
python two
you need python
python three"""
print(p.findall(data))


print('---------------------------------------------------------------')
# m = re.search('\(+(\w+?)\)+$', 'abc(123)')
m = re.search('\(+([0-9,]+?)\)+$', '웹프로그래머(4,537)')
# m = re.search('\(+([0-9,]+?)\)+$', 'abcdef(ghi)(1,23)')

if m:
	print(m)
	print(m.group())
	print(m.group(1))
else:
	print(m)

print('---------------------------------------------------------------')
m = re.search('\({1}(.+)\){1}$', 'abcdef(ghi)(123)')
if m:
	print(m)
	print(m.group())
	print(m.group(1))
else:
	print(m)

print('---------------------------------------------------------------')
m = re.search('.*\[(.*)\].*', 'abcdef[123]')
if m:
	print(m)
	print(m.group()) 
	print(m.group(1))
else:
	print(m)

print('---------------------------------------------------------------')
temp = 'MySQL(abc)(250)'
# temp = '데이터마이닝(77)'
m = re.search('^\w+', temp)
if m:
	print(m)
	print(m.group())
	# print(m.group(1))
else:
	print(m)