from tkinter import *

def add_to_list(event):
    text = entry.get()
    if text != "":
        listbox.insert(END, text)
        entry.delete(0, END)

def copy_to_entry(event):
    selected = listbox.curselection()
    if selected:
        text = listbox.get(selected)
        entry.delete(0, END)
        entry.insert(0, text)

root = Tk()

entry = Entry(root)
entry.pack()
entry.bind('<Return>', add_to_list)

listbox = Listbox(root)
listbox.pack()
listbox.bind('<Double-Button-1>', copy_to_entry)

root.mainloop()