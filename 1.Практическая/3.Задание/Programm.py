import tkinter
from tkinter import *
from tkinter import ttk


def open_programm():
    def close_programm():
        root.destroy()

    def move_to_shopping_list():
        selected = goods_listbox.curselection()
        for index in selected[::-1]:
            shopping_listbox.insert(END, goods_listbox.get(index))
            goods_listbox.delete(index)

    def move_to_goods_list():
        selected = shopping_listbox.curselection()
        for index in selected[::-1]:
            goods_listbox.insert(END, shopping_listbox.get(index))
            shopping_listbox.delete(index)

    tkLogin.destroy()
    root = Tk()
    root.title("Смена цвета")
    root.geometry("300x250")

    goods_listbox = Listbox(root, selectmode=MULTIPLE)
    goods_listbox.pack(side=LEFT)
    goods = ['apple', 'bananas', 'carrot', 'bread', 'butter', 'meat', 'potato', 'pineaplle', 'tomato', 'milk']
    for item in goods:
        goods_listbox.insert(END, item)

    shopping_listbox = Listbox(root, selectmode=MULTIPLE)
    shopping_listbox.pack(side=RIGHT)

    boot = Frame(root)

    boot.pack(side=RIGHT)

    to_shopping_button = Button(boot, text='>>', command=move_to_shopping_list)
    to_shopping_button.pack()

    to_goods_button = Button(boot, text='<<', command=move_to_goods_list)
    to_goods_button.pack()



def ChekUser():
    login = LoginEntry.get()
    password = PasswordEntry.get()

    f = open("Data.txt")
    lines = f.readlines()
    for i in range(len(lines)):
        if i % 2 == 1:
            continue
        if login.lower().strip() == lines[i].lower().strip():
            if password.lower().strip() == lines[i + 1].lower().strip():
                print("entered")
                open_programm()


def AddUser():
    login = LoginEntry.get()
    password = PasswordEntry.get()

    f = open("Data.txt")
    lines = f.readlines()
    for i in range(len(lines)):
        if i % 2 == 1:
            continue
        if login.lower().strip() == lines[i].lower().strip() and login != None:
            print("login is invalid")
            return
        if password.lower().strip() == lines[i + 1].lower().strip() and password != None:
            print("password is invalid")
            return
    f = open("Data.txt")
    t = f.read()
    f = open("Data.txt", 'w')
    t += login + "\n" + password + "\n"
    f.write(t)
    f.close()


try:
    f = open("Data.txt")
    f.close()
except:
    f = open("Data.txt", 'w')
    f.write("admin\nadmin\n")
    f.close()

tkLogin = Tk()
tkLogin.title("Вход")
tkLogin.geometry("250x200")

FrameText = Frame()
FrameText.pack(side=TOP)
LoginLabel = Label(FrameText, text="Логин: ")
LoginLabel.grid(row=0, column=0, columnspan=1, pady=5)
LoginEntry = Entry(FrameText)
LoginEntry.grid(row=0, column=1, columnspan=1, pady=5)
PasswordLabel = Label(FrameText, text="Пароль: ")
PasswordLabel.grid(row=1, column=0, columnspan=1, pady=5)
PasswordEntry = Entry(FrameText)
PasswordEntry.grid(row=1, column=1, columnspan=1, pady=5)

FrameControl = Frame()
FrameControl.pack(side=BOTTOM)
buttonAdd = Button(FrameControl, text="Создать", command=AddUser)
buttonAdd.grid(row=0, column=0, columnspan=1, pady=5)
buttonChek = Button(FrameControl, text="Войти", command=ChekUser)
buttonChek.grid(row=0, column=1, columnspan=1, pady=5)

tkLogin.mainloop()
