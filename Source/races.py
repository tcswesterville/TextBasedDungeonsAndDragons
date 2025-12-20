import utilities
class Race:
    def __init__(self):
        self.races = {"1": "Human", "2": "Goblin", "3": "Golem"}
        message = "Select race from:"
        for key, value in self.races:
            message += f" {key}: {value}"
        choice = ""
        while not utilities.validate_input(self.races.keys(), choice):
            choice = input(message)