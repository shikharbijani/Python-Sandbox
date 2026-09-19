from tkinter import *
def submit():
    print(f"Tempearture is {scale.get()} degree")
window=Tk()
scale=Scale(window,
            from_=100,to=0,
            length=200,
            orient=VERTICAL,
            font=("Consolar",10,"bold"),
            tickinterval=10,
            showvalue=0,
            resolution=5,
            troughcolor="Black")
scale.set(50)
scale.pack()

button=Button(window,text="Submit",command=submit)
button.pack()
window.mainloop()