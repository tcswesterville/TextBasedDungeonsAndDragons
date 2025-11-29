class Stats:
    def __init__ (strength, dexterity, charisma, constitution, intelligence, wisdom):
        self.stats = {
            "strength": strength,
            "dexterity": dexterity,
            "charisma": charisma,
            "constitution": constitution,
            "intelligence": inteligence,
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
    def SkillModifier(stat: str):
        return (self.stats[stat]-10)//2