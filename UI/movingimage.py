from tkinter import *

def forward(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)

def downward(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()+10)

def left(event):
    label.place(x=label.winfo_x()-10,y=label.winfo_y())

def right(event):
    label.place(x=label.winfo_x()+10,y=label.winfo_y())

window=Tk()
window.geometry("960x1080")

window.bind("<w>",forward)
window.bind("<s>",downward)
window.bind("<a>",left)
window.bind("<d>",right)
myimage=PhotoImage(file="C:\\Users\\LOX\\Downloads\\MP4-4-Real-Painting-3980336820.png")


label=Label(window,image=myimage)
label.place(x=0,y=0)
window.mainloop()