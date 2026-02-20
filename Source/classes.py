import utilities
import stats
class Classes:
    def __init__(self):
        self.classes = {"1": "Barbarian", "2": "Bard", "3": "Cleric", "4": "Druid", "5": "Fighter", "6": "Monk", "7": "Paladin", "8": "Ranger", "9": "Rouge", "10": "Sorcerer", "11": "Warlock", "12": "Wizard"}
        message = "Select class from:"
        for key, value in self.classes.items():
            message += f" {key}: {value}"
        message += ": "
        choice = ""
        while not utilities.validate_input(self.classes.keys(), choice):
            choice = input(message)
        print("Class chosen:")
   
"""
Classes={
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rouge",
    "Sorcerer",
    "Warlock",
    "Wizard",
}
"""