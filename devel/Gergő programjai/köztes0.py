import re


class Datum(object): # singular of data
    @property
    def name(self):
        return 'Aang'


class Filter(object):
    def __init__(self, target: property, expression: str):
        self.target: property = target
        self.expression: str = expression

    def is_pass(self, entity):
        return bool(re.search(self.expression, self.target.fget(entity)))


if __name__ == '__main__':
    datum = Datum()

    print(f'{Datum.name = }')
    print(f'{datum.name = }')
    print(f'{Datum.name.fget(datum) = }')

    name_filter = Filter(Datum.name, r'[Aa]?')
    print(f'{name_filter.is_pass(datum) = }')
