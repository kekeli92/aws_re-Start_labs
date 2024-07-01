myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of a data type " + str(type(myString)))

firtString = "water"
secondString = "fall"
thirdString = firtString + secondString
print(thirdString)

name = input(" what is your name? ")
print(name)

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
