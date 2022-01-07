# -*- coding:utf-8 -*-

import tkinter
from tetris_field import field

root = tkinter.Tk()
#---

# 1マスのサイズ（正方形）
size = field(50)

# 画面作成
root.title("テトリス！")
root.geometry( str(size.window_width) + "x" + str(size.window_height) ) 
root.config(bg="#ffffff")

# キャンバス作成
canvas = tkinter.Canvas(
    root,
    width= size.canvas_width,
    height= size.canvas_height,
    bg= "gray"
)
canvas.place(
    x = size.one_block * 2 ,
    y = 0,
)

# キャンバスのマス目作成 
i = 1
j = 1
while i < 10:
    canvas.create_rectangle(
        size.one_block * i , 0, # 長方形のキャンバス上の始点座標
        size.one_block * i, size.canvas_height, # 長方形のキャンバス上の終点座標
        width = 0.1, # 枠線の太さ
        outline = "white" # 塗り潰しの色
    )
    i += 1
    while j < 20:
        canvas.create_rectangle(
            0, size.one_block * j, # 長方形のキャンバス上の始点座標
            size.canvas_width, size.one_block * j, # 長方形のキャンバス上の終点座標
            width = 0.1, # 枠線の太さ
            outline = "white" # 塗り潰しの色
        )
        j += 1


#---
root.mainloop()







#--------------------------------------------------------------
#tetris_field.py
# class field:
#     def __init__(self, size):
#         self.window_width = size * 14
#         self.window_height = size * 20
#         self.canvas_width = size * 10
#         self.canvas_height = size * 20
#         self.one_block = size