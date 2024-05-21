#CREATING A PARCEL
class Parcel: 
    def __init__(self, owner, area): #INITIALIZATION
        self.owner = owner
        self.area = area
        self.getClassification = {
            "Residential": self.area/10000 < 1,
            "Private Agricultural": 1 < self.area/10000 < 12,
            "Public Agricultural": self.area/10000 > 12,
        }
            # {
            # # if (self.getClassification/10000 < 1):
            # #     return("Residential")
            # # elif (1 < self.getClassification/10000 < 12):
            # #     return("Private Agricultural")
            # # elif (self.getClassification/10000 > 12):
            # #     return("Public Agricultural")
            # }

    def getClassification(self):
        if (self.getClassification == "Residential"):
            return("Residential")
        elif (1 < self.getClassification/10000 == "Private Agricultural"):
            return("Private Agricultural")
        elif (self.getClassification/10000 == "Public Agricultural"):
            return("Public Agricultural")
            
#OPERATION OVERLOADING 
def __str__(self): #OVERLOADING THE PRINT FUNCTION
    return("A parcel of land owned by" + self.owner + "with an area of" + self.area + "square meters")

def __add__(self, other): #OVERLOADING THE "+" OPERATOR
    return("Consolidated lot of" + self.owner + "and" + other.owner + "with a total area of" + self.area + other.area + "square meters")

class Riparian(Parcel):
    def __init__(self, owner, area, type):  #INITIALIZATION
        self.owner = str(owner)
        self.area = int(area)
        self.type = type
        self.getAdjoiningWaterbody = {
            "Adjacent to River - can be subject to titling": self.type == 1,
            "Adjacent to Ocean (Littoral) - cannot be subject to titling": self.type == 2,
            "Invalid Riparian Parcel": self.type != 1 or 2,
        }

            # {
            # # if (self.type == 1):
            # #     return("Adjacent to River - can be subject to titling")
            # # elif (self.type == 2):
            # #     return("Adjacent to Ocean (Littoral) - cannot be subject to titling")
            # # else:
            # #     return("Invalid Riparian Parcel")
            # }

    def getAdjoiningWaterbody(self):
        if (self.getAdjoiningWaterbody == "Adjacent to River - can be subject to titling"):
            return("Adjacent to River - can be subject to titling")
        elif (self.getAdjoiningWaterbody == "Adjacent to Ocean (Littoral) - cannot be subject to titling"):
            return("Adjacent to Ocean (Littoral) - cannot be subject to titling")
        elif (self.getAdjoiningWaterbody == "Invalid Riparian Parcel"):
            return("Invalid Riparian Parcel")



      
            



    

