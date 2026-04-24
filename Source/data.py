import json
class Data:
    def __init__(self):
        self.categorys = {
        }
    def loadData(self, fileName):
        with open(fileName, "r") as file:
            #json is treated as a dictonary
            self.data = json.load(file)

            self.getCost(self.data) 
    def getCost(self, category, current_category="unknown"):
        for key, value in category.items():
            if isinstance(value, dict):
                self.getCost(value, key)
            elif isinstance(value, (int, float)):
                if current_category not in self.categorys:
                    self.categorys[current_category] = {}
                self.categorys[current_category][key] = value
    




