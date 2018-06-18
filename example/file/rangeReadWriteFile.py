import time
from sys import exit

if __name__ == "__main__":
    start = time.time()

    readPath = "/Users/whitexozu/dev/example_source/keras/snli_1.0/"
    readFileName = "snli_1.0_train.jsonl"
    writePath = "/Users/whitexozu/dev/pycharm_workspace/pythonExample/example/keras/"
    writeFileName = "snli_1.0_train.jsonl"

    callSentencesFile = open(''.join([readPath, readFileName]), 'r')
    callWordFile = open(''.join([writePath, writeFileName]), 'w')

    for i in range(1, 10000):
        line = callSentencesFile.readline()
        if not line: break
        # print(line)
        # line = line[line.index(' ')+1:]
        # line = line[line.index(' ')+1:]
        callWordFile.write(line)

    callSentencesFile.close()
    callWordFile.close()

    end = time.time() - start
    print(end)