import tkinter
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox


def insert_text():
    try:
        file_name = fd.askopenfilename()
        f = open(file_name)
        lines = f.readlines()
        textName.delete(1.0, END)
        textSurname.delete(1.0, END)
        textPhone.delete(1.0, END)
        textName.insert(1.0, lines[0])
        textSurname.insert(1.0, lines[1])
        textPhone.insert(1.0, lines[2])
        f.close()
    except:
        messagebox.showinfo("Ошибка", "Файл не загружен")


def extract_text():
    try:
        file_name = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),
                       ("HTML files", "*.html;*.htm"),
                       ("All files", "*.*")))
        f = open(file_name, 'w')
        s = ""
        s += textName.get(1.0, END)
        s += textSurname.get(1.0, END)
        s += textPhone.get(1.0, END)
        f.write(s)
        f.close()
    except:
        messagebox.showinfo("Ошибка", "Файл не сохранен")


def clear_text():
    if messagebox.askokcancel("Подтверждение", "Вы уверены, что хотите очистить текст?"):
        textName.delete(1.0, END)
        textSurname.delete(1.0, END)
        textPhone.delete(1.0, END)


root = Tk()
textName = Text(root, width=50, height=1, wrap="none")
textName.grid(row=0, column=0, columnspan=2, pady=5)
textSurname = Text(root, width=50, height=1, wrap=NONE)
textSurname.grid(row=1, column=0, columnspan=2, pady=5)
textPhone = Text(root, width=50, height=1, wrap=tkinter.NONE)
textPhone.grid(row=2, column=0, columnspan=2, pady=5)
ButOpen = Button(text="Открыть", command=insert_text)
ButOpen.grid(row=3, column=0, sticky=EW)
ButSave = Button(text="Сохранить", command=extract_text)
ButSave.grid(row=3, column=1, sticky=EW)
ButClear = Button(text="Очистить", command=clear_text)
ButClear.grid(row=4, column=0, columnspan=2, sticky=EW)

root.mainloop()
