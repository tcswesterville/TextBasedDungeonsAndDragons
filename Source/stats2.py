
import utilities
import stats
class choosingStats:
        def __init__ (self):
            AddingStats = [15, 14, 13, 12, 10, 8]
            StoredStats = stats.Stats()

            statOptions = ["strength", "dexterity", "charisma", "constitution", "intelligence", "wisdom"]
            for currentStat in AddingStats:
                addingStats2 = currentStat

                message = ""
                AcceptableOptions = list(map(str, list(range(1, 1 + len(statOptions)))))
                message = f"Choose {currentStat} to add one of the following stats (StatBoost will be added):\n"
                for i, AvailableStat in enumerate(statOptions):
                        message += f"{i+1}: {AvailableStat}\n"
                chosenStat = -1
                
                while not utilities.validate_input(AcceptableOptions, chosenStat):
                        chosenStat = input(message)
                StoredStats.setStat(statOptions[int (chosenStat)-1], currentStat)
                del statOptions[int(chosenStat)-1]
                StoredStats.printStats()
                
