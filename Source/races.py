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
    "Golem": [Race.StatBoosts, [[2,1],[1,1,1]]],
}