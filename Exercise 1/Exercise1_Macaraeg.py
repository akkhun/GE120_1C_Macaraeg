"""
Exercise 1
John Austin S. Macaraeg
2023-13332
BS Geodetic Engineering
"""

# DD TO DMS
DD = float((input("Input a number (In Decimal): ")))
print(DD)

# kunin si degrees 
degree = int(DD)

# kunin si minutes
minutes = ((DD - degree) * 60)
minutes_whole = int(minutes) 

# kunin si seconds
seconds = ((minutes - minutes_whole) * 60)

print("DMS: " + str(degree) + "-" + str(minutes_whole) + "-" + str(round(seconds, 2)))


# DMS TO DD
DMS =str(input("Input a number (In DMS): "))
print(DMS)

# split the values depending on the number of dashes
values = DMS.split("-")

degrees = int(values[0]) # getting degrees
minutes = int(values[1]) # getting minutes
seconds = float(values[2]) # getting seconds

dd = degrees + (minutes/600) + (seconds/3600)

print("DD: ", round(dd,6))
