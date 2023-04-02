myString = "This is a string."
print(myString)

#Extend the Python script by using the built-in function type() to get the data type of the variable. Enter the following code:
print(type(myString))

#To convert the return value of type into a string, use the str() built-in function:
print(myString + " is of the data type " + str(type(myString)))

#Create two strings and then concatenate them by entering the following code:
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name? ")
#Use the print() function to write the value of the variable to the shell:

print(name)

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
#You have been using the print() function with only one variable, but you can also use it with multiple variables to format a string. Enter the following code:

print("{}, you like a {} {}!".format(name,color,animal))