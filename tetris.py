# -*- coding:utf-8 -*-

import tkinter as tk
import random

size = 50   # サイズ
moveX = 4   # 開始位置(X座標)
moveY = 1   # 開始位置(Y座標)

# ブロック作成
tetroI = [0,0, 0,-1, 0,1, 0,2]
tetrol = [-1,1, 0,-1, 0,0, 0,1]
tetroL = [0,0, 0,-1, 1,1, 0,1]
tetroO = [0,0, 1,0, 0,-1, 1,-1,]
tetroS = [-1,0, 0,-1, 1,-1, 0,0]
tetroT = [-1,0, 0,0, 1,0, 0,1]
tetroZ = [-1,-1, 0,-1, 1,0, 0,0]
tetro  = [tetroI, tetrol, tetroL, tetroO, tetroS, tetroT, tetroZ]

def draw_tetris():
    i = 0
    while i < 4:
        x = (tetro[6] [ i * 2 ] + moveX) * size
        y = (tetro[6] [ i * 2 + 1 ] + moveY) * size
        can.create_rectangle( x, y, x+size, y+size, fill="red")
        i += 1



app = tk.Tk()
can = tk.Canvas(app, width= size*10, height = size*20 )
can.pack()
#---処理---

# 再帰的処理
def game_loop():
    can.delete("all")
    draw_tetris()
    can.after(50, game_loop)

game_loop()



#----END---
app.mainloop()