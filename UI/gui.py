import tkinter as tk
from tkinter import *

window=tk.Tk()
window.geometry("420x420")              #Window Size
window.title("GUI")                     #Window Title
# window.config(background="black")     #Background Colour
photo=PhotoImage(file="C:\\Users\\LOX\\Pictures\\Screenshots\\Screenshot (5).png")  #Photo Path
label=Label(window,
            text="This is The Grid",    #Text of Higlight
            font=("Arial",40,"bold"),   #Font
            fg="White",                 #Foreground Colour
            bg="Black",                 #Background Colour
            relief=SUNKEN,              #Boder Style
            bd=10,                      #Boder Widht
            padx=30,                    #Gap Between Text and x axis of Boder
            pady=10,                    #Gap BEtween Text and y axis of Boder
            image=photo,                #Image
            compound="bottom")          #Position of Image
# label.place(x=0,y=0)                  #Position of Text
label.pack()                            #display label
window.mainloop()