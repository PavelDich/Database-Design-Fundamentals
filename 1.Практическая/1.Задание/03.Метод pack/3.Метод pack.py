from tkinter import *


def Red():
    leb['text'] = 'красный'
    ent.delete(0, END)
    ent.insert(0, 'FF0000')


def Orange():
    leb['text'] = 'ораньжевый'
    ent.delete(0, END)
    ent.insert(0, 'FF7F00')


def Yellow():
    leb['text'] = 'жолтый'
    ent.delete(0, END)
    ent.insert(0, 'FFFF00')


def Green():
    leb['text'] = 'зеленый'
    ent.delete(0, END)
    ent.insert(0, '00FF00')


def Gay():
    leb['text'] = 'голубой'
    ent.delete(0, END)
    ent.insert(0, '00FFFF')


def Blue():
    leb['text'] = 'синий'
    ent.delete(0, END)
    ent.insert(0, '0000FF')


def Purple():
    leb['text'] = 'фиолетовый'
    ent.delete(0, END)
    ent.insert(0, 'FF00FF')


root = Tk()

out = 2

frm = Frame(root, padx=out, pady=out)
frmBut = Frame(frm, padx=out, pady=out)
leb = Label(frm, text='', width=20)
ent = Entry(frm, width=20)
butRed = Button(frmBut, width=4, height=2, bg='#FF0000', command=Red)
butOrange = Button(frmBut, width=4, height=2, bg='#FF7F00', command=Orange)
butYellow = Button(frmBut, width=4, height=2, bg='#FFFF00', command=Yellow)
butGreen = Button(frmBut, width=4, height=2, bg='#00FF00', command=Green)
butGay = Button(frmBut, width=4, height=2, bg='#00FFFF', command=Gay)
butBlue = Button(frmBut, width=4, height=2, bg='#0000FF', command=Blue)
butPurple = Button(frmBut, width=4, height=2, bg='#FF00FF', command=Purple)

frm.pack()
frmBut.pack(side=BOTTOM)
leb.pack()
ent.pack()
butRed.pack(side=LEFT, padx=out, pady=out)
butOrange.pack(side=LEFT, padx=out, pady=out)
butYellow.pack(side=LEFT, padx=out, pady=out)
butGreen.pack(side=LEFT, padx=out, pady=out)
butGay.pack(side=LEFT, padx=out, pady=out)
butBlue.pack(side=LEFT, padx=out, pady=out)
butPurple.pack(side=LEFT, padx=out, pady=out)

root.mainloop()
