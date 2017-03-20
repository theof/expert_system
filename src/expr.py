import fileinput

priority_table = ['(',')', '!', '+', '|', '^']

class Expr():
    def __init__(self, expr):
        level = 0
        for i in range(len(expr)):
            if expr[i] is '(':
                if level is 0:
                    start = i
                level += 1
            elif expr[i] is ')':
                if level > 0:
                    level -= 1
                else:
                    raise Exception('bad letter')
            i += 1


for line in fileinput.input():
    print('out: {}'.format(Expr(line)))
