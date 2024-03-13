"""
Exercise 2
John Austin S. Macaraeg
2023-13332
BS Geodetic Engineering
"""

# CREATE A SENTINEL CONTROLLED LOOP
counter = 1
lines = []

while True:
    print()
    print("LINE NO. ", counter)
    distance = input("DISTANCE: ")
  
    azimuth = float(input("AZIMUTH FROM THE SOUTH: ")) % 360
   
    if azimuth > 0 and azimuth < 90:
        bearing = 'S {: ^10} W' .format(azimuth)
    elif azimuth > 90 and azimuth < 180:
        bearing = 'N {: ^10} W' .format(180 - azimuth)
    elif azimuth > 180 and azimuth < 270:
        bearing = 'N {: ^10} E' .format(azimuth - 180)
    elif azimuth > 270 and azimuth < 360:
        bearing = 'S {: ^10} E' .format(360 - azimuth)
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


    line = (counter, distance, bearing) # CREATE TUPLE OF THE LINE
    lines.append(line)

# ASKING FOR INPUT
    yn = input("ADD NEW LINE? ")
    
    if yn.lower() == "yes" or yn.lower() == "y":
        counter = counter + 1
        continue
    else:
        break

print("\n\n")
print('{: ^10} {: ^10} {: ^10}' .format("LINE NO.", "DISTANCE", "    BEARING"))
for line in lines: 
    print('{: ^10} {: ^10} {: ^10}' .format(line[0], line[1], line[2]))
    
print("           -----END-----          ")