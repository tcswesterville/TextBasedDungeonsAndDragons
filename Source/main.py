import utilities
import races
import classes
import stats2
import StartingGold
import shop
from data import Data
def greeting():
    message = "New Character(choose 1) or load save file(choose 2)"
    choice = ""
    data = Data()
    data.loadData("Source/data.json")
    playerRace = races.Race()
    playerClass = classes.Classes()
    className = playerClass.chooseClass()
    playerStats = stats2.choosingStats()
    playerGold = StartingGold.GoldRoll(playerClass, className)
    playerShop = shop.Shop(data.data["items"])
    playerShop.openShop(playerGold)
    
def main():
    greeting()
if __name__ == "__main__":
    main()
