print("Ilevel mo na yan!")
print("A program used to compute your direct levelling values")
print("John Austin S. Macaraeg")

from math import sqrt # IMPORT FROM ANOTHER MODULE
# INITIALIZATION OF VARIABLES

levelling_table = [] #CREATE A TUPLE
total_distance = 0
tp_counter = 1

# CREATING A FUNCTION
def floatInput(prompt):
    '''
    This purpose of this function is to make sure
    that the output is already converted into
    the float data type

    input - float
    '''

BM0 = float(input('Initial Elevation: ')) #INITIAL ELEV

# CREATING A SENTINEL-CONTROLLED LOOP
while True:

    print()
    print("LINE #: ", tp_counter)

       
    input_error = False # CREATE A SENTINEL CONTROLLED LOOP
    while not(input_error):
        backsight = float(input("Backsight: "))
        foresight = float(input("Foresight: "))
        distance = float(input("Distance: "))
        if input_error:
            print("INPUT ERROR")
            continue
        if not (input_error):
            break    

    
    height = BM0 + backsight
    total_distance += distance
    elevation = height - foresight

    line = (backsight, foresight, height, elevation)
    levelling_table.append(line)

    yn = input("ADD NEW LINE? ") # ASK FOR AN INPUT
    if yn.lower() == "yes" or yn.lower() == "y":
        tp_counter = tp_counter + 1
        continue
    else:
        break

print("\n")

error = elevation - BM0
firstorder = 4.80 * (sqrt(total_distance / 10**3))
secondorder = 8.40 * (sqrt(total_distance / 10**3))
thirdorder = 12.00 * (sqrt(total_distance / 10**3))



print('{: ^10} {: ^10} {: ^10} {: ^10}' .format("B.S.", "H.I.", "F.S.", "ELEV")) 
for line in levelling_table: 
    print('{: ^10} {: ^10} {: ^10} {: ^10}' .format(line[0], line[1], line[2], line[3]))

print("\n")    

print("Total Distance: ", total_distance)
print("Error: ", error)
print("FIRST ORDER: ", firstorder)
print("SECOND ORDER: ", secondorder)
print("THIRD ORDER: ", thirdorder)

if error == firstorder:
    print("FIRST ORDER"):
elif error == secondorder:
    print("SECOND ORDER"):
elif error == thirdorder
    print("THIRD ORDER"):
else:
    print("ERROR TOO LARGE")


