# OBJECT ORIENTED PROGRAMMING

#creating classes
class Crayon:
    pass

redCrayon = Crayon()

# print(type(redCrayon))

# creating ml heroes

class MLHero:
    def __init__(self, name, description="Twilight Goddess", offense=80):
        self.name = name
        self.description = description
        self.role = "Mage"
        self.specialty = "Damage/Poke"
        self.statistics = {
            "durability": 60,
            "offense"
            "skill_effects": 50,
            "difficulty": 70,
        }

    def __str__(self):
        return(self.name + " , the " + self.description)

    def __add__(self, other):
        return(self.name + " and " + other.name + " combined!")

    def __gt__(self,other):
        if (self.statistics["offense"] > other.statistics["offense"]):
            return(self.name + "lost. ", other.name + " is too strong!")    

    def skill(self):
        print(self.name + " used the ATTACK!!")

    def superSkill(self, opponent):
        print(self.name + " used SUPERSKILL!! against " + opponent)    

    def split(self):
        print("MASAKIT Mag split")

# hero = MLHero("Lunox", "MasipagNaUPStudent")
lunox = MLHero("Lunox")
aldous = MLHero("Aldous", "Demon SLayer", 90)
print(aldous > lunox)
# print(hero)
# print("Hero Name:", hero.name)
# print("Hero Description:", hero.description)
# print("Hero Role:", hero.role)
# print("Hero Specialty:", hero.specialty.split("/"))
# print("Hero Offense+Difficulty:", hero.statistics["offense"] + hero.statistics["difficulty"])

hero.superSkill("Zilong")
hero.split()

# split is just a method of the class String
text = "HELLO,PLUS,ME"
text.split()