class Shop:
    def __init__(self, weapons):
        self.weapons = weapons
    def openShop(self, playerGold):
        print("Gold: " + str(playerGold.gold))
        pickedOption = input("pick an option: weapon(1), ")
        if pickedOption == "1":
            self.openWeapons()
        self.openShop(playerGold)
    def openWeapons(self):
        print("weapons: ")
        index = 1
        for key, value in self.weapons.items():
            print(f" {key}: {value} gold ({index})")
            index += 1
        choice = input("pick a weapon: ")
        print(f"you picked {list(self.weapons.keys())[int(choice)-1]}")