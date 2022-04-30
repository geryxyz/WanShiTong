# importing the module
import json


class CParser:
    def __init__(self):
        # Opening JSON file
        with open('config.json') as json_file:
            self.data = json.load(json_file)

    def getdata(self, dataname):
        return self.data[dataname]
