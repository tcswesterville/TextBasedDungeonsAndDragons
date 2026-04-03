class Shop:
    def __init__(self, weapons):
        self.weapons = weapons
        self.boughtWeapons = []
    def openShop(self, playerGold):
        print("Gold: " + str(playerGold.gold))
        pickedOption = input("pick an option: weapon(1), ")
        if pickedOption == "1":
            self.openWeapons(playerGold)
        self.openShop(playerGold)
    def openWeapons(self, playerGold):
        print("weapons: ")
        index = 1
        for key, value in self.weapons.items():
            print(f" {key}: {value} gold ({index})")
            index += 1
        choice = input("pick a weapon: ")
        pickedItem = list(self.weapons.keys())[int(choice)-1]
        if playerGold.gold >= self.weapons[pickedItem]:
            playerGold.gold -= self.weapons[pickedItem]
            self.boughtWeapons.append(pickedItem)
            print(f"you bought {pickedItem} for {self.weapons[pickedItem]} gold")
        else:
            print("not enough gold")