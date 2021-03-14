#Importing
from tkinter import *


#Creating root widget
root = Tk()
myLabel1 = Label(root, text = "Hello World!")
myLabel2 = Label(root, text = "Jello told you :")
 
e = Entry(root, width = 4)
e.grid(row = 0, column = 2)

def myClick():
	myLabel = Label(root, text = "You clicked!")
	myLabel.grid(row = 4, column = 0)
	#myLabel.pack()

myButton = Button(root, text = "Click Me!",command = myClick, width = 50)


myLabel1.grid(row = 0, column = 0)
myLabel2.grid(row = 2, column = 0)
#myButton.pack()#pack cannot be used with grid

myButton.grid(row = 3, column = 0, padx = 50)
root.mainloop()