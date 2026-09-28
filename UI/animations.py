from tkinter import *
import time
WIDTH=500
HEIGHT=500
xVelocity=3
yVelocity=2

window=Tk()
window.geometry("500x500")


canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

spaceimage=PhotoImage(file="C:\\Users\\LOX\\Downloads\\Space-PNG-HD.png")
space=canvas.create_image(0,0,image=spaceimage,anchor=NW)

photoimage=PhotoImage(file="C:\\Users\\LOX\\Downloads\\21-214655_ufo-icon-thane.png")
my_image=canvas.create_image(0,0,image=photoimage,anchor=NW)


image_width=photoimage.width()
image_height=photoimage.height()

while True:
    coord=canvas.coords(my_image)
    print(coord)
    if (0>coord[0] or coord[0]>(500-image_width)):
        xVelocity*=-1

    if (0>coord[1] or coord[1]>(500-image_height)):
        yVelocity*=-1

    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()