from tkinter import *

def resize_text_widget():
    width = width_entry.get()
    height = height_entry.get()
    text_widget.config(width=int(width), height=int(height))

def change_bg_color(event):
    if event.type == '7':  # FocusIn event
        text_widget.config(bg='white')
    else:  # FocusOut event
        text_widget.config(bg='lightgrey')

root = Tk()

intp = Frame(root)
boot = Frame(intp)

intp.pack(side=TOP)
boot.pack(side=RIGHT)

width_entry = Entry(intp)
width_entry.pack()

height_entry = Entry(intp)
height_entry.pack()

resize_button = Button(boot, text='Resize', command=resize_text_widget)
resize_button.pack(side=RIGHT)

text_widget = Text(root, bg='lightgrey')
text_widget.pack()

width_entry.bind('<Return>', lambda event: resize_text_widget())
height_entry.bind('<Return>', lambda event: resize_text_widget())
text_widget.bind('<FocusIn>', change_bg_color)
text_widget.bind('<FocusOut>', change_bg_color)

root.mainloop()