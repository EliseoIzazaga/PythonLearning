import re
kwTERM = "if|else|int|float|print|=|\+|>|\*|\(|\)|:|;|“|”|[A-z]+\w+|[A-z]+|\d+.\d+|\d+"
lineToSearch = "int A1=5"
#Output <type, token> list: [<key,int>, <id,A1>, <op,=>, <lit,5>]

def CutOneLineTokens(inCode):
    outList = ["<key,","<id,","<op,","<lit,"]
    listOfOccurences = re.findall(kwTERM, inCode)
    #print(listOfOccurences)
    for x in range(len(listOfOccurences)):
    #print(listOfOccurences[x])
        if(listOfOccurences[x] == "if"):
            #print(listOfOccurences[x])
            tempStr = outList[0]
            tempStr = tempStr + listOfOccurences[x] + ","
            outList[0] = tempStr
        elif(listOfOccurences[x] == "else"):
            #print(listOfOccurences[x])
            tempStr = outList[0]
            tempStr = tempStr + listOfOccurences[x] + ","
            outList[0] = tempStr
        elif(listOfOccurences[x] == "int"):
            #print(listOfOccurences[x])
            tempStr = outList[0]
            tempStr = tempStr + listOfOccurences[x] + ","
            outList[0] = tempStr
        elif(listOfOccurences[x] == "float"):
            #print(listOfOccurences[x])
            tempStr = outList[0]
            tempStr = tempStr + listOfOccurences[x] + ","
            outList[0] = tempStr
        elif(listOfOccurences[x] == "="):
            tempStr = outList[2]
            tempStr = tempStr + listOfOccurences[x] + ","
            outList[2] = tempStr
        elif(listOfOccurences[x] == "+"):
            tempStr = outList[2]
            tempStr = tempStr + listOfOccurences[x] + ","
            outList[2] = tempStr
        elif(listOfOccurences[x] == ">"):
            tempStr = outList[2]
            tempStr = tempStr + listOfOccurences[x] + ","
            outList[2] = tempStr
        elif(listOfOccurences[x] == "*"):
            tempStr = outList[2]
            tempStr = tempStr + listOfOccurences[x] + ","
            outList[2] = tempStr
        elif(listOfOccurences[x] == "("):
            tempStr = outList[2]
            tempStr = tempStr + listOfOccurences[x] + ","
            outList[2] = tempStr
        elif(listOfOccurences[x] == ")"):
            tempStr = outList[2]
            tempStr = tempStr + listOfOccurences[x] + ","
            outList[2] = tempStr
        elif(listOfOccurences[x] == ":"):
            tempStr = outList[2]
            tempStr = tempStr + listOfOccurences[x] + ","
            outList[2] = tempStr
        elif(listOfOccurences[x] == "“"):
            tempStr = outList[2]
            tempStr = tempStr + listOfOccurences[x] + ","
            outList[2] = tempStr
        elif(listOfOccurences[x] == "”"):
            tempStr = outList[2]
            tempStr = tempStr + listOfOccurences[x] + ","
            outList[2] = tempStr
        else:
            litFloat = re.match("\d+\d.\d+", listOfOccurences[x]) # float literal
            if litFloat != None:
                    tempStr = outList[3]
                    tempStr = tempStr + listOfOccurences[x] + ","
                    outList[3] = tempStr
            else:
                litInt = re.match("^[0-9]*$", listOfOccurences[x]) # int literal
                if litInt != None:
                    tempStr = outList[3]
                    tempStr = tempStr + listOfOccurences[x] + ","
                    outList[3] = tempStr
                else:
                    litString = re.match("\b[^print][A-z]\b+", listOfOccurences[x]) # string literal
                    if litString != None:
                        tempStr = outList[3]
                        tempStr = tempStr + listOfOccurences[x] + ","
                        outList[3] = tempStr
                    else:
                        if(listOfOccurences[x] != "print"):
                            tempStr = outList[1]
                            tempStr = tempStr + listOfOccurences[x] + ","
                            outList[1] = tempStr
    tempStr = outList[0]
    tempStr = tempStr + ">"
    outList[0] = tempStr
    tempStr = outList[1]
    tempStr = tempStr + ">"
    outList[1] = tempStr
    tempStr = outList[2]
    tempStr = tempStr + ">"
    outList[2] = tempStr
    tempStr = outList[3]
    tempStr = tempStr + ">"
    outList[3] = tempStr

    print(outList)

CutOneLineTokens(lineToSearch)


'''listOfOccurences = re.findall(kwTERM, inCode)
print(listOfOccurences)
for x in range(len(listOfOccurences)):
    #print(listOfOccurences[x])
    if(listOfOccurences[x] == "if"):
        print(listOfOccurences[x])
    elif(listOfOccurences[x] == "else"):
        print(listOfOccurences[x])
    elif(listOfOccurences[x] == "int"):
        print(listOfOccurences[x])
    elif(listOfOccurences[x] == "float"):
        print(listOfOccurences[x])
    elif(listOfOccurences[x] == "="):
        print(listOfOccurences[x])
    elif(listOfOccurences[x] == "+"):
        print(listOfOccurences[x])
    elif(listOfOccurences[x] == ">"):
        print(listOfOccurences[x])
    elif(listOfOccurences[x] == "*"):
        print(listOfOccurences[x])
    elif(listOfOccurences[x] == "("):
        print(listOfOccurences[x])
    elif(listOfOccurences[x] == ")"):
        print(listOfOccurences[x])
    elif(listOfOccurences[x] == ":"):
        print(listOfOccurences[x])
    elif(listOfOccurences[x] == "“"):
        print(listOfOccurences[x])
    elif(listOfOccurences[x] == "”"):
        print(listOfOccurences[x])
    else:
        litFloat = re.match("\d+\d.\d+", listOfOccurences[x]) # float literal
        if litFloat != None:
            print("found a float literal")
            print(litFloat.group())
        else:
            litInt = re.match("^[0-9]*$", listOfOccurences[x]) # int literal
            if litInt != None:
                print("found an int literal")
                print(litInt.group())
            else:
                litString = re.match("\b[^print][A-z]\b+", listOfOccurences[x]) # string literal
                if litString != None:
                    print("found a string literal")
                    print(litString.group())
                else:
                    if(listOfOccurences[x] != "print"):
                        print(listOfOccurences[x])
                        print("is an identifier")'''    