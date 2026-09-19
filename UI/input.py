from tkinter import *
def submit():
    username=entry.get()
    print(f"Hello {username}!")
    # entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)

window=Tk()
entry=Entry(window,
            font=("Arial",20),
            relief=GROOVE,
            show="*")
# entry.insert(0,"Example")
entry.pack(side=LEFT)

submit_button=Button(window,
                     command=submit,
                     font=("Arial",10,"bold"),
                     text="Submit")
submit_button.pack(side=RIGHT)

clear_button=Button(window,
                     text="Clear",
                     font=("Arial",10,"bold"),
                     command=delete)
clear_button.pack(side=RIGHT)

backspace_button=Button(window,
                     text="Backspace",
                     font=("Arial",10,"bold"),
                     command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()
