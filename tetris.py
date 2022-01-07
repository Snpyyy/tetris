# -*- coding:utf-8 -*-

import tkinter as tk
import random

# 定義
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
type = random.randint(0,6)

# テトリスブロック描写
def draw_tetris():
    i = 0
    while i < 4:
        x = (tetro[type] [ i * 2 ] + moveX) * size
        y = (tetro[type] [ i * 2 + 1 ] + moveY) * size
        can.create_rectangle( x, y, x+size, y+size, fill="red")
        i += 1

# 再帰的処理
def game_loop():
    can.delete("all")
    game_field()
    draw_tetris()
    can.after(50, game_loop)

# マス目作成
def game_field():
    i = 0
    j = 0
    while i < 20:
        field_y = i * size
        while j < 10:
            field_x = j * size 
            can.create_rectangle( 
                        field_x, field_y,   #始点
                        field_x + size, field_y + size, #終点
                        width=1, outline= "#ACACAC",)   #オプション
            j += 1
        i += 1
        j = 0

#-----------------------------------

app = tk.Tk()
can = tk.Canvas(app, width= size*10, height = size*20, bg="#E5E5E5" )
can.pack()
#---処理---


game_loop()


#----END---
app.mainloop()