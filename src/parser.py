import fileinput

def es_parse(line):
    line = line.split('#')[0]
    line = ''.join(line.split())

    return line

for line in fileinput.input():
    print('out: {}'.format(es_parse(line)))
