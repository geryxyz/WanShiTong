"""
example usage:
ÉS: Metszet
VAGY: Unió
NEM: Komplementer
XOR: ?
"""
from typing import List

class Logic():
    def __init__(self):
        pass

class And(Logic):
    def __init__(self):
        super().__init__()

    def analyze(self, set1, set2):
        re = []
        for s in set1:
            if(s in set2):
                re.append(s)
        return re

class Or(Logic):
    def __init__(self):
        super().__init__()

    def analyze(self, set1, set2):
        resulting_list = list(set1)
        resulting_list.extend(x for x in set2 if x not in resulting_list)
        return resulting_list

class Xor(Logic):
    def __init__(self):
        super().__init__()

    def analyze(self, set1: List, set2: List):
        #https://stackoverflow.com/questions/22736641/xor-on-two-lists-in-python
        return list(set(set1).symmetric_difference(set2))

# class Not(Logic):
#     def __init__(self):
#         super().__init__()
#
#     def analyse(self, set1, set2):
#         """
#
#         :param set1: The whole entry
#         :param set2: The filter
#         :return:
#         """
#         r = []
#         for s in set1:
#             if(s not in set2):
#                 r.append(s)
#         return r
