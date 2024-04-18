/*
Exercise 3
John Austin S. Macaraeg
2023-13332
BS Geodetic Engineering
*/

# IMPORT DIFFERENT FUNCTIONS IN A MODULE
from math import cos, sin, radians, sqrt 

# CREATING MY OWN FUNCTION(S)
function getLatitude(distance, azimuth) {
    /*
    Compute for the latitude of a given line.

    Input:
    distance - float
    azimuth - float

    Output:
    latitude - float
    */

    var latitude = -distance * Math.cos(Math.radians(azimuth))

    return latitude
}

function getDeparture(distance, azimuth) {
    /*
    Compute for the departure of a given line.

    Input:
    distance - float
    azimuth - float

    Output:
    departure - float
    */

    var departure = -distance * Math.sin(Math.radians(azimuth))

    return departure
}

function azimuthToBearing(azimuth) {
    /*
    Compute for the bearing of a given angle.

    Input:
    azimuth - float

    Output:
    bearing - string
    */

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
    bearing = azimuthToBearing(azimuth)

    if "-" in str(azimuth): # DMS TO DD
        dms = azimuth
        degrees, minutes, seconds = azimuth.split("-")
        degrees, minutes, seconds = float(degrees), float(minutes), float(seconds)
        azimuth = (int(degrees) + (int(minutes)/60) + (float(seconds)/3600))%360
    else:
        azimuth = float(azimuth)%360

# DD TO DMS (TO SHOW IN BEARING)
    if (azimuth > 0 && azimuth < 90) {
        DD = float(azimuth)
        degree = int(DD)
        minutes = ((DD - degree) * 60)
        minutes_whole = int(minutes) 
        seconds = ((minutes - minutes_whole) * 60)
        DD = str(degree) + "-" + str(minutes_whole) + "-" + str(round(seconds, 2))
        bearing = 'S '.concat(DD.toString(), {: ^10} ' W')
    }
    else if (azimuth > 90 && azimuth < 180) {
        DD = float(azimuth)
        degree = int(DD)
        minutes = ((DD - degree) * 60)
        minutes_whole = int(minutes) 
        seconds = ((minutes - minutes_whole) * 60)
        DD = str(degree) + "-" + str(minutes_whole) + "-" + str(round(seconds, 2))
        bearing = 'S '.concat(DD.toString(), {: ^10} ' W')
        bearing = 'N {: ^10} W' .format(180 - azimuth)
    }
    else if (azimuth > 180 && azimuth < 270) {
        DD = float(azimuth)
        degree = int(DD)
        minutes = ((DD - degree) * 60)
        minutes_whole = int(minutes) 
        seconds = ((minutes - minutes_whole) * 60)
        DD = str(degree) + "-" + str(minutes_whole) + "-" + str(round(seconds, 2))
        bearing = 'S '.concat(DD.toString(), {: ^10} ' W')
        bearing = 'N {: ^10} W' .format(180 - azimuth)
        bearing = 'N {: ^10} E' .format(azimuth - 180)
    }
    else if (azimuth > 270 && azimuth < 360) {
        DD = float(azimuth)
        degree = int(DD)
        minutes = ((DD - degree) * 60)
        minutes_whole = int(minutes) 
        seconds = ((minutes - minutes_whole) * 60)
        DD = str(degree) + "-" + str(minutes_whole) + "-" + str(round(seconds, 2))
        bearing = 'S '.concat(DD.toString(), {: ^10} ' W')
        bearing = 'N {: ^10} W' .format(180 - azimuth)
        bearing = 'N {: ^10} E' .format(azimuth - 180)
        bearing = 'S {: ^10} E' .format(360 - azimuth)
    }
    else if (azimuth == 0) {
        bearing = "DUE SOUTH"    
    }
    else if (azimuth == 90) {
        bearing = "DUE WEST"
    }
    else if (azimuth == 180) {
        bearing = "DUE NORTH"
    }
    else if (azimuth == 270) {
        bearing = "DUE EAST"
    }
    else {
        bearing = "EWAN KO"
    }

    lat = getLatitude(azimuth = float(azimuth), distance = float(distance))
    dep = getDeparture(azimuth = float(azimuth), distance = float(distance))

    sumLat += lat
    sumDep += dep
    sumDist += float(distance)

    constCorrLat = (-sumLat*(float(distance)/sumDist))
    constCorrDep = (-sumDep*(float(distance)/sumDist))

    corr_lat = (constCorrLat * float(distance))
    corr_dep = (constCorrDep * float(distance))

    adjLat = (lat + corr_lat)
    adjDep = (dep + corr_dep)


    line = (counter, distance, bearing, lat, dep, corr_lat, corr_dep, adjLat, adjDep) # CREATE TUPLE OF THE LINE
    lines.append(line)

# ASKING FOR INPUT
    yn = input("ADD NEW LINE? ")

    if yn.lower() == "yes" or yn.lower() == "y":
        counter = counter + 1
        continue
    else:
        break

}

# ALIGNMENT AND ORGANIZATION
print("____________________________________________________________________________________________________________________________________________________")
print("                                                                    TRAVERSE                                                                        ")

print("____________________________________________________________________________________________________________________________________________________")
print('{: ^10} {: ^10} {: ^15} {: ^17} {: ^17} {: ^17} {: ^17} {: ^20} {: ^20}' .format("LINE NO.", "DISTANCE", "BEARING", "LATITUDE", "DEPARTURE", "cLAT", "cDEP", "ADJLAT", "ADJDEP")) 
for line in lines: 
    print('{: ^10} {: ^10} {: ^10} {: ^10} {: ^10} {: ^10} {: ^10} {: ^10} {: ^10}' .format(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8]))
print("____________________________________________________________________________________________________________________________________________________")

print("\n")

print("____________________________________________________________________________________________________________________________________________________")
print("                                                                   SUMMATION                                                                        ")
print("____________________________________________________________________________________________________________________________________________________")
print("SUMMATION OF LAT: ", sumLat)
print("SUMMATION OF DEP: ", sumDep)
print("SUMMATION OF DIST: ", sumDist)

lec = sqrt((sumLat**2) + (sumDep**2))

print("LEC: ", lec)
rec = sumDist/lec
print("1: ", round(rec, -3))
print("____________________________________________________________________________________________________________________________________________________")
    
print("                                                                      END                                                                           ")