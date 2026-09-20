from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title="hmmm",message="Yo")
    # messagebox.showwarning(title="Defender",message="You Have A VIRUS!")
    # messagebox.showerror(title="Error",message="404")
    # if messagebox.askokcancel(title="Sure?",message="You wanna do the things?"): #aksyesno,askokcancle works the same
    #     print("You Did It!")
    # else:
    #     print(":(")
    # print(messagebox.askquestion(title="Question?",message="You Like Me?"))
    print(messagebox.askyesnocancel(title="NYC",message="New York City"))

window=Tk()

button=Button(window,text="Click Me",command=click)
button.pack()

window.mainloop()