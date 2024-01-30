from tkinter import *


def SetNuber():
    nm.config(text=var.get())


root = Tk()

var = StringVar()
frmLft = Frame(root)
rb1 = Radiobutton(frmLft, text="Ваня", variable=var, value='+88005553535', indicatoron=0, command=SetNuber, width=10, height=1)
rb2 = Radiobutton(frmLft, text="Катя", variable=var, value='+88239232913', indicatoron=0, command=SetNuber, width=10, height=1)
rb3 = Radiobutton(frmLft, text="Никита", variable=var, value='+892011083293', indicatoron=0, command=SetNuber, width=10, height=1)
nm = Label(root, text="", width=20)

frmLft.pack(side=LEFT)
rb1.pack()
rb2.pack()
rb3.pack()
nm.pack(side=RIGHT)

root.mainloop()
