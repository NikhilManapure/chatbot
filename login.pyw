from Tkinter import *
import fileinput
import os
from tkMessageBox import *
import sqlite3
conn = sqlite3.connect('login.db')
c = conn.cursor()

#Initiate Window
WindowTitle = 'ANSH ChAt BoT'

def check():
    logfile = open('name.txt', 'w')
    temp = name.get().upper()
    temp2=passw.get().upper()
    if temp!="" and temp2!="":
        logfile.write(temp)
        logfile.close()
        m=0
        for row in c.execute("SELECT * FROM user where name='"+temp+"' and pass='"+temp2+"'"):
            m=1
        if m==1:
            print "success"
            conn.close()
            top.destroy()
            #execfile('host.pyw')
            os.system('python host.pyw')
        else:
            showerror('Error!!', "Invalid Username/Password")
            name.delete("0.0",END)
            passw.delete("0.0",END)
    else:
        showerror('Error!!', "Enter Username/Password")
def PressAction(event):
    passw.config(state=NORMAL)
    check()
def DisableEntry(event):
    passw.config(state=DISABLED)



#Create a window
top = Tk()
top.title(WindowTitle)
top.geometry("300x130")
top.resizable(width=FALSE, height=FALSE)

L1 = Label(top, text="User Name")
name= Entry(top, bd=5)
L2 = Label(top, text="Password")
passw= Entry(top, bd=5, show='*')

passw.bind("<Return>", DisableEntry)
passw.bind("<KeyRelease-Return>", PressAction)

#Create the Button to send message
SendButton = Button(top, font=30, text="login", width='5', height='1',
                    bd=0, bg="#FFBF00", activebackground="#FACC2E",command=check)

SendButton.place(x=100, y=80)

L1.place(x=30,y=20)
L2.place(x=30,y=50)
name.place(x=100,y=20)
passw.place(x=100,y=50)
top.mainloop()
