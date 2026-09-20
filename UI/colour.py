from tkinter import *
from tkinter import colorchooser

def color():
    color=colorchooser.askcolor()
    window.config(bg=color[1])
    # window.config(bg=colorchooser()[1])

window=Tk()
window.geometry("480x480")

button=Button(window,text="click!",command=color)
button.pack()

window.mainloop()