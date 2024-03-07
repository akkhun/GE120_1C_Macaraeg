# Lecture 3 Notes

# LISTS
listahan = ["mafe", "justin", "mika", "uste"]
print(listahan)

# gusto si mika makuha (position)
print(listahan[2])

# subset of the list, mafe and si justin
print(listahan[0:2])

print(listahan[1:3])

# nagstastart sa simula
print(listahan[3])

# start from index, end sa dulo
print(listahan[2:])

print(listahan[-1])

# gets first item, last item, then those in between
print(listahan[-3:3])

# Addition 

listahan[0] = "chelzy"

#TUPLES
tuple_1 = ("maja", "gianna", "jewel")
print(tuple_1)

# tuples are immutable
# tuple_1 = "quinmar"

# NESTED LISTS
list_1 = [ ["apple", "bola", "carton"], ["apricot", "banana", "cow"]]
print(list_1[0][2])

# NESTED TUPLES
tuple_2 = ((12.1244, -12.1244),(35.46261,-67.1231),(123.124, 56.232))
print(tuple_2[2][0])

# DICTIONARIES - key value pairs
dog = {
        "name": "Bogart",
        "age": 2,
        "color": "white",
        "favorite_num": 3.14,
        1: 45 # pwede si number as key (float or int)
       }

# print(dog[1.113]) 
print(dog.values()) #returns a list of values
print(dog.keys()) #returns a list of keys

dog["favorite_num"] = 39

print(dog["favorite_num"])

grade = 85
if grade >= 92:
    print("YAHOO")
elif grade >= 60:
    print("NICE")
else:
    print("SAD")

grade = 59; favorite = True
if grade >= 92:
    print("YAHOO")
elif grade >= 60:
    print("NICE")
elif grade < 60 and favorite:
    print("PASANG AWA")
else:
    print("SAD")

# LOOPS AND BREAK CONTINUE AND PASS

# for number in range(10):
#     #print(number) 0-5
#     if number == 5:
#         break
#     print(number)

# for number in range(10):
#     print(number)
#     if number == 5:
#         continue

# for number in range(10):
#     if number == 5:
#         print(number)
#         continue

# for number in range(10):
#     if number == 5:
#         pass 
#         print(number)

rec = 0
while rec < 5000:
    rec = int(input("Enter REC: "))
    kulang = 5000 - rec
    if rec >= 4500:
        pass
        print("onti nalang kulang, kaya mo yan")
    print("kulang ka ng REC na ", kulang)

print("PASOK NA REC")
print("-----END-----")



