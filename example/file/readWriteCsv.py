import os
import re

def readWriteData(testFileDir):
    fileNames = os.listdir(testFileDir)
    for fileIdx, fileName in enumerate(fileNames):
        fullReadFileName = os.path.join(testFileDir, fileName)
        fullWriteFileName = os.path.join(testFileDir, 'M' + fileName)
        # if fileName[:15] == '180901100701140':
        if fileName[:1] == '1':
            print(fullReadFileName, fullWriteFileName)
            fr = open(fullReadFileName, 'r', encoding='utf-8')
            fw = open(fullWriteFileName, 'w', encoding='utf-8')
            while True:
                line = fr.readline()
                if not line: break
                ms = re.findall('[\S^ ]+', line)
                line = '{0}|{1}|{2}|{3}'.format('F' if ms[0] == 'A' else ms[0], int(ms[1]), int(ms[2]), ms[3])
                print(line)
                fw.write(line + '\n')

if __name__ == '__main__':
    
    readWriteData('/Users/whitexozu/dev/project/lgu+/data/lotte_data')