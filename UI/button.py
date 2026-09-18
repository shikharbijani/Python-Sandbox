from tkinter import *
def click():
    print("A Cutie Pie!")
window=Tk()
photo=PhotoImage(file="C:\\Users\\LOX\\Downloads\\thinking-face-emoji-png-3619646795.png")
button=Button(window,
              text="What am I?",
              command=click,
              font=("Comic Stans",
                    30,"italic"),
                    fg="White",
                    bg="Black",
                    activebackground="Black",
                    activeforeground="White",
                    relief=RAISED,
                    bd=20,
                    padx=20,
                    pady=10,
                    # state=DISABLED,
                    image=photo,
                    compound="bottom")
button.pack()

window.mainloop()