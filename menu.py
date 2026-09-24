from tkinter import *


def openfile():
    print("File has been Opened!")

def savefile():
    print("FIle Saved!")

window=Tk()
menubar=Menu(window)
window.config(menu=menubar)

filemenu=Menu(menubar,tearoff=0)

menubar.add_cascade(label="File",menu=filemenu)

filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Save",command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=quit)

editmenu=Menu(menubar,tearoff=0)

menubar.add_cascade(label="Edit",menu=editmenu)

editmenu.add_command(label="Redo")
editmenu.add_command(label="Undo")
editmenu.add_separator()
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Cut")

window.mainloop()