#-*- coding: utf-8 -*-

a = b = c = d = 0
print(a)
a += 1
print(a)
print(b)

a = [ "AAA", "BBB", "CCC" ]
b = [ 1 ,2 ,3, 435, 643, 525]

print("{0}".format(len(a)))
print(a[0])
print(1 not in b)

str1 = ','.join(str(e) for e in b)
print(str1)
# print(a.index("ddd"))

# 맨 앞에 새 요소 추가
a.insert(0, "똠방각하")
print(" ".join(a))
# 출력 결과: 똠방각하 AAA BBB CCC



# 맨 뒤에 새 요소 추가
a.append("ZZZ")
print(" ".join(a))
# 출력 결과: 똠방각하 AAA BBB CCC ZZZ



# 맨 앞의 요소 제거
a.pop(0)
print(" ".join(a))
# 출력 결과: AAA BBB CCC ZZZ



# 맨 마지막 요소 제거
s = a.pop()
print(" ".join(a))
# 출력 결과: AAA BBB CCC


# 그리고 pop 은 말 그대로 "뽑아내는 것"이기 때문에,
# 요소를 제거한 후, 그 요소를 반환합니다.
print(s)
# 출력 결과: ZZZ