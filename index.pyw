from Tkinter import *
import os
from distutils.core import setup

def login():
    top.destroy()
    #setup(console=['login.pyw'])
    os.system('python login.pyw')
def Signup():
    top.destroy()
    os.system('python signup.pyw')
#Create a window
top = Tk()
top.title("ANSH ChAt BoT")
top.geometry("300x130")
top.resizable(width=FALSE, height=FALSE)

L1 = Label(top, text="Registered user ?")
L2 = Label(top, text="New User ?")

SendButton = Button(top, font=30, text="Login", width='5', height='1',
                    bd=0, bg="#FFBF00", activebackground="#FACC2E",command=login)
SendButton.place(x=50, y=50)

SendButton1 = Button(top, font=30, text="SignUp", width='5', height='1',
                    bd=0, bg="#FFBF00", activebackground="#FACC2E",command=Signup)
SendButton1.place(x=200, y=50)

L1.place(x=30,y=20)
L2.place(x=200,y=20)

top.mainloop()
