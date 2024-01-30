from tkinter import *

root = Tk()


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


leb = Label(root, text='', width=20)
ent = Entry(root, width=20)
butRed = Button(root, width=20, bg='#FF0000', command=Red)
butOrange = Button(root, width=20, bg='#FF7F00', command=Orange)
butYellow = Button(root, width=20, bg='#FFFF00', command=Yellow)
butGreen = Button(root, width=20, bg='#00FF00', command=Green)
butGay = Button(root, width=20, bg='#00FFFF', command=Gay)
butBlue = Button(root, width=20, bg='#0000FF', command=Blue)
butPurple = Button(root, width=20, bg='#FF00FF', command=Purple)

leb.pack()
ent.pack()
butRed.pack()
butOrange.pack()
butYellow.pack()
butGreen.pack()
butGay.pack()
butBlue.pack()
butPurple.pack()

root.mainloop()
