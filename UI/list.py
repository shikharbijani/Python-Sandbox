from tkinter import *
flavour=["Butterscotch","Belguim Chocolate","Vanilla"]

def submit():
    order=[]
    for i in listbox.curselection():
        order.insert(i,listbox.get(i))
    print("You have Ordered:")
    for item in order:
        print(item)

def add():
    listbox.insert(listbox.size(),entry_box.get())
    listbox.config(height=listbox.size())
    entry_box.delete(0,END)

def delete():
    for item in reversed(listbox.curselection()):
        listbox.delete(item)
    listbox.config(height=listbox.size())
window=Tk()

listbox=Listbox(window,
                font=("Constantia",15),
                width=20,
                selectmode=MULTIPLE)
listbox.pack()
for i in range(len(flavour)):
    listbox.insert(i+1,flavour[i])

listbox.config(height=listbox.size())

entry_box=Entry(window,font=("Constantia",15))
entry_box.pack()

submit_button=Button(window,text="Submit",command=submit)
submit_button.pack()

add_button=Button(window,text="Add",command=add)
add_button.pack()

delete_button=Button(window,text="Delete",command=delete)
delete_button.pack()
window.mainloop()