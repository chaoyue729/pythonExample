import time

if __name__ == "__main__":
    start = time.time()

    path = "/Users/whitexozu/dev/pycharm_workspace/pythonExample/example/createCSVFile/"
    readFileName = "callsentenceText1.txt"
    writeFileName = "callWordMod1.txt"

    callSentencesFile = open(''.join([path, readFileName]), 'r')
    callWordFile = open(''.join([path, writeFileName]), 'w')

    while True:
        line = callSentencesFile.readline()
        if not line: break
        line = line[line.index(' ')+1:]
        line = line[line.index(' ')+1:]
        callWordFile.write(line)

    callSentencesFile.close()
    callWordFile.close()

    end = time.time() - start
    print(end)