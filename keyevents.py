from tkinter import *
def doSomething(event):
    # print(f"You Pressed {event.keysym}")
    label.config(text=event.keysym)

window=Tk()

window.bind("<Key>",doSomething)

label=Label(window,text="Press A Key",font=("",100))
label.pack()

window.mainloop()