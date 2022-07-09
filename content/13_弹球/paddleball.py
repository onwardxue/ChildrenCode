# -*- coding:utf-8 -*-
# @Time : 2022/7/4 9:50 下午
# @Author : Bin Bin Xue
# @File : paddleball
# @Project : ChildrenCode
# 该程序可直接运行（会在窗口中生成一个活蹦乱跳的弹珠）

from tkinter import *
import random
import time

#
class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y =3
        if pos[3] >= self.canvas_height:
            self.y=-3
        if pos[0] <= 0:
            self.x=3
        if pos[2] >= self.canvas_width:
            self.x=-3


if __name__ == '__main__':
    # 创建游戏的画布
    tk = Tk()
    tk.title('Game')
    # 固定窗口尺寸
    tk.resizable(0, 0)
    # 把当前窗口放在所有窗口之前
    tk.wm_attributes('-topmost', 1)
    # 设置窗口尺寸
    canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
    #  让画布尺寸按前一行给出的宽度和高度的参数调整其自身大小
    canvas.pack()
    # 让游戏动画做好初始化
    tk.update()

    ball = Ball(canvas, 'red')

    while 1:
        ball.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
