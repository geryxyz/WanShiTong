class Filter(object):
    def __init__(self, target: property):
        self.target: property = target

    def is_pass(self, entity) -> bool:
        raise NotImplementedError()
