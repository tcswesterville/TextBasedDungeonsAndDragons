class Shop:
    def __init__(self, data):
        self.data = data
        self.boughtItems = []
        self.playerGold = 0
    def openShop(self, playerGold):
        self.playerGold = playerGold
        self.pickCategory(self.data)
        print("Gold: " + str(playerGold.gold))
    def selectFromCategory(self, playerGold):
        print("weapons: ")
        index = 1
        for key, value in self.data.items():
            print(f" {key}: {value} gold ({index})")
            index += 1
        choice = input("pick a weapon: ")
        pickedItem = list(self.data.keys())[int(choice)-1]
        if playerGold.gold >= self.data[pickedItem]:
            playerGold.gold -= self.data[pickedItem]
            self.boughtItems.append(pickedItem)
            print(f"you bought {pickedItem} for {self.data[pickedItem]} gold")
        else:
            print("not enough gold")
    def pickCategory(self, categories):
        for index, name in enumerate(categories.keys(), 1):
            print(f"({index}) {name}")
        pickedOption = input("pick an option: ")

        if pickedOption == "1":
            self.selectFromCategory(playerGold)
        self.openShop(playerGold)