from tkinter import *
from tkinter.ttk import *
import time

def download():
    Gb=10
    download=0
    speed=1
    while (download<Gb):
        time.sleep(0.5)
        bar["value"]+=(speed/Gb)*100
        download+=speed
        percent.set(f"{int(download/Gb*100)}%")
        downloads.set(f"{download}/{Gb} Gb completed!")
        window.update_idletasks()

window=Tk()

percent=StringVar()
downloads=StringVar()

bar=Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

precentlabrl=Label(window,textvariable=percent).pack()
tasklabrl=Label(window,textvariable=downloads).pack()

button=Button(window,text="Download",command=download).pack()
window.mainloop()