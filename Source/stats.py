import random
class Stats():
    def __init__ (self, strength=0, dexterity=0, charisma=0, constitution=0, intelligence=0, wisdom=0):
        self.stats = {
            "strength": strength,
            "dexterity": dexterity,
            "charisma": charisma,
            "constitution": constitution,
            "intelligence": intelligence,
            "wisdom": wisdom
        }
    SkillMappings = {
        "Athletics": "strength", 
        "Acrobatics": "dexterity",
        "Sleight Of Hand": "dexterity",
        "Stealth": "dexterity",
        "Arcana": "intelligence",
        "History": "intelligence",
        "Investigation": "intelligence",
        "Nature": "intelligence",
        "Religion": "inteligence",
        "Animal Handeling": "wisdom",
        "Insight": "wisdom",
        "Medicine": "wisdom",
        "Perception": "wisdom",
        "Survival": "wisdom",
        "deception": "charisma",
        "Intimidation": "charisma",
        "Performance": "charisma",
        "Persuasion": "charisma"
    }
    def setStat(self, stat, value):
        self.stats[stat] = value
    def GetStats(self):
        return self.stats
    def printStats(self):
        print("stats:\n")
        for key, value in self.stats.items():
            print(f"{key}: {value}\n")
    def SkillModifier(self, stat: str):
        return (self.stats[stat]-10)//2

    def generateStat(self):
        numbers = []
        for i in range(4):
            numbers.append(random.randint(1, 6)) 
        return sum(numbers) - min(numbers)
    def generateStats(self):
        generatedStats = []
        for i in range(6):
            generatedStats.append(self.generateStat())
        return generatedStats
