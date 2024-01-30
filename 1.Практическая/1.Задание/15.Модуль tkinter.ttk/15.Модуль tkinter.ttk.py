import tkinter as tk
from tkinter import ttk

def change_color(event):
    selected_color = color_combo.get()
    canvas.config(bg=selected_color)

root = tk.Tk()
root.title("Color Changer")

# Создание выпадающего списка и добавление цветов
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
color_combo = ttk.Combobox(root, values=colors)
color_combo.pack(pady=10)
color_combo.bind("<<ComboboxSelected>>", change_color)

# Создание холста
canvas = tk.Canvas(root, width=200, height=200, bg='white')
canvas.pack(pady=10)

root.mainloop()
