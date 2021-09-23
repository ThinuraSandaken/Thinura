import tkinter as tk

OptionList1 = [
"KG",
"GR",

]

def Ok():

    chicken = variable.get()


    amount = float(e1.get())

    if (chicken == "KG" ):

        tot = amount * 100

    else:
        tot = amount/1000 * 100

    nsalText.set(tot)

root = tk.Tk()
root.geometry('300x200')
root.title("Chicken Shop System Python")

variable = tk.StringVar(root)
variable.set(OptionList1[0])

opt = tk.OptionMenu(root, variable, *OptionList1)
variable1 = tk.StringVar(root)
opt.config(width=10, font=('Helvetica', 12))
opt.pack(side="top")

global e1
global nsalText
nsalText = tk.StringVar()
labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")


tk.Label(root, text="Chicken ").place(x=10, y=10)

tk.Label(root, text="Qty").place(x=10, y=80)

tk.Label(root, text="Total:").place(x=10, y=150)
tk.Label(root, text="", font=('Helvetica', 20), fg='red' , textvariable=nsalText).place(x=100, y=150)
tk.Button(root, text="Cal", command=Ok ,height = 1, width = 3).place(x=100, y=110)

e1 = tk.Entry(root)
e1.place(x=80, y=80,)

root.mainloop()
