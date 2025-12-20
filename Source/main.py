import utilities
import races
def greeting():
    message = "New Character(choose 1) or load save file(choose 2)"
    choice = ""
    while not utilities.validate_input({"1", "2"}, choice):
        choice = input(message)
    match choice:
        case "1":
            playerRace = races.Race()
        case "2":
            pass
def main():
    greeting()
if __name__ == "__main__":
    main()
