import fileinput
from expr import Expr

class Parsed():
    def __init__(self, line):
        self._parse(line)

    def _parse(self, line):
        raise NotImplementedError

    @classmethod
    def check(cls, line):
        return cls.symbol in line

class ParsedQuery(Parsed):
    symbol = '?'

    def _parse(self, line):
        self.queries = []
        for letter in line[1:]:
            if letter.isupper():
                self.queries += letter
            else:
                raise Exception('bad letter {}'.format(letter))

    def __str__(self):
        return 'Queries: {}'.format(self.queries)

    @classmethod
    def check(cls, line):
        return cls.symbol is line[0]

class ParsedEquivalence(Parsed):
    symbol = '<=>'

    def _parse(self, line):
        array = line.split('<=>')
        if len(array) != 2:
            raise Exception('syntax err')
        else:
            try:
                self.lmember = Expr(array[0])
                self.rmember = Expr(array[1])
            except:
                raise Exception('expected expressions')

    def __str__(self):
        return 'Equivalence: {} <=> {}'.format(self.lmember, self.rmember)


class ParsedImplies(Parsed):
    symbol = '=>'

    def _parse(self, line):
        array = line.split('=>')
        if len(array) != 2:
            raise Exception('syntax err')
        else:
            try:
                self.lmember = Expr(array[0])
                self.rmember = Expr(array[1])
            except:
                raise Exception('expected expressions')

    def __str__(self):
        return 'Implication: {} => {}'.format(self.lmember, self.rmember)


class ParsedFact(Parsed): 
    symbol = '='

    def _parse(self, line):
        self.facts = []
        for letter in line[1:]:
            if letter.isupper():
                self.facts += letter
            else:
                raise Exception('bad letter {}'.format(letter))

    def __str__(self):
        return 'Facts: {}'.format(self.facts)

    @classmethod
    def check(cls, line):
        return cls.symbol is line[0]

priority_table = [
            ParsedQuery,
            ParsedFact,
            ParsedEquivalence,
            ParsedImplies,
            ]


def es_parse(line):
    line = ''.join(line.split())
    line = ''.join(line.split('#')[0])
    try:
        for rule in priority_table:
            if rule.check(line):
                return rule(line)
        raise Exception(line)
    except:
        raise Exception('bad op')

for line in fileinput.input():
    print('out: {}'.format(es_parse(line)))
