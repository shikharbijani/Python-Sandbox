from tkinter import *

def display():
    if x.get():
        print("Shouldn't have done that!")
    else:
        print("Come ON!")

window=Tk()
x=BooleanVar()
check_button=Checkbutton(window,
                         text="Select",
                         variable=x,
                         onvalue=True,
                         offvalue=False,
                         command=display)
check_button.pack()
window.mainloop()