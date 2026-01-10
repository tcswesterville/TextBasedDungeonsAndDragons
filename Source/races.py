import utilities
import stats
class Race:
    def __init__(self):
        self.races = {"1": "Human", "2": "Goblin", "3": "Golem"}
        message = "Select race from:"
        for key, value in self.races.items():
            message += f" {key}: {value}"
        message += ": "
        choice = ""
        while not utilities.validate_input(self.races.keys(), choice):
            choice = input(message)
        if isinstance(RacialStats[self.races[choice]], list):
            print("callable")
        else:
            print("not callable")
    def StatBoosts(options):
        message = "Select choice from: "
        for index, option in enumerate (options):
            message += f" {index + 1}: "
            for i in range(len(options)): 
                message += f"add {options[i]} to one stat" if i == 0 else f" and add {options[i]} to a different stat"
            message += "\n"
        option = -1
        while not utilities.validate_input(list(range(1, 1 + len(options))), option):
            option = input()

RacialStats={
    "Human": {"strength":1, "dexterity":1, "charisma":1, "constitution":1, "intelligence":1, "wisdom":1},
    "Goblin": [Race.StatBoosts, [[2,1],[1,1,1]]],
    "Golem": [Race.StatBoosts, [[2,1],[1,1,1]]],
}