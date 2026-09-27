from tkinter import *

def doSomething(event):
    print(f"Pressed: {event.x}, {event.y}")

window=Tk()

# window.bind("<Button-1>",doSomething) #LEFT
# window.bind("<Button-2>",doSomething) #MIDDLE
# window.bind("<Button-3>",doSomething) #RIGHT
# window.bind("<ButtonRelease>",doSomething)
# window.bind("<Enter>",doSomething)
# window.bind("<Leave>",doSomething)
window.bind("<Motion>",doSomething)
window.mainloop()
