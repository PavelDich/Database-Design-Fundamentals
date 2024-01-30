from tkinter import *

def move_to_event(event):
    global target_x, target_y
    target_x, target_y = event.x, event.y
    move_smoothly()

def move_smoothly():
    ball_coords = c.coords(ball)
    ball_x = (ball_coords[0] + ball_coords[2]) / 2
    ball_y = (ball_coords[1] + ball_coords[3]) / 2
    dx = (target_x - ball_x) / 10
    dy = (target_y - ball_y) / 10
    if abs(dx) < 1 and abs(dy) < 1:  # Если шар достаточно близко к цели, остановить движение
        return
    c.move(ball, dx, dy)
    root.after(50, move_smoothly)  # Повторить движение через 50 миллисекунд

root = Tk()
c = Canvas(root, width=300, height=200, bg="white")
c.pack()
ball = c.create_oval(0, 100, 40, 140, fill='green')
c.bind("<Button-1>", move_to_event)
target_x, target_y = 0, 0
root.mainloop()