import tkinter as tk


def draw_scene():
    canvas.delete("all")

    canvas.create_oval(500, 50, 550, 100, fill='yellow')

    canvas.create_rectangle(200, 250, 400, 450, fill='lightblue', outline='lightblue' )
    canvas.create_polygon(150, 250, 450, 250, 300, 125, fill='lightblue')


    for i in range(0, 600, 20):
        i += 100
        canvas.create_arc(i, 450, i, 600,
                     start=0, extent=45,
                     fill='green', outline='green' )


root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=500)
canvas.pack()

draw_scene()

root.mainloop()
