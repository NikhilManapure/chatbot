import Tkinter as tk
import tkMessageBox
def ask_quit():
    if tkMessageBox.askokcancel("Quit", "You want to quit now? *sniff*"):
        root.destroy()
	execfile('host.pyw')
root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", ask_quit)
root.mainloop()
