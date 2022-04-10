"""
Ordernél szükségem van:
- mi alapján?
- Növekvő/Csökkenő?
- Kolleckió
https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary

"""
from pydantic.fields import ModelField, List


class Order:
    def __init__(self, key: ModelField):
        pass


class AscendingOrder(Order):
    def __init__(self, key: ModelField):
        super().__init__(key)
        self.key = key

    def order(self, collection: List):
        new_list = sorted(collection, key=lambda d: getattr(d, self.key))
        return new_list


class DescendingOrder(Order):
    def __init__(self, key: ModelField):
        super().__init__(key)
        self.key = key

    def order(self, collection: List):
        new_list = sorted(collection, key=lambda d: getattr(d, self.key), reverse=True)
        return new_list
