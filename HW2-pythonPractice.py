#Eliseo Izazaga HW2

#Python exercise questions
#Help you getting familiar with Python syntax

#Grading:

#IMPORTANT NOTICE:
#A good practice in coding is to show your customer a working version and tell them
#what new features you want to add next.
#Thus, we require you to submit all your homework as a working version. If you
#only know how to solve 7/10 questions, just submit the 7 that runs without errors.
#For incomplete answers, comment the code out and print a line tell us your progress
#E.g. "Problem 3 is a completed but has run time errors"
#or "problem 5 is incomplete, but I did 75% of the work."

#Complete HW + correct results: 10pt
#Each question has a equal share of the total points
#Code that does not run will have only 2pt.
#No submission: 0%

#Please follow the required input/output and function names
#Main function is at the end of the file
#Please call all of your completed functions and print the results out

#Please define all the needed input variables in your main function directly and not asking for
#user input. Also, please format the output from each function and print them out in the main.
import random
'''
 1. Input: Count
 Output: print Count number of "hello":
            1th hello
           2th hello...
 IMPORTANT: copy to visualizer, observe the behavior
'''
def easy_hello_loop1_for(Count):
        for x in range(Count):
                #print(int(x) + "hello")
                print(x, end ="")
                print("th hello")

'''
2.Input: number x,y
 Output: return the smaller value of the two
 Do it by yourself, no system calls like min()
'''
def smaller_value(x,y):
        if x < y:
                return x
        else:
                return y

'''
3. Do not use len(). Write a function to calculate how many elements do you have in your list, and return it
'''
def my_len(lis):
        count = 0
        for x in lis:
                count += 1
        return count
                

'''
4. input: a list with small strings that has 2 letters, 3 letters, or 4 letters
output: return 3 lists, Letter2, Letter3, Letter4 containing small strings. Print results out in the main function.
Sample:
input list: ['rt','asdf','ton','er','user']
will give
    Letter2=['rt','er']
    Letter3=['ton']
    Letter4=['asdf','user']
You can use len() in this question.
'''
def cate_letters(LongStr):
        Letter2 = []
        Letter3 = []
        Letter4 = []
        for x in range(len(LongStr)):
                #print(x)
                for k in range(len(LongStr[x])):
                        #print(k)
                        #print(LongStr[x][k])
                        if len(LongStr[x]) == 2:
                                Letter2.append(LongStr[x][k])
                        elif len(LongStr[x]) == 3:
                                Letter3.append(LongStr[x][k])
                        else:
                                Letter4.append(LongStr[x][k])     
        return Letter2, Letter3, Letter4



'''
5. input: a string with letters in it, a string with numbers in it.
We assume they have same amount of characters/length. 
output: go through the two strings together, print out elements by index
format "the elements at index __ from string1 is __, from string2 is ___"
'''
def two_strings(str1,str2):
        for x in range(len(str1)):
                print("the elements at index ", end="")
                print(x, end="")
                print(" from string1 is " , end="")
                print(str1[x], end ="")
                print(" from string2 is ", end="")
                print(str2[x])



'''
6. input: a string with letters in it, a string with numbers in it
output: go through the two strings together. At index i, if the number in str2 is even, put the letter in str1 into evenStr
if the number is odd, put the letter into oddStr. Return the even/odd strings
Sample: "helloworld" "2435232399"
gives evenStr="heoo" oddStr="llwrld"
'''
def two_strings_even_odd(str1,str2):
        evenStr1 = ""
        oddStr1 = ""
        #evenStr2 = ""
        #oddStr2 = ""
        for x in range(len(str2)):
                toCheck = int(str2[x]) % 2
                if toCheck == 0:
                        evenStr1 += str1[x]
                        #evenStr2 += str2[x]
                else:
                        oddStr1 += str1[x]
                        #oddStr2 += str2[x]
        return evenStr1, oddStr1




'''
7.
The number 6 is a truly great number. Given two int values, a and b, return True
if either one is 6. Or if their sum or difference is 6.
Note: the function abs(num) computes the absolute value of a number.

love6(6, 4) returns True
love6(4, 5) returns False
love6(1, 5) returns True
'''
def love6(a,b):
        if a == 6:
                return True
        elif b == 6:
                return True
        elif abs(a - b) == 6:
                return True
        elif abs(b - a) == 6: 
                return True
        elif abs(b + a) == 6: 
                return True
        else:
                return False


'''
########
#8. ISBN number

#As you know, every book has an unique ISBN number (International Standard Book Number).
#It is a 10-digit (or 13) code that uniquely specifies a book. Since this number is long, the right most digit is actually a "checksum"
#to roughly check if all the digits are correct (not mis-typed etc.) and forming a legit ISBN number. (checksum is also used in other places, like credit card number.)
#The rule is: when adding all the (10 numbers * its position (rightmost be position 1, leftmost be 10)) together, the sum should be divisible by 10. (For a real ISBN, they actually use 11. To make our program simple, we will use 10. If you are interested, read under "ISBN 10" on https://en.wikipedia.org/wiki/Check_digit)
#For example: ISBN 020131452-7 is legit since:
#               (0*10 + 2*9 + 0*8 + 1*7 + 3*6 + 1*5 + 4*4 + 5*3 + 2*2 + 7*1)%10 = 90%10 = 0 the sum 90 is divisible by 10
#In fact, the cool thing is that the checksum (rightmost 7) is the only single digit number that can satisfy this rule. In other words, if you know the first
#9 digit, you can calculate the checksum (last digit). In this problem, you will be calculte the checksum of an ISBN number.
#########
'''
'''
Helper function 1: check_legit_ISBN
Input: a list with 10 single digit number in it
Output: return "Legit" if the 10 digits form a legit ISBN number
        return "Not Legit" otherwise

Sample: [0,2,0,1,3,1,4,5,2,7] should return "Legit"
        [0,2,0,1,3,1,4,5,2,3] should return "Not Legit"

'''
def check_legit_ISBN(ISBNLis):
        runningTotal = 0
        for x in range(len(ISBNLis)):
                #print(runningTotal)
                runningTotal = runningTotal + (ISBNLis[x] * (x))
        
        #runningTotal = runningTotal % 10 
        if runningTotal % 10 == 0:
                return "legit"
        else:
                return "Not legit" 



'''
Helper func 2: format output
input: a list with 10 numbers in it
output: format it to the correct ISBN format and return it
Sample:
[0,2,0,1,3,1,4,5,2,7] will become: "ISBN 020131452-7"
'''
def format_ISBN(ISBNLis):
        retStr = "ISBN "
        for x in range(len(ISBNLis)):
                if x == (len(ISBNLis) - 1):
                        retStr += "-"
                retStr += str(ISBNLis[x])
        
        return retStr

'''
Helper func 3: checksum_ISBN
Input: a list with 9 single digit number in it (first 9 digit in ISBN)
Output: print out: "The correct checksum digit is:__. Now we have a legit ISBN: _____"
Hint: just loop through 0,1,2...X (X represents 9), test every one with helper func1 to find out the one checksum that forms a legit ISBN
with the correct ISBN in lis (10 numbers), call helper func2 to format it correctly. Then print the final result.
(Technical googling practice - google how to append or remove an element from a list)
'''
def checksum_ISBN(partISBN):
        for x in range(9):
                partISBN.append(x)
                if check_legit_ISBN(partISBN) == "legit":
                        #print(check_legit_ISBN(partISBN))
                        #print(format_ISBN(partISBN))
                        print("The correct checksum digit is: ", end="")
                        print(x, end="")
                        print(" Now we have a legit ISBN: ", end="")
                        print(partISBN)
                        break
                else:
                        del partISBN[9]
        
'''
Main Func: Generate a ISBN by:
add 9 random nunmbers into a list
(Technical googling practice - how to generate random numbers?)
call helper func 3 to find the checksum

Repeat 10 times
Generate 10 good ISBN numbers with one function call (not 10 digits for 1 ISBN)
Sample:
The correct checksum digit is:0. Now we have a legit ISBN:123456789-0 
The correct checksum digit is:0. Now we have a legit ISBN:987654321-0 
etc.
'''
def generate_ten_ISBNs():
        for x in range(10):
                randomlist = []
                for i in range(0,9):
                        n = random.randint(0,9)
                        randomlist.append(n)
                checksum_ISBN(randomlist)

        



if __name__ == '__main__':
    print("****Question 1****")
    #you can add your functions calls here
    #Please keep all the function calls and result printing
    easy_hello_loop1_for(3)
    print("****Question 2****")
    print(smaller_value(3,2))
    print("****Question 3****")
    list = [1,2,3, "hello", "item"]
    print(my_len(list))
    print("****Question 4****")
    sampleCate = ['rt','asdf','ton','er','user']
    list1, list2, list3 = cate_letters(sampleCate)
    print(list1)
    print(list2)
    print(list3)
    print("****Question 5****")
    string1 = "hello"
    string2 = "12345"
    two_strings(string1,string2)
    print("****Question 6****")
    print(two_strings_even_odd("helloworld", "2435232399"))
    print("****Question 7****")
    print(love6(6,4))
    print(love6(4,5))
    print(love6(1,5))
    print("****Question 8****")
    list1 = [0,2,0,1,3,1,4,5,2,7]
    list2 = [0,2,0,1,3,1,4,5,2]
    #print(check_legit_ISBN(list1))
    #print(format_ISBN(list1))
    #checksum_ISBN(list2)
    generate_ten_ISBNs()









