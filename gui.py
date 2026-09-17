import tkinter as tk
from tkinter import *

window=tk.Tk()
window.geometry("420x420")
window.title("GUI")
# window.config(background="black")
photo=PhotoImage(file="C:\\Users\\LOX\\Pictures\\Screenshots\\Screenshot (5).png")
label=Label(window,
            text="This is The Grid",
            font=("Arial",40,"bold"),
            fg="White",
            bg="Black",
            relief=SUNKEN,
            bd=10,
            padx=30,
            pady=10,
            image=photo,
            compound="top")
# label.place(x=0,y=0)
label.pack()
window.mainloop()