import random
class GoldRoll():
    def __init__(self, playerClass, className):
        self.className = className
        self.classGoldRoll = {
            "Barbarian": 2,
            "Bard": 5,
            "Cleric": 5,
            "Druid": 2,
            "Fighter": 5,
            "Monk": 5,
            "Paladin": 5,
            "Ranger": 5,
            "Rogue": 4,
            "Sorcerer": 3,
            "Warlock": 4,
            "Wizard": 4
        }
        tempGold = 0
        self.gold = 0
        for i in range(self.classGoldRoll[self.className]):
            tempGold = random.randint(1, 4)
            if self.className != "Monk":
                tempGold *= 10
            self.gold += tempGold
        print("starting gold: " + str(self.gold))
 