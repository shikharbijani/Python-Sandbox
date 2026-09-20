from tkinter import *

def click():
    input=text.get("1.0",END)
    print(input)

window=Tk()
text=Text(window,font=("roman",15,"italic"))
text.pack()

button=Button(window,text="click",command=click)
button.pack()

window.mainloop()