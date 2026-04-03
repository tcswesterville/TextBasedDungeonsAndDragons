import json
class Data:
    def __init__(self):
        self.data = {

        }
    def loadData(self, fileName):
        with open(fileName, "r") as file:
            self.data = json.load(file)