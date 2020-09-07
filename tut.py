import sys
import math
import random
import threading 
import time
from functools import reduce
# Hello, this is a comment in python
# Python files always end in extension .py
# statements terminate with a new line

print("Hello world") 

# take in input 
#nm = input("Enter name ") # takes input into variable nm
#print("hello, ", nm) # prints nm with string before
#number and reasignment demonstration
#num = input("Enter a number ")
#print("this is num ", num)
#nm = input("Enter a number to replace nm ")
#print(nm) 


#Extend multiple line statement enclosed in ()
v1 = ( 
    1 + 3
    + 4 + 6 
)
print(v1)

'''
This is a comment
hello
'''

# Varaibles in python 3
# 1st character must be a _ or a letter 

variableUno = 2
variableDos = 1
variableWater = "cool clear water"

print(variableUno)
print(variableDos)
print(variableWater)

# Data types are dynamic in python, 
# Data types in variables can be changed from one
# to another with ease, since all variables are dynamic
# they are interpreted as objects and do not need 
# declaration. 
# Python can handle string, numbers, ints, floats
# complex numbers and bools, there are no chars

# type function returns type
print(type(10))
print(type(variableUno))
print(type(variableWater))

# there are no limitations to the size of the size
# of the variables. but there is a practical size 

# practical max int size
print(sys.maxsize)
# practical max float size 
print(sys.float_info.max)

# floats are accurate to 15 decimal places
f1 = 1.111111111111111
f2 = f1
print(f1 + f2)
