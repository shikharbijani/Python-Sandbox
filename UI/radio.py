from tkinter import *
flavour=["Butterscoth","Belgium Chocolate","Vanilla"]
window=Tk()
x=IntVar()
for i in range(len(flavour)):
    radio_button=Radiobutton(window,
                            text=flavour[i],
                            variable=x,
                            value=i,
                            indicatoron=0,
                            width=20
                            )
    radio_button.pack(anchor=W)
window.mainloop()
