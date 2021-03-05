#Written by Eliseo Izazaga
#This is homework 4, this gui takes in text from
#one side of the input and displays it line by 
#line

from tkinter import * 
#import ScrolledText

class Gui:
    def __init__(self, root):
        self.lineCounter = 1
        self.master = root
        self.master.title("Lexical Analyzer for TinyPie")
        self.master.geometry('800x320+950+200')  #sets height and placement

        self.label = Label(self.master, text = "In Text")   #text label with padding, for the left text box
        self.label.grid(row = 0, column = 0, padx = 15, pady = 15, sticky = W)
       
        self.label2 = Label(self.master, text = "Lexical Analyzed Result") #label for the text box on the right
        self.label2.grid(row = 0, column = 4, padx = 15, pady = 15, sticky = W)

        self.inText1 = Text(self.master, height = 10, width = 40, bg = "white", fg = "black", bd = 4, font = "16")
        self.inText1.grid(row = 4, column = 0, padx = 15) #left text box
        
        self.inText2 = Text(self.master, height = 10, width = 40, bg = "white", fg = "black", bd = 4, font = "16")
        self.inText2.grid(row = 4, column = 4, padx = 15) #right text box

        #self.inText2.insert(float(1), "Hello")  #this inserts text into the text box at line 1, space 0

        self.CurLineLabel = Label(self.master, text = "Current Processing Line: ")
        self.CurLineLabel.grid(row = 5, column = 0, padx = 15, pady = 0, sticky = W)

        self.CurLineTextField = Entry(self.master)  #The text field box that shows the current line being read
        self.CurLineTextField.grid(row = 5, column = 0, padx = 20, pady = 0, sticky = E)

        #self.CurLineTextField.insert(1, "2") #this changes the number in the box

        self.NextLineButton = Button(self.master, text = "Next Line", command = self.clickNextLineButton)
        self.NextLineButton.grid(row = 6, column = 0, padx = 15, pady = 15, sticky = E)

        self.ExitButton = Button(self.master, text = "Exit", command = self.clickExit)
        self.ExitButton.grid(row = 6, column = 4, padx = 15, pady= 15, sticky = E)

    def clickNextLineButton(self):
        
        #toBeLookedAnalized = self.inText1.get()
        toBeLookedAnalized = self.inText1.get(str(float(self.lineCounter))+' linestart' ,str(float(self.lineCounter))+ ' lineend')
        print(toBeLookedAnalized)
        #self.inText2.insert(float(self.lineCounter), toBeLookedAnalized)
        self.inText2.insert(END, toBeLookedAnalized +'\n')
        print(self.lineCounter)
        self.CurLineTextField.delete(0, 'end')
        self.CurLineTextField.insert(0, str(self.lineCounter))
        self.lineCounter += 1
        print(self.lineCounter)

        #self.CurLineTextField.delete(0, 'end')  #clears the current text and gets it ready for the next
        #self.CurLineTextField.insert(0, "pressed")
        #self.CurLineTextField.delete(0, 'end')
    def clickExit(self):
        exit()


if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = Gui(myTkRoot)
    myTkRoot.mainloop()
