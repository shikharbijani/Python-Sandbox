from tkinter import *

def create_linked_window():
    new_lined_window=Toplevel() #Linked to bottom window

def create_window():
    new_window=Tk()
    window.destroy()

window=Tk()
Button(window,text="Open New Linked Window",command=create_linked_window).pack()
Button(window,text="Open New Window",command=create_window).pack()

window.mainloop()