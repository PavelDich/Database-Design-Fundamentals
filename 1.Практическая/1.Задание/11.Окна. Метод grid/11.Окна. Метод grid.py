import tkinter as tk
from tkinter import messagebox


def draw_figure(canvas, x1, y1, x2, y2, figure_type):
    if figure_type == "Прямоугольник":
        canvas.create_rectangle(x1, y1, x2, y2, fill='gray', outline="black")
    else:
        canvas.create_oval(x1, y1, x2, y2, fill='gray', outline="black")


def open_window(canvas):
    def add_figure():
        x1 = int(x1_entry.get())
        y1 = int(y1_entry.get())
        x2 = int(x2_entry.get())
        y2 = int(y2_entry.get())
        figure_type = figure_type_var.get()
        draw_figure(canvas, x1, y1, x2, y2, figure_type)
        top.destroy()

    top = tk.Toplevel()
    top.title("Добавить фигуру")

    figures = tk.Frame(top)
    figures.pack(side=tk.TOP)
    figure1 = tk.Frame(figures)
    figure1.pack(side=tk.LEFT)
    figure2 = tk.Frame(figures)
    figure2.pack(side=tk.RIGHT)

    figure1L = tk.Frame(figure1)
    figure1L.pack(side=tk.LEFT)
    figure1E = tk.Frame(figure1)
    figure1E.pack(side=tk.RIGHT)

    x1_label = tk.Label(figure1L, text="x1:")
    x1_label.pack()
    x1_entry = tk.Entry(figure1E)
    x1_entry.pack()

    y1_label = tk.Label(figure1L, text="y1:")
    y1_label.pack()
    y1_entry = tk.Entry(figure1E)
    y1_entry.pack()

    figure2L = tk.Frame(figure2)
    figure2L.pack(side=tk.LEFT)
    figure2E = tk.Frame(figure2)
    figure2E.pack(side=tk.RIGHT)

    x2_label = tk.Label(figure2L, text="x2:")
    x2_label.pack()
    x2_entry = tk.Entry(figure2E)
    x2_entry.pack()

    y2_label = tk.Label(figure2L, text="y2:")
    y2_label.pack()
    y2_entry = tk.Entry(figure2E)
    y2_entry.pack()

    figure_type_var = tk.StringVar()
    figure_type_var.set("Прямоугольник")
    rectangle_radio = tk.Radiobutton(top, text="Прямоугольник", variable=figure_type_var, value="Прямоугольник")
    rectangle_radio.pack()
    oval_radio = tk.Radiobutton(top, text="Овал", variable=figure_type_var, value="Овал")
    oval_radio.pack()

    draw_button = tk.Button(top, text="Нарисовать", command=add_figure)
    draw_button.pack()


root = tk.Tk()
root.title("Холст")
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
add_button = tk.Button(root, text="Добавить фигуру", command=lambda: open_window(canvas))
add_button.pack()
root.mainloop()
