import utilities
import stats
class Race:
    def __init__(self):
        self.races = {"1": "Human", "2": "Goblin", "3": "Goliath", "4": "DragonBorn", "5": "Dwarf", "6": "Gnome", "7": "Aasimar", "8": "Tiefling", "9": "Halfling", "10": "Elf"}
        message = "Select race from:"
        for key, value in self.races.items():
            message += f" {key}: {value}"
        message += ": "
        choice = ""
        while not utilities.validate_input(self.races.keys(), choice):
            choice = input(message)
        if isinstance(RacialStats[self.races[choice]], list):
            RacialStats[self.races[choice]][0](RacialStats[self.races[choice]][1])
        else:
            print("not callable")
    def StatBoosts(options):
        message = "Select choice from:\n"
        for i, option in enumerate (options):
            message += f" {i + 1}: "
            for j in range(len(options[i])): 
                message += f"add {options[i][j]} to one stat" if j == 0 else f", add {options[i][j]} to a different stat"
            message += "\n"
        option = -1
        AcceptableOptions = list(map(str, list(range(1, 1 + len(options)))))
        while not utilities.validate_input(AcceptableOptions, option):
            option = input(message)
        StoredStats = stats.Stats()
        statOptions = ["strength", "dexterity", "charisma", "constitution", "inteligence", "wisdom"]
        for number in options[int(option)-1]:
            AcceptableOptions = list(map(str, list(range(1, 1 + len(statOptions)))))
            message = f"Add {number} to one of the following stats:\n"
            for i, AvailableStat in enumerate(statOptions):
                message += f"{i+1}: {AvailableStat}\n"
            chosenStat = -1
            while not utilities.validate_input(AcceptableOptions, chosenStat):
                chosenStat = input(message)
            StoredStats.setStat(statOptions[int (chosenStat)-1], number)
            del statOptions[int(chosenStat)-1]
        StoredStats.printStats()

RacialStats={
    "Human": {"strength":1, "dexterity":1, "charisma":1, "constitution":1, "intelligence":1, "wisdom":1},
    "Goblin": [Race.StatBoosts, [[2,1],[1,1,1]]],
    "Goliath": [Race.StatBoosts, [[2,1],[1,1,1]]],
    "DragonBorn": {"strength":2, "dexterity":0, "charisma":1, "constitution":0, "intelligence":0, "wisdom":0},
    "Dwarf": {"strength":0, "dexterity":0, "charisma":0, "constitution":2, "intelligence":0, "wisdom":0},
    "Gnome": {"strength":0, "dexterity":0, "charisma":0, "constitution":0, "intelligence":2, "wisdom":0},
    "Aasimar": [Race.StatBoosts, [[2, 2],[1,1,1]]],
    "Tiefling": {"strength":0, "dexterity":0, "charisma":2, "constitution":0, "intelligence":1, "wisdom":0},
    "Halfing": {"strength":0, "dexterity":2, "charisma":0, "constitution":0, "intelligence":0, "wisdom":0},
    "Elf": {"strength":0, "dexterity":2, "charisma":0, "constitution":0, "intelligence":0, "wisdom":0},
}