from Tkinter import *
import fileinput
import os
import sqlite3
conn = sqlite3.connect('login.db')
c = conn.cursor()

#Initiate Window
WindowTitle = 'ANSH ChAt BoT'

def check():
    logfile = open('name.txt', 'w')
    temp = name.get().upper()
    temp2= passw.get().upper()
    if temp!="" and temp2!="":
        logfile.write(temp)
        logfile.close()
        # Insert a row of data
        c.execute("INSERT INTO user VALUES ('"+temp+"','"+temp2+"')")
        # Save (commit) the change
        conn.commit()
        top.destroy()
        #execfile('host.pyw')
        os.system('python login.pyw')
    else:
        showerror('Error!!', "wrong username or password")
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

L1 = Label(top, text="New username")
name= Entry(top, bd=5)
L2 = Label(top, text="Choose Password")
passw= Entry(top, bd=5, show='*')

passw.bind("<Return>", DisableEntry)
passw.bind("<KeyRelease-Return>", PressAction)

#Create the Button to send message
SendButton = Button(top, font=30, text="SignIn", width='5', height='1',
                    bd=0, bg="#FFBF00", activebackground="#FACC2E",command=check)

SendButton.place(x=130, y=80)

L1.place(x=30,y=20)
L2.place(x=30,y=50)
name.place(x=130,y=20)
passw.place(x=130,y=50)
top.mainloop()
