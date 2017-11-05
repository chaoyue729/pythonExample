#-*- coding: utf-8 -*-

import random
import time

if __name__ == "__main__":
    start = time.time()

    path = "/Users/whitexozu/dev/pycharm_workspace/pythonExample/example/createCSVFile/"
    writeFileName = "callMemberCsv1.txt"

    gender = [1, 2]
    age = [20, 30, 40, 50, 60, 70]

    callMemberFile = open(''.join([path, writeFileName]), 'w')

    line = []
    for i in range(1, 1000):
        del line[:]
        line.append('user' + str(i))
        line.append('|')
        line.append(str(gender[random.randrange(0, len(gender))]))
        line.append('|')
        line.append(str(age[random.randrange(0, len(age))]))
        line.append('\n')
        callMemberFile.write("".join(line))

    callMemberFile.close()

    end = time.time() - start
    print("end time : " + str(end))

# user1|1|20|11|1200|70|800|4|1|2|24152152
# user2|1|40|26|1200|80|1100|2|2|2|24152153
# user3|2|50|27|1200|90|200|3|3|2|24152154

# {"locInfoCd", "11", "서울"}
# ,{"locInfoCd", "26", "부산"}
# ,{"locInfoCd", "27", "대구"}
# ,{"locInfoCd", "28", "인천"}
# ,{"locInfoCd", "29", "광주"}
# ,{"locInfoCd", "30", "대전"}
# ,{"locInfoCd", "31", "울산"}
# ,{"locInfoCd", "36", "세종"}
# ,{"locInfoCd", "41", "경기"}
# ,{"locInfoCd", "42", "강원"}
# ,{"locInfoCd", "43", "충북"}
# ,{"locInfoCd", "44", "충남"}
# ,{"locInfoCd", "45", "전북"}
# ,{"locInfoCd", "46", "전남"}
# ,{"locInfoCd", "47", "경북"}
# ,{"locInfoCd", "48", "경남"}
# ,{"locInfoCd", "50", "제주"}
# ,{"locInfoCd", "X", "미상"}
# ,{"locInfoCd", "Y", "미입력"}
# ,{"locInfoCd", "Z", "미등록"}