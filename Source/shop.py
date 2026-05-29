class Shop:
    def __init__(self, data):
        self.data = data
        self.boughtItems = []
        self.playerGold = 0
        self.categorys = {}
        self.createCategorys(self.data)
    def createCategorys(self, category, categoryName = "None"):
       for key, value in category.items():
            if isinstance(value, dict):
                self.createCategorys(value, key)
            else:
                if categoryName not in self.categorys:
                    self.categorys[categoryName] = {}
                self.categorys[categoryName][key] = value 

    def openShop(self, playerGold):
        self.playerGold = playerGold
        self.pickCategory()
    def selectFromCategory(self, data):
        index = 1
        for key, value in data.items():
            print(f" {key}: {value} gold ({index})")
            index += 1
        print(f"exit ({index})")
        pickedOption = input("pick an option(" + str(self.playerGold) + " gold remaining): ")

        while not pickedOption.isdigit() and pickedOption < 0 or int(pickedOption) > index:
            pickedOption = input("pick an option(" + str(self.playerGold) + " gold remaining): ")
        if int(pickedOption) == index:
            return

        pickedItem = list(data.keys())[int(pickedOption)-1]
        if self.playerGold >= data[pickedItem]:
            self.playerGold -= data[pickedItem]
            self.boughtItems.append(pickedItem)
            print(f"you bought {pickedItem} for {data[pickedItem]} gold")
        else:
            print("not enough gold")
    def pickCategory(self):
        category_names = self.categorys.keys()
        for index, name in enumerate(category_names):
            print(f"({index}) {name}")
        print(f"({len(category_names)}) exit")
        pickedOption = input("pick an option(" + str(self.playerGold) + " gold remaining): ")

        while not pickedOption.isdigit() and pickedOption < 0 or int(pickedOption) > len(category_names):
            pickedOption = input("pick an option(" + str(self.playerGold) + " gold remaining): ")
        if int(pickedOption) == len(category_names):
            return 
        self.selectFromCategory(self.categorys[ list(category_names)[int(pickedOption)]])
        self.openShop(self.playerGold)