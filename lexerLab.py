#Eliseo Izazaga
#the regex expressions work, the issue is that every time you remove an op or an element and not add a white
#space later in the function it will add all the elements, without this white space the elements will then 
#join to make a new string which is not what we want, I ran out of time to complete this HW

import re

#Print your output list, look like this: [<key,int>, <id,A1>, <op,=>, <lit,5>]

kwIF    =       "if"
kwELSE  =       "else"
kwINT   =       "int"
kwFLOAT =       "float"
opEQUAL     =       "=" #or ^=$ works too
opPLUS      =       "\+"
opGREATER   =       "\>"
opMULT      =       "\*"
sepOPENPARENTHESIS          =   "\("
sepCLOSEDPARENTHESIS        =   "\)"
sepCOLON                    =   "\:"
sepOPENDOUBLEQUOTE          =   "\“"
sepCLOSEDOUBLEQUOTE          =   "\”"
litFLOAT    =   "\d+\d.\d+"
litINT      =   "^[0-9]*$"
litFLOAT    =   "\d+\d.\d+"
litSTRING    =   "[^print]\b[A-z]+\b"




stringToCutUp = "int A1=5"

def CutOneLineTokens(instring):
    keyword = re.match(kwINT, instring)
    if keyword != None:
         if keyword.group() == "int":
             print("you made it this far")
             listOfSplitString = instring.split(keyword.group())
             print("this is the split ", end = "")
             print(listOfSplitString)
             instring = ""
             instring = instring.join(listOfSplitString)
             print(instring)
    keyword = re.match(kwFLOAT, instring)
    if keyword != None:
         if keyword.group() == "float":
             print("you made it this far")
             listOfSplitString = instring.split(keyword.group())
             print("this is the split ", end = "")
             print(listOfSplitString)
             instring = ""
             instring = instring.join(listOfSplitString)
             print(instring)
    keyword = re.search(opEQUAL, instring)
    print(instring)
    if keyword != None:
         if keyword.group() == "=":
             #print("you made it this far")
             listOfSplitString = instring.split(keyword.group())
             print("this is the split ", end = "")
             print(listOfSplitString)
             instring = ""
             instring = instring.join(listOfSplitString)
             print(instring)
             keyword = re.search(opEQUAL, instring)
    print(instring)
    if keyword != None:
         if keyword.group() == "=":
             #print("you made it this far")
             listOfSplitString = instring.split(keyword.group())
             print("this is the split ", end = "")
             print(listOfSplitString)
             instring = ""
             instring = instring.join(listOfSplitString)
             print(instring)
             keyword = re.search(opEQUAL, instring)
    print(instring)
    if keyword != None:
         if keyword.group() == "=":
             #print("you made it this far")
             listOfSplitString = instring.split(keyword.group())
             print("this is the split ", end = "")
             print(listOfSplitString)
             instring = ""
             instring = instring.join(listOfSplitString)
             print(instring)


    #ret = instring.partition()
    #print(ret)
    
    #keyWordHolder = re.match(kwINT, instring)
    #if keyWordHolder.group() == "int":
    #    listOfSplitString = instring.split(keyWordHolder.group())
    #    print(listOfSplitString)
    #    joinedListIntoString = ""
    #    joinedListIntoString = joinedListIntoString.join(listOfSplitString)
    #    print(joinedListIntoString)
    #    print("We caught an int")
    #print(keyWordHolder.group())
    #print(instring)

CutOneLineTokens(stringToCutUp)