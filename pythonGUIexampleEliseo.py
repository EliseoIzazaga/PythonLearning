#by Eliseo Izazaga
#This is an example of using the tkinter python extension to create a basic window with button

from tkinter import *

class Catabase:
    def __init__(self):
        self.catLis = []
    def add_cat(self, catinfo):
        self.catLis.append(catinfo)
    def print_cat_database(self):
        print("**********************")
        print("The Catabase!")
        print("**********************")
        print("Cat Name, Cat ID")
        for x in self.catLis:
            print(x)


class MyFirstGUI: #class definition

    #This is the initialize function for a class.
    #Variables belonging to this class will get created and initialized in this function
    #What is the self parameter? It represents this class itself.
    #By using self.functionname, you can call functions belonging to this class.
    #By using self.variablename, you can create and use variables belonging to this class.
    #It needs to be the first parameter of all the functions in your class

    def __init__(self, root):

        self.catDatabase = Catabase()
        #Master is the default prarent object of all widgets.
        #You can think of it as the window that pops up when you run the GUI code.
        self.master = root
        self.master.title("My Cat Registration System")

        #grid function puts a widget at a certain location
        # return value is none, please do not use it like self.label=Label().grad()
        #it will make self.label=none and you will no longer be able to change the label's content
        self.label = Label(self.master, text="Cat Name: ")
        self.label.grid(row=0,column=0,sticky=E)

        self.catnameentry = Entry(self.master)
        self.catnameentry.grid(row=0, column=1, sticky =E)

        self.label = Label(self.master, text="Cat ID: ")
        self.label.grid(row=0,column=2,sticky=E)

        self.catId = Entry(self.master)
        self.catId.grid(row=0, column=3, sticky =E)
        
        self.submitbutton = Button (self.master, text="Submit Cat", command=self.submitname)
        self.submitbutton.grid(row=0,column=4, sticky=E)

        self.printCatabaseButton = Button (self.master, text="Print Catabase", command=self.catDatabase.print_cat_database)
        self.printCatabaseButton.grid(row=1,column=4, sticky=E)

        self.label = Label(self.master, text = "Registered Name: ")
        self.label.grid(row=1, column = 0, sticky = E)
        
        #self.label = Label(self.master, text = "Cat ID: ")
        #self.label.grid(row=1, column = 1, sticky = E)

        self.label = Label(self.master, text = "Registered ID: ")
        self.label.grid(row=1, column = 2, sticky = E)
        

    def submitname (self):
        print ("a cat name submitted ",end = "")
        print(self.catnameentry.get())
        #print(self.catId.get())

        inName = self.catnameentry.get() 
        inId = self.catId.get()

        if inName == '':
            print("invalid")
        elif inId == '':
            print("invalid")
        else:
            print("Valid")
            self.label = Label(self.master, text = inId)
            self.label.grid(row=1, column = 3, sticky = E)

            self.label = Label(self.master, text = inName)
            self.label.grid(row=1, column = 1, sticky = E)

            addToCataBaseTuple = (inName, inId)           

            #addToCataBase = "(" + inName + "," + inId + ")"
            self.catDatabase.add_cat(addToCataBaseTuple)
    








if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = MyFirstGUI(myTkRoot)
    myTkRoot.mainloop()














