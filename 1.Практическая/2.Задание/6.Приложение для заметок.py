from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox


def insert_text():
    try:
        file_name = fd.askopenfilename()
        f = open(file_name)
        s = f.read()
        text.insert(1.0, s)
        f.close()
    except:
        messagebox.showinfo("Ошибка", "Файл не загружен")


def extract_text():
    try:
        file_name = fd.asksaveasfilename(
            filetypes=(("TXT files", "*.txt"),))
        f = open(file_name+".txt", 'w')
        s = text.get(1.0, END)
        f.write(s)
        f.close()
    except:
        messagebox.showinfo("Ошибка", "Файл не сохранен")


def clear_text():
    if messagebox.askokcancel("Подтверждение", "Вы уверены, что хотите очистить текст?"):
        text.delete(1.0, END)


root = Tk()
text = Text(root, width=50, height=25, wrap="none")
text.grid(row=0, column=0, columnspan=2, pady=5)
ButOpen = Button(text="Открыть", command=insert_text)
ButOpen.grid(row=3, column=0, sticky=EW)
ButSave = Button(text="Сохранить", command=extract_text)
ButSave.grid(row=3, column=1, sticky=EW)
ButClear = Button(text="Очистить", command=clear_text)
ButClear.grid(row=4, column=0, columnspan=2, sticky=EW)

root.mainloop()