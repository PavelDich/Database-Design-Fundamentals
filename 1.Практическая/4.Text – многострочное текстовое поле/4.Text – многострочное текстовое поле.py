from tkinter import *


#
#                   LOGIC
#

def DataOpen():
    name = entry
    content = text
    a = str(name.get(1.0, END))
    file = open(a[0:len(a) - 1], 'r')
    content.delete(1.0, END)
    content.insert(1.0, file.read())
    file.close()

    print('File', a[0:len(a) - 1], 'is opened.')


def DataSave():
    name = entry
    content = text
    a = str(name.get(1.0, END))
    file = open(a[0:len(a) - 1], 'w')
    file.write(str(content.get(1.0, END)))
    file.close()

    print('File', a[0:len(a) - 1], 'is saved.')


#
#                   INTERFACE
#

root = Tk()

#   TEXT

frmOut = Frame(root)
entry = Text(frmOut, width=20, height=1)
ButOpen = Button(frmOut, command=DataOpen, text="Открыть", width=10, height=1)
ButSave = Button(frmOut, command=DataSave, text="Сохранить", width=10, height=1)
frmOut.pack(side=TOP)
entry.pack(side=LEFT)
ButOpen.pack(side=LEFT)
ButSave.pack(side=LEFT)

#   SCROLL

frmIn = Frame(root)
frmInT = Frame(frmIn)
text = Text(frmInT, wrap=NONE, width=40, height=20)
text.pack(side=LEFT)

scrolly = Scrollbar(frmInT, command=text.yview)
scrolly.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scrolly.set)

scrollx = Scrollbar(frmIn, command=text.xview, orient=HORIZONTAL)
scrollx.pack(side=BOTTOM, fill=X)
text.config(xscrollcommand=scrollx.set)

frmIn.pack(side=BOTTOM)
frmInT.pack(side=TOP)

root.mainloop()
