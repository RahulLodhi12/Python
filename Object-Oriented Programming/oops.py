# a = 12
# b = 34

# print("Sum of a and b: ",a+b)

# OR
# Using OOPS 
from tkinter import N


class Number:
    def sum(self):
        return self.a + self.b   # a and b are variable of class Number

num = Number() # object instantiation, object num is asigned to one instance of class Number
# instance -> distinct identity
num.a = 12
num.b = 34

print(num.sum())

''' Solving a problem by creating objects is one of the most popular approaches in programming. 
This is called object-oriented programming.
This concept focuses on using reusable code.(OOPS Implements DRY(Don't repeat yourself) principle)

Class :-
A class is a blueprint/template (used) for creating objects.
A class contains info to create a valid object. '''

'''
PascalCase :-
EmployeeName

camelCase :-
isNumeric, isFloatOrInt
'''
# The syntax of a class looks like this:

# Class EmployeeName:		[classname is written in PascalCase]
 	#methods & variables