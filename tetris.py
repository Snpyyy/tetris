# -*- coding:utf-8 -*-

import tkinter as tk

Size = 50

app = tk.Tk()
can = tk.Canvas(app, width= 10*Size, height=20*Size )
can.pack()

# 再帰的処理
def game_loop():
    can.delete("all")
    draw_tetris()

app.mainloop()