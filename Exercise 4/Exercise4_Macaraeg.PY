"""
Exercise 4
John Austin S. Macaraeg
2023-13332
BS Geodetic Engineering
"""
# IMPORT DIFFERENT FUNCTIONS IN A MODULE
from math import cos, sin, radians, sqrt 

class Line: # TO BUNDLE THE DATA

    def __init__(self, distance, azimuth): # INITIALIZATION OF ATTRIBUTES
        self.distance = distance
        self.azimuth = azimuth

    def latitude(self):
        # INSERT CODE FOR LATITUDE HERE
        '''
        Compute for the latitude of a given line.

        Input:
        distance - float
        azimuth - float

        Output:
        latitude - float
        '''

        latitude = -float(self.distance) * cos(radians(float(self.azimuth)))

        return latitude

    def departure(self):
        # INSERT CODE FOR DEPARTURE HERE
        '''
        Compute for the departure of a given line.

        Input:
        distance - float
        azimuth - float

        Output:
        departure - float
        '''

        departure = -float(self.distance) * sin(radians(float(self.azimuth)))

        return departure

    def bearing(self):
        # INSERT CODE FOR BEARING HERE
        '''
        Compute for the DMS bearing of a given angle.

        Input:
        azimuth - float

        Output:
        bearing - string
        '''

    # DD TO DMS (TO SHOW IN BEARING)
        if azimuth > 0 and azimuth < 90:
            DD = float(azimuth)
            degree = int(DD)
            minutes = ((DD - degree) * 60)
            minutes_whole = int(minutes) 
            seconds = ((minutes - minutes_whole) * 60)
            DD = str(degree) + "-" + str(minutes_whole) + "-" + str(round(seconds, 2))
            bearing = 'S {: ^10} W' .format(DD,) 
        elif azimuth > 90 and azimuth < 180:
            DD = float(azimuth)
            degree = int(DD)
            minutes = ((DD - degree) * 60)
            minutes_whole = int(minutes) 
            seconds = ((minutes - minutes_whole) * 60)
            DD = str(degree) + "-" + str(minutes_whole) + "-" + str(round(seconds, 2))
            bearing = 'S {: ^10} W' .format(DD)
            bearing = 'N {: ^10} W' .format(180 - azimuth) # TO CONSIDER THE DIRECTION PER INSERTED VALUE
        elif azimuth > 180 and azimuth < 270:
            DD = float(azimuth)
            degree = int(DD)
            minutes = ((DD - degree) * 60)
            minutes_whole = int(minutes) 
            seconds = ((minutes - minutes_whole) * 60)
            DD = str(degree) + "-" + str(minutes_whole) + "-" + str(round(seconds, 2))
            bearing = 'S {: ^10} W' .format(DD)
            bearing = 'N {: ^10} W' .format(180 - azimuth) # TO CONSIDER THE DIRECTION PER INSERTED VALUE
            bearing = 'N {: ^10} E' .format(azimuth - 180)
        elif azimuth > 270 and azimuth < 360:
            DD = float(azimuth)
            degree = int(DD)
            minutes = ((DD - degree) * 60)
            minutes_whole = int(minutes) 
            seconds = ((minutes - minutes_whole) * 60)
            DD = str(degree) + "-" + str(minutes_whole) + "-" + str(round(seconds, 2))
            bearing = 'S {: ^10} W' .format(DD)
            bearing = 'N {: ^10} W' .format(180 - azimuth)
            bearing = 'N {: ^10} E' .format(azimuth - 180)
            bearing = 'S {: ^10} E' .format(360 - azimuth) # TO CONSIDER THE DIRECTION PER INSERTED VALUE
        elif azimuth == 0:
            bearing = "DUE SOUTH"    
        elif azimuth == 90:
            bearing = "DUE WEST"
        elif azimuth == 180:
            bearing = "DUE NORTH"
        elif azimuth == 270:
            bearing = "DUE EAST"
        else:
            bearing = "EWAN KO"
        return bearing

class Cardinal(Line):

    def __init__(self, distance, azimuth): # INITIALIZATION ULIT
        super().__init__(distance, azimuth) # PARA MAACCESS YUNG PROPERTY NG IBANG CLASS (PARA HINDI NA MAGING REDUNDANT)

    def bearing(self):
        if azimuth == 0:
            bearing = "DUE SOUTH"
        elif azimuth == 90:
            bearing = "DUE WEST"
        elif azimuth == 180:
            bearing = "DUE NORTH"
        elif azimuth == 270:
            bearing = "DUE EAST"
        else:
            bearing = "EWAN KO"
        return bearing      

counter = 1
lines = []
sumLat = 0
sumDep = 0
sumDist = 0

while True:

    print()
    print("LINE NO. ", counter)

    input_error = False # CREATE A SENTINEL CONTROLLED LOOP
    while not(input_error):
        distance = input("Distance: ")
        if input_error:
            print("INPUT ERROR")
            continue
        if not (input_error):
            break    

    azimuth = input("Azimuth from the South [DMS]: ")
   
    if "-" in str(azimuth): # DMS TO DD
        dms = azimuth
        degrees, minutes, seconds = azimuth.split("-")
        degrees, minutes, seconds = float(degrees), float(minutes), float(seconds)
        azimuth = (int(degrees) + (int(minutes)/60) + (float(seconds)/3600))%360
    else:
        azimuth = float(azimuth)%360

    if azimuth % 90 == 0:
        line = Cardinal(distance, azimuth)
    else:
        line = Line(distance, azimuth)

    sumLat += line.latitude() # sumLat = sumLat + line.(latitude)
    sumDep += line.departure()
    sumDist += float(line.distance)

    lines.append((counter, line.distance, line.bearing(), line.latitude(), line.departure())) # INSERT () AS BEARING, LATITUDE, AND DEPARTURE ARE NOW FUNCTIONS

# ASKING FOR INPUT
    yn = input("ADD NEW LINE? ")

    if yn.lower() == "yes" or yn.lower() == "y": # TO WIDEN OR CONSIDER OTHER OPTIONS (ANSWER) TO THE QUESTION "ADD NEW LINE?"
        counter = counter + 1
        continue
    else:
        break

# ALIGNMENT AND ORGANIZATION
print("___________________________________________________________________________")
print("                                 TRAVERSE                                  ")

print("___________________________________________________________________________")
print('{: ^10} {: ^10} {: ^15} {: ^17} {: ^17}' .format("LINE NO.", "DISTANCE", "BEARING", "LATITUDE", "DEPARTURE")) #ADD SPACES
for line in lines: 
    print('{: ^10} {: ^10} {: ^10} {: ^18} {: ^16}' .format(line[0], line[1], line[2], round(line[3]), round(line[4]))) #ADD SPACES AND YUNG ROUND PARA MAROUND OFF YUNG VALUES NUNG FLOAT
print("___________________________________________________________________________")

print("\n")

print("___________________________________________________________________________")
print("                                 SUMMATION                                 ")
print("___________________________________________________________________________")
print("SUMMATION OF LAT: ", sumLat)
print("SUMMATION OF DEP: ", sumDep)
print("SUMMATION OF DIST: ", sumDist)

lec = sqrt((sumLat**2) + (sumDep**2))

print("LEC: ", lec)
rec = sumDist/lec
print("1: ", round(rec, -3))
print("___________________________________________________________________________")
    
print("                                    END                                    ")