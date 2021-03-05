#Eliseo Izazaga
import re

string1 = "22.11"
string2 = "23"
string3 = "66.7f"
string4 = "123abcde"
string5 = "Case44"
string6 = "Happy"
string7 = "78"
string8 = "66.7"
string9 = "yes123"
string10 = "Book111"

#regex terms
a = "^\d+$"                #to search for an int
b =  "^\d+\.\d+$"        #searches for float
c = "^\b\d*\.\d{2}\b$" #looks for float with 2
d = "^\d*\.\d+f$"
e = "^[A-Z]+[a-z]+\d+$"    #cap letters then lower then digits
f = "^\d{3}[A-z]{2,}$"      #exaclty 2 digits then 2 letters

def search(regexParam, stringToSearch, stringToPrint):
    result = re.search(regexParam, stringToSearch)
    if result != None:
        print(stringToSearch, end="")
        print(" matches the pattern: ", end="")
        print(stringToPrint)
    else:
        print(stringToSearch, end="")
        print(" does not match and pattern for", end="")
        print(" "+ stringToPrint)

def removeIntFromBeginning( stringToSearch):
    numberToRemove = re.search("^\\d+$",stringToSearch)
    print(numberToRemove)
    x = stringToSearch.split(numberToRemove)
    del x[0] 
    print(x)  

        

search(a, string1, "An integer")
search(b, string1, "A float consists of 1 or more digits before and after decimal point")
search(c, string1, "A float with exactly 2 digits after the decimal point")
search(d, string1, "A float end with letter f")
search(e, string1, "Capital letters, followed by small case letters, followed by digits")
search(f, string1, "Exactly 3 digits, followed by at least 2 letters")
print()
search(a, string2, "An integer")
search(b, string2, "A float consists of 1 or more digits before and after decimal point")
search(c, string2, "A float with exactly 2 digits after the decimal point")
search(d, string2, "A float end with letter f")
search(e, string2, "Capital letters, followed by small case letters, followed by digits")
search(f, string2, "Exactly 3 digits, followed by at least 2 letters")
print()
search(a, string3, "An integer")
search(b, string3, "A float consists of 1 or more digits before and after decimal point")
search(c, string3, "A float with exactly 2 digits after the decimal point")
search(d, string3, "A float end with letter f")
search(e, string3, "Capital letters, followed by small case letters, followed by digits")
search(f, string3, "Exactly 3 digits, followed by at least 2 letters")
print()
search(a, string4, "An integer")
search(b, string4, "A float consists of 1 or more digits before and after decimal point")
search(c, string4, "A float with exactly 2 digits after the decimal point")
search(d, string4, "A float end with letter f")
search(e, string4, "Capital letters, followed by small case letters, followed by digits")
search(f, string4, "Exactly 3 digits, followed by at least 2 letters")
print()
search(a, string5, "An integer")
search(b, string5, "A float consists of 1 or more digits before and after decimal point")
search(c, string5, "A float with exactly 2 digits after the decimal point")
search(d, string5, "A float end with letter f")
search(e, string5, "Capital letters, followed by small case letters, followed by digits")
search(f, string5, "Exactly 3 digits, followed by at least 2 letters")
print()
search(a, string6, "An integer")
search(b, string6, "A float consists of 1 or more digits before and after decimal point")
search(c, string6, "A float with exactly 2 digits after the decimal point")
search(d, string6, "A float end with letter f")
search(e, string6, "Capital letters, followed by small case letters, followed by digits")
search(f, string6, "Exactly 3 digits, followed by at least 2 letters")
print()
search(a, string7, "An integer")
search(b, string7, "A float consists of 1 or more digits before and after decimal point")
search(c, string7, "A float with exactly 2 digits after the decimal point")
search(d, string7, "A float end with letter f")
search(e, string7, "Capital letters, followed by small case letters, followed by digits")
search(f, string7, "Exactly 3 digits, followed by at least 2 letters")
print()
search(a, string8, "An integer")
search(b, string8, "A float consists of 1 or more digits before and after decimal point")
search(c, string8, "A float with exactly 2 digits after the decimal point")
search(d, string8, "A float end with letter f")
search(e, string8, "Capital letters, followed by small case letters, followed by digits")
search(f, string8, "Exactly 3 digits, followed by at least 2 letters")
print()
search(a, string9, "An integer")
search(b, string9, "A float consists of 1 or more digits before and after decimal point")
search(c, string9, "A float with exactly 2 digits after the decimal point")
search(d, string9, "A float end with letter f")
search(e, string9, "Capital letters, followed by small case letters, followed by digits")
search(f, string9, "Exactly 3 digits, followed by at least 2 letters")
print()
search(a, string10, "An integer")
search(b, string10, "A float consists of 1 or more digits before and after decimal point")
search(c, string10, "A float with exactly 2 digits after the decimal point")
search(d, string10, "A float end with letter f")
search(e, string10, "Capital letters, followed by small case letters, followed by digits")
search(f, string10, "Exactly 3 digits, followed by at least 2 letters")


removeIntFromBeginning("22 street")
removeIntFromBeginning("90years")




#foundInt = re.search(a, string2)
#print(foundInt.group())
#this is a basic pattern insert
#txt = "The rain in Spain"
#x = re.search("^The.*Spain$", txt)
#regexIsUgly = "^\\d\\d$"
#x = re.search(regexIsUgly, string2)
#print(x)
#print(x.group())