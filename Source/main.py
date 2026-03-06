import utilities
import races
import classes
import stats2
def greeting():
    message = "New Character(choose 1) or load save file(choose 2)"
    choice = ""
    playerRace = races.Race()
    playerClass = classes.Classes()
    playerStats = stats2.choosingStats()
def main():
    greeting()
if __name__ == "__main__":
    main()
