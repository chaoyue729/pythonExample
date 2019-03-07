'''
https://techreviewtips.blogspot.com/2017/10/04-04-bar.html
https://datastory1.blogspot.com/2017/12/matplotlib.html
https://m.blog.naver.com/PostView.nhn?blogId=samsjang&logNo=220749009417&proxyReferer=https%3A%2F%2Fwww.google.com%2F
'''

import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np
import itertools
from sys import exit

year = [1960, 1970, 1980, 1990, 2000, 2010]
pop_pakistan = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6]
pop_india = [449.48, 553.57, 696.783, 870.133, 1000.4, 1309.1]

n_groups = len(year)
index = np.arange(n_groups)
print(index)
print([n + i for i, n in enumerate(index)])
print([n + i + 1 for i, n in enumerate(index)])
plt.bar([n + i for i, n in enumerate(index)], pop_pakistan, tick_label=year, align='center', color='C1')
plt.bar([n + i + 1 for i, n in enumerate(index)], pop_india, tick_label=year, align='center', color='C9')

plt.xlabel('year')
plt.ylabel('average rainfall (mm)')
plt.title('Weather Bar Chart')
# plt.xlim( -1, n_groups)
# plt.ylim( 0, 400)
plt.show()
exit()


temp = '''
상품>상품불량(보관, 사용) , doc count :  74 , word count :  1641
상품>가격문의 , doc count :  67 , word count :  1313
오류>시스템오류 , doc count :  85 , word count :  1728
해외점>나트랑공항 , doc count :  1 , word count :  35
회원등급/멤버스/카드발급>L.Point 관련 , doc count :  309 , word count :  4437
상품>재고유무 , doc count :  264 , word count :  4545
지불관련>롯데포인트(조회,적립,사용) , doc count :  61 , word count :  1245
상품>상품상이 , doc count :  32 , word count :  668
해외점>괌 공항점 , doc count :  3 , word count :  74
회원등급/멤버스/카드발급>등급확인 , doc count :  431 , word count :  5863
출국정보 및 인도관련>출국정보 오입력(여권번호,편명,날짜) , doc count :  109 , word count :  2289
행사/제휴>공연, 초청 , doc count :  1 , word count :  38
상품>사은품(문의,누락) , doc count :  90 , word count :  1554
면세점이용>구매가능시간 , doc count :  881 , word count :  10065
회원등급/멤버스/카드발급>회원정보변경(주소, 여권번호 등) , doc count :  1440 , word count :  17734
출국정보 및 인도관련>결항 , doc count :  8 , word count :  232
서비스관련>채팅상담전종료 , doc count :  1 , word count :  32
지불관련>실시간계좌이체(공인인증서) , doc count :  1 , word count :  34
지불관련>결제수단변경 , doc count :  32 , word count :  735
출국정보 및 인도관련>상품인도,인도장문의 , doc count :  792 , word count :  11719
오류>채팅상담전종료 , doc count :  2 , word count :  17
면세점이용>세금관련 , doc count :  28 , word count :  560
행사/제휴>세일행사(정기,시즌) , doc count :  76 , word count :  1599
행사/제휴>증정문의(사은품,선불카드,쿠폰 등) , doc count :  636 , word count :  8885
회원등급/멤버스/카드발급>수신동의/비동의(DM,SMS,EMAIL) , doc count :  104 , word count :  1950
null , doc count :  649 , word count :  8791
지불관련>지불수단(통화,상품권,선불카드 등) , doc count :  545 , word count :  7701
면세점이용>전화연결 , doc count :  103 , word count :  1983
면세점이용>액체,경유 관련 , doc count :  116 , word count :  2125
면세점이용>스페셜오더 , doc count :  45 , word count :  919
상품>제조불량(부속품 누락) , doc count :  16 , word count :  273
회원등급/멤버스/카드발급>등급별 발급기준 , doc count :  61 , word count :  1095
서비스관련>직원친절 , doc count :  1 , word count :  35
상품>상품교환 , doc count :  151 , word count :  2850
출국정보 및 인도관련>인도상이 , doc count :  8 , word count :  231
출국정보 및 인도관련>편명문의 , doc count :  318 , word count :  5353
회원등급/멤버스/카드발급>구매실적조회(누락) , doc count :  57 , word count :  1300
상품>입점브랜드 , doc count :  2149 , word count :  15509
지불관련>환율 , doc count :  38 , word count :  598
회원등급/멤버스/카드발급>유효기간 확인 및 연장 , doc count :  14 , word count :  368
행사/제휴>응모행사 , doc count :  73 , word count :  1403
서비스관련>행사불만족 , doc count :  6 , word count :  104
행사/제휴>패밀리콘서트 , doc count :  1 , word count :  25
출국정보 및 인도관련>고객인도 망각 , doc count :  2 , word count :  51
상품>상품A/S , doc count :  115 , word count :  2325
상품>보증서관련 , doc count :  15 , word count :  353
회원등급/멤버스/카드발급>VIP 발급 및 재발급 , doc count :  134 , word count :  2314
면세점이용>구매방법(구비서류, 대리구매) , doc count :  1092 , word count :  11754
면세점이용>채팅상담전종료 , doc count :  3 , word count :  25
회원등급/멤버스/카드발급>VIP할인 및 부가서비스 , doc count :  69 , word count :  1373
가이드>단체예약 , doc count :  113 , word count :  2267
지불관련>영수증발급(현금영수증) , doc count :  23 , word count :  533
상품>상품파손 , doc count :  7 , word count :  148
면세점이용>기타 , doc count :  96 , word count :  2013
회원등급/멤버스/카드발급>등급전환 , doc count :  66 , word count :  1196
면세점이용>영업장(위치,영업시간,전화번호) , doc count :  1866 , word count :  15758
면세점이용>구매(반입)한도 , doc count :  286 , word count :  5159
지불관련>할인쿠폰 관련(쿠폰사용,중복할인) , doc count :  177 , word count :  3010
지불관련>신용카드 관련(구매내역,무이자,할인 등) , doc count :  232 , word count :  4283
행사/제휴>웨딩이벤트 , doc count :  165 , word count :  2803
행사/제휴>제휴행사 , doc count :  451 , word count :  7127
서비스관련>직원불친절(응대미숙,오안내) , doc count :  13 , word count :  130
상품>수량부족 , doc count :  39 , word count :  734
오류>결제오류 , doc count :  81 , word count :  1363
서비스관련>단선(전화끊김,무응답) , doc count :  100 , word count :  624
출국정보 및 인도관련>미운송 , doc count :  2 , word count :  41
면세점이용>시설(주차 등) , doc count :  229 , word count :  3677
지불관련>반품/취소 , doc count :  2386 , word count :  24723
출국정보 및 인도관련>출국정보변경 관련 , doc count :  1428 , word count :  17521
오류>기타오류 , doc count :  103 , word count :  2011
'''
linelist = temp.split('\n')
xn, v1, v2 = [], [], []
for d in linelist:
    if d:
        try:
            t = d.split(' , ')
            xn.append(t[0])
            v1.append(int(t[1].split(':')[1]))
            v2.append(int(t[2].split(':')[1]))
        except:
            print(d)

# npv1 = np.array(v1)
docCountAvg = np.mean(v1)
print(docCountAvg)
npFilterV1 = np.array(list(itertools.filterfalse(lambda x: x < docCountAvg, v1)))
for v in npFilterV1:
    print(v)


v1sort = sorted(v1, key=lambda idx : idx, reverse=False)
v2sort = sorted(v2, key=lambda idx : idx, reverse=False)
npFilterV1 = sorted(npFilterV1, key=lambda idx : idx, reverse=False)
print(npFilterV1)

plt.plot([i for i, n in enumerate(npFilterV1)], npFilterV1, color='C1')
plt.xlabel('Countries')
plt.ylabel('Population in million')
plt.title('Pakistan India Population till 2010')
plt.show()

exit()


n_groups = len(xn)
index = np.arange(n_groups)

plt.bar([n + i for i, n in enumerate(index)], v1, tick_label=xn, align='center', color='C1')
plt.bar([n + i + 1 for i, n in enumerate(index)], v2, tick_label=xn, align='center', color='C9')
plt.xlabel('xn')
plt.ylabel('average rainfall (mm)')
plt.title('Weather Bar Chart')
# plt.xlim( -1, n_groups)
# plt.ylim( 0, 400)
plt.show()