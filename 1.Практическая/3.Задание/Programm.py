import tkinter
from tkinter import *
import customtkinter
from customtkinter import *

global UserName


def open_programm():
    def Plus():
        try:
            s = str(float(num1.get()) + float(num2.get()))
        except:
            s = 'Value error'
        tex.configure(text=' '.join(str(s)))

    def Minus():
        try:
            s = str(float(num1.get()) - float(num2.get()))
        except:
            s = 'Value error'
        tex.configure(text=' '.join(str(s)))

    def Multiply():
        try:
            s = str(float(num1.get()) * float(num2.get()))
        except:
            s = 'Value error'
        tex.configure(text=' '.join(str(s)))

    def Devide():
        try:
            s = str(float(num1.get()) / float(num2.get()))
        except:
            s = 'Value error'
        tex.configure(text=' '.join(str(s)))

    tkLogin.destroy()
    root = CTk()
    root.title("Смена цвета")
    root.geometry("300x250")

    LabelUserName = CTkLabel(root, text=str(UserName), width=20, fg_color="transparent")
    LabelUserName.pack(side=TOP, padx=10, pady=10)
    frameCulculater = CTkFrame(root)
    frameCulculater.pack(side=TOP)

    num1 = CTkEntry(frameCulculater, width=100)
    num2 = CTkEntry(frameCulculater, width=100)
    tex = CTkLabel(frameCulculater, text=' ', width=20, fg_color="transparent")
    butPlus = CTkButton(frameCulculater, text="+", width=20, command=Plus)
    butMinus = CTkButton(frameCulculater, text="-", width=20, command=Minus)
    butMultiply = CTkButton(frameCulculater, text="*", width=20, command=Multiply)
    butDevide = CTkButton(frameCulculater, text="/", width=20, command=Devide)

    num1.grid(row=0, column=0, columnspan=1, pady=5, sticky=EW)
    num2.grid(row=0, column=1, columnspan=1, pady=5, sticky=EW)
    tex.grid(row=1, column=0, columnspan=2, pady=5, sticky=EW)
    butPlus.grid(row=2, column=0, columnspan=1, pady=5, sticky=EW)
    butMinus.grid(row=2, column=1, columnspan=1, pady=5, sticky=EW)
    butMultiply.grid(row=3, column=0, columnspan=1, pady=5, sticky=EW)
    butDevide.grid(row=3, column=1, columnspan=1, pady=5, sticky=EW)

    root.mainloop()


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
                global UserName
                UserName = lines[i]
                print("entered", UserName)
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
