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


# next to learn is logic and control flow
# of lists and other other logic control items, 
# ultimately we are going to program the rpi
# to a robot, good practice is to complete planter
# comm and give to friends, accomplish the same with
# rpi in python since the hardware is the same. 

#we will declare cariable and do and if then an else

aVariable = 30 
if aVariable < 100:
    print(aVariable)
elif aVariable > 100:
    print(aVariable)
else:
    print("default case")

#This is the lists part
#lists hold changeable pieces of data, they do not all have to be the same

l1 = [1, 2.1, "String", False]

if len(l1) < 10:
    print(len(l1))
    print(l1)
else:
    print(l1)

#changing things in list

l1[0] = "A different value"
print(l1)
l1[2:4] = [5, "we changed 4"]
print(l1)
 #the list also has a pop function

l1.pop(0) #the parameter inside pop will remove the element in that place


#this is the loops part
countingVariable = 1 
while countingVariable < 10:
    print(countingVariable)
    countingVariable += 1

leCounter = 0
while leCounter < 20:
    if leCounter < 10:
        print(leCounter)
        leCounter += 1
    elif leCounter > 15:
        print(leCounter)
        leCounter += 3
    else:
        print(leCounter)
        leCounter += 5

#this is the for loop

for x in range(0, 20):
   print(x)

#below does not work as intended, x is a variable, while x is between 0 and 10
#in ascending order the, it will only cycle because of the range() function,
#nothing is able to overide it.     
y = 0
for y in range(y,20):
    y += 5
    print(y)
 

 #will print the elements in the list
for x in[2,5,7,6]:
     print(x)

#tuples are like list but they do not change
#syntax is as follows
tupleUno = (1, 3, "HEllO", "Based", 3.21)

for x in tupleUno:
    print(x)


