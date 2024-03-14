# FUNCTIONS: because they uphold the DRY principle (Don't Repeat Yourself)

# print("Hello World")

# # Convert a number into a string
# a = 1
# b = str(a)
# print(type(b))

# Define our own functions
# def shout(word):
#     # number = 2
#     print(number)
#     print(word + "!")

# number = 1

# # Calling a fxn
# shout("YOLE")
# shout("AJ")
# shout("MIKA")
# shout("PETER")

# number = 3

# shout("JUSTIN")

# variables inside fxns are not available globally
# print(word)
# print(number)

def shout(word1, num_ulit_last_letter):
    '''
    Given a word, kunin yung last letter, ulitin ng ilang beses
    tapos kapag prinint, print the word, plus inulit na last 
    letter + exclamation point

    Parameters:
    word1 (string) - word to be printed
    '''
    print(word1.upper() + word1[-1].upper()*(num_ulit_last_letter-1) + "!!!!!")
    # print(list_of_names_)

# shout("Mafe", 5)

print(shout.__doc__)
# help(len)
# help(shout)

# TYPES OF ARGUMENTS

def convertDMStoDEG(dms_1="118-25-14.48", name = "JANNAH"):
    '''
    Convert DMS to degrees

    Arguments:
        dms - string
    '''
    degrees, minutes, seconds = dms_1.split("-")
    dd = int(degrees) + (int(minutes)/60) + (float(seconds)/3600)
    return round(dd,6)

convertDMStoDEG(name = "MAJA", dms_1 = "123-13-14")

# RETURNING FROM A FUNCTION
result = (convertDMStoDEG("12-12-12"))
result += 10
print(result)

# printing after returning something
def getDirection(degrees):
    '''
    Gives the quadrant of an angle

    Input:
    degrees - float

    Output:
    quadrant - string
    '''
    print("HELLO DOM")
    if degrees > 0 and degrees < 90:
        return "S-W"
    elif degrees > 90 and degrees < 180:
        return "N-W"
    elif degrees > 180 and degrees < 270:
        return "N-E"
    elif degrees > 270 and degrees < 360:
        return "S-E"
    else: 
        return "IDK"

dms = "100-12-14"
dd = convertDMStoDEG(dms)
direction = getDirection(dd)
print(direction)
