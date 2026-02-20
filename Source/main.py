import utilities
import races
import classes
def greeting():
    message = "New Character(choose 1) or load save file(choose 2)"
    choice = ""
    playerRace = races.Race()
    playerClass = classes.Classes()
def main():
    greeting()
if __name__ == "__main__":
    main()
