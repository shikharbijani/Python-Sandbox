from tkinter import *
from tkinter import filedialog
def open_file():
    filepath=filedialog.askopenfilename(initialdir="Documents",
                                        filetypes=(("Text files","*.txt"),("all files","*.*")))

    file=open(filepath,'r')
    print(file.read())
    file.close()
    
window=Tk()

button=Button(window,text="Open",command=open_file)
button.pack()

window.mainloop()