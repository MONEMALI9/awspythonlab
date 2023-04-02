'''
Categorizing Values
    Lab overview
    With Python, you can mix types in a list. In this lab, you will create a list with different types and print the values.
    
    In this lab, you will:
    
        Use numeric data types
        Use string data types
        Use the list data type
        Use a for loop
        Use the print() function
'''
#Exercise 1: Creating a mixed-type list

#Define a list with different types, like the following example:
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

#Use a for loop statement to traverse the list and print the data type for each item in the list:
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))