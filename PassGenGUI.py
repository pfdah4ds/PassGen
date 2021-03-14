from tkinter import *
import random as rnd


root = Tk()

welcomeLabel = Label(root, text = "Welcome to password generator")
welcomeLabel.pack()

requestLabel = Label(root, text = "Enter the length of the password")
requestLabel.pack()


inputEntry = Entry(root, width = 20)
inputEntry.pack()

def passGen(inp):
	upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	lower = 'abcdefghijklmnopqrstuvwxyz'
	numbs = '1234567890'
	symbs = '!@#$&*()+_-][{}.,'
	allof = upper + lower + numbs + symbs
	return ''.join(rnd.sample(allof,inp))

def clicks():
	passw = passGen(int(inputEntry.get()))
	resultLabel = Label(root, text = passw)
	resultLabel.pack()

myButton = Button(root, text = "Generate your Password", command = clicks)
myButton.pack()


root.mainloop()