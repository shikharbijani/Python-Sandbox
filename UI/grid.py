from tkinter import *

def done():
    print(f"First Name: {firstNameEntry.get()}")
    print(f"Last Name: {lastNameEntry.get()}")
    print(f"Email: {emailEntry.get()}")

window=Tk()

titlelabe=Label(window,text="Enter Info",font=("",10,"bold")).grid(row=0,column=0,columnspan=2)

firstNameLabel=Label(window,text="Enter First Name:").grid(row=1,column=0)
firstNameEntry=Entry(window)
firstNameEntry.grid(row=1,column=1)

lastNameLabel=Label(window,text="Enter last Name:").grid(row=2,column=0)
lastNameEntry=Entry(window)
lastNameEntry.grid(row=2,column=1)

emailLabel=Label(window,text="Enter Email Name:").grid(row=3,column=0)
emailEntry=Entry(window)
emailEntry.grid(row=3,column=1)
donebutton=Button(window,text="Done",command=done).grid(row=4,column=0,columnspan=2)

window.mainloop()