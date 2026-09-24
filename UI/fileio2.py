from tkinter import *
from tkinter import filedialog

def savefile():
    file=filedialog.asksaveasfile(initialdir="Document",
                                  defaultextension=".txt",
                                  filetypes=[("Text file",".txt"),
                                             ("HTML file",".html"),
                                             ("All files",".*")])
    # filetext=str(text.get("1.0",END))
    filetext=input("Enter Some Msg: ")
    file.write(filetext)
    file.close
    

window=Tk()

button=Button(window,text="Save",command=savefile)
button.pack()
text=Text(window,font=("Roma",15))
text.pack()
window.mainloop()