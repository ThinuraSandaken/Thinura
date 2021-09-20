import time
from tkinter import *

root= Tk()

root.geometry("350x150+0+0")
root.title("Clock")

root.configure(background="pink")

root.resizable(0, 0)



def start():
    text= time.strftime("%H:%M:%S")
    label.config(text=text)
    label.after(100,start)


label=Label(root,font=("DS-digital",50),bg='pink',fg='blue',bd=50)
label.grid(row=0,column=1)
start()
print("done")
root.mainloop()
