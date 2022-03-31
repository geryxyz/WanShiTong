class Filter(object):
    def __init__(self, target: property):
        self.target: property = target

    def is_pass(self, entity) -> bool:
        raise NotImplementedError()
class ContainsFilter(Filter):
    def __init__(self, target, text: str):
        super().__init__(target)
        self._text = text

    def is_pass(self, entity) -> bool:
        return self._text in self.target.fget(entity)