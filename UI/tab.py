from tkinter import *
from tkinter import ttk

window=Tk()

notebook=ttk.Notebook(window)

tab1=Frame(notebook)
tab2=Frame(notebook)
tab3=Frame(notebook)

notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")
notebook.add(tab3,text="Tab 3")
notebook.pack(expand=True,fill=BOTH)

Label(tab1,text="Hello").pack()
Label(tab2,text="World").pack()

window.mainloop()