from tkinter import *

def forward(event):
    canvas.move(myimage,0,-10)

def downward(event):
    canvas.move(myimage,0,10)

def left(event):
    canvas.move(myimage,-10,0)

def right(event):
    canvas.move(myimage,10,0)

window=Tk()

window.bind("<w>",forward)
window.bind("<s>",downward)
window.bind("<a>",left)
window.bind("<d>",right)

canvas=Canvas(window,width=500,height=500)
canvas.pack()

photoimage=PhotoImage(file="C:\\Users\\LOX\\Downloads\\MP4-4-Real-Painting-3980336820.png")

myimage=canvas.create_image(0,0,image=photoimage,anchor=NW)

window.mainloop()