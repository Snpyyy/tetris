# -*- coding:utf-8 -*-

import tkinter as tk
import random

# 定義
size = 30   # サイズ
moveX = 5   # 開始位置(X座標)
moveY = 1   # 開始位置(Y座標)

# フィールド作成（当たり判定）
defence_field = [
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,7,7,7,7,7,7,7,7,7,7,8],
    [8,8,8,8,8,8,8,8,8,8,8,8]
]

# ブロック作成
tetroI = [0,0, 0,-1, 0,1, 0,2]
tetroJ = [-1,1, 0,-1, 0,0, 0,1]
tetroL = [0,0, 0,-1, 1,1, 0,1]
tetroO = [0,0, 1,0, 0,-1, 1,-1,]
tetroS = [-1,0, 0,-1, 1,-1, 0,0]
tetroT = [-1,0, 0,0, 1,0, 0,1]
tetroZ = [-1,-1, 0,-1, 1,0, 0,0]
tetro  = [tetroI, tetroJ, tetroL, tetroO, tetroS, tetroT, tetroZ]
color = ["red", "yellow", "lime", "green", "blue", "navy", "fuchsia", "gray", "black"]
type = random.randint(0,6)

# テトリスブロック描写
def draw_tetris():
    i = 0
    while i < 4:
        x = (tetro[type] [ i * 2 ] + moveX) * size
        y = (tetro[type] [ i * 2 + 1 ] + moveY) * size
        can.create_rectangle( x, y, x+size, y+size, fill=color[type])
        i += 1

# マス目作成
def game_field():
    i = 0
    j = 0
    while i < 22:
        field_y = i * size
        while j < 12:
            field_x = j * size 
            can.create_rectangle( 
                        field_x, field_y,   #始点
                        field_x + size, field_y + size, #終点
                        width=1, outline="#ACACAC")   #オプション
            if defence_field[i][j] == 8:
                can.create_rectangle( 
                        field_x, field_y,   #始点
                        field_x + size, field_y + size, #終点
                        fill="black")   #オプション
            j += 1
        i += 1
        j = 0

# キー操作
def keypress(event):
    global moveX, moveY
    judge_x = moveX
    judge_y = moveY
    rotation = []
    rotation.extend(tetro[type])
    if event.keysym == "Left":
        judge_x -= 1
    elif event.keysym == "Right":
        judge_x += 1
    elif event.keysym == "Up":
        judge_y -= 1
    elif event.keysym == "Down":
        judge_y += 1
    elif event.keysym == "space":
        rotation.clear()
        i = 0
        while i < 4:
            rotation.append(tetro[type][i*2+1]*(-1))
            rotation.append(tetro[type][i*2])
            i += 1
    judge(judge_x, judge_y, rotation)

# 当たり判定の確認
def judge(x, y, rotation):
    global moveX, moveY
    result = True
    i = 0
    while i < 4:
        j = rotation [i * 2] + x
        k = rotation [i * 2 + 1] + y
        if defence_field[ k ] [ j ] != 7:
            result = False
        i += 1
    if result == True:
            moveX = x
            moveY = y
            tetro[type].clear()
            tetro[type].extend(rotation)
        

# 再帰的処理
def game_loop():
    can.delete("all")
    game_field()
    draw_tetris()
    can.after(50, game_loop)

#-----------------------------------

app = tk.Tk()
can = tk.Canvas(app, width= size*12, height = size*21, bg="#E5E5E5" )
can.pack()
#---処理---

app.bind("<KeyPress>", keypress)

game_loop()


#----END---
app.mainloop()