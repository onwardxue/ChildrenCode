# -*- coding:utf-8 -*-
# @Time : 2022/7/4 9:50 下午
# @Author : Bin Bin Xue
# @File : paddleball
# @Project : ChildrenCode
# 该程序可直接运行（会在窗口中生成一个活蹦乱跳的弹珠） - 这个程序运行不动,不知道是电脑问题还是程序问题？

from tkinter import *
import random
import time

# 定义球类
class Ball:
    def __init__(self, canvas, color):
        # 设置画布
        self.canvas = canvas
        self.paddle = paddle
        # 设置小球尺寸坐标和颜色，并保存到对象变量中
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        # 把椭圆形移动到画布的指定位置
        self.canvas.move(self.id, 245, 100)
        # x设置小球的速度为随机速度（混排列表，取第一个）
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        # y设置小球的速度
        self.y=-3
        #
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    # 小球运动
    def draw(self):
        # 移动小球-id为小球,x为移动xian
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

class Paddle():
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos =self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x=0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self,evt):
        self.x = -2

    def turn_right(self,evt):
        self.x = 2


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

    paddle=Paddle(canvas,'blue')
    ball = Ball(canvas, 'red')

    while 1:
        if ball.hit_bottom == False:
            ball.draw()
            paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
