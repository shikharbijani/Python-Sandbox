from tkinter import *

window=Tk()

canvas=Canvas(window,height=500,width=500)

# canvas.create_line(0,0,500,500,fill="blue",width=5)
# canvas.create_line(0,500,500,0,fill="red",width=5)
# canvas.create_rectangle(50,50,250,250)
# canvas.create_polygon(250,0,500,500,0,500,fill='yellow',outline="black")

canvas.create_arc(50,50,450,450,style=PIESLICE,start=180,extent=180)
canvas.create_arc(50,50,450,450,style=PIESLICE,extent=180,fill="red")
canvas.create_line(50,255,450,255,width=30,fill="black")

# canvas.create_arc(200,200,300,300,extent=180,fill="black")
# canvas.create_arc(200,200,300,300,start=180,extent=180,fill="black")

canvas.create_oval(200,200,300,300,fill="black")

# canvas.create_arc(210,210,290,290,extent=180,fill="white")
# canvas.create_arc(210,210,290,290,start=180,extent=180,fill="white")

canvas.create_oval(210,210,290,290,fill="white")

# canvas.create_arc(215,215,285,285,extent=180,fill="white")
# canvas.create_arc(215,215,285,285,start=180,extent=180,fill="white")

canvas.create_oval(215,215,285,285,fill="white")

canvas.pack()
window.mainloop()