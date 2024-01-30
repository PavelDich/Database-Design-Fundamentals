from tkinter import *

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

root = Tk()

goods_listbox = Listbox(root, selectmode=MULTIPLE)
goods_listbox.pack(side=LEFT)
goods = ['apple','bananas','carrot','bread','butter','meat','potato','pineaplle','tomato','milk']
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

root.mainloop()