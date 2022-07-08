# -*- coding:utf-8 -*-
# @Time : 2022/7/7 9:39 下午
# @Author : Bin Bin Xue
# @File : 10_常用的Python模块
# @Project : ChildrenCode

# 使用tkinter库高级绘图，比海龟更快
# 使用import * 的方式导入就可以用方法，不需要用库.方法了
from tkinter import *

tk = Tk()


def hello():
    print('hello there')

def movetriangle(event):
    canvas.move(1,5,0)


if __name__ == '__main__':
    # 创建一个按钮
    btn = Button(tk, text='click me', command=hello)
    btn.pack()
    # 创建一个画布
    canvas = Canvas(tk,width=500,height=500)
    canvas.pack()
    canvas.create_line(0,0,500,500)
    # 对象运动
    canvas.pack()
    canvas.create_polygon(10,10,10,60,50,35)
    canvas.bind_all('<KeyPress-Return>',movetriangle)
    