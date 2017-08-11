fname="/Users/whitexozu/dev/data/voc/InternalData/201601/InternalData.small.UTF-8"

with open(fname) as f:
    content = f.readlines()
    content = [x.strip() for x in content]

valueSb = []
state = 0
output = []

for line in content:
    if line == '(DQ_DOC':
        state = 1
    elif line == ')DQ_DOC':
        state = 2
    elif line.startswith('(') and line.find(')') == -1 and line != '(DQ_DOC':
        state = 3
    elif line.startswith(')') and line.find('(') == -1 and line != ')DQ_DOC':
        state = 4
        valueSb.append('^')

    if state == 3:
        if not(line.startswith('(')):
            line = line.strip()
            line = line.replace('^', '')
            valueSb.append(line)
    elif state == 2:
        output.append(''.join(valueSb)[:-1])
        valueSb = []

for s in output:
    print(s)