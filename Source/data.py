import json
class Data:
    def __init__(self):
        self.data = {
        }
    def loadData(self, fileName):
        with open(fileName, "r") as file:
            self.data = json.load(file)

            categories = list(self.data.items.keys())
            for i, category in enumerate(categories):
                print(f"{i+1}: {category}")
            choice = input("pick a category: ")
            selectedCategory = categories[int(choice)-1]
            catagoryData = self.data[selectedCategory]

            if not isinstance(list(catagoryData.values())[0], int):
                subCatagories = list(catagoryData.keys())
                for i, subCatagory in enumerate(subCatagories, 1):
                    print(f"{i}: {subCatagory}")
                subChoice = input("pick a sub category: ")
                selectedSubCatagory = subCatagories[int(subChoice)-1]
                finalItems = catagoryData[selectedSubCatagory]
            else:
                finalItems = catagoryData

                self.categorys = {
                    
                }
                def getCost(category):
                    for item in category:

