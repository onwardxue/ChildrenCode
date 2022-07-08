# -*- coding:utf-8 -*-
# @Time : 2022/7/7 9:39 下午
# @Author : Bin Bin Xue
# @File : 10_常用的Python模块
# @Project : ChildrenCode

# 介绍turtle的高级用法
import turtle


class turtleTest():

    def star(self):
        t = turtle.Pen()
        t.reset()
        for x in range(1, 9):
            t.forward(100)
            t.left(225)

    def spiral(self):
        t = turtle.Pen()
        t.reset()
        for x in range(1, 38):
            t.forward(100)
            t.left(175)

    def star_2(self):
        t = turtle.Pen()
        t.reset()
        for x in range(1, 19):
            t.forward(100)
            if x % 2 == 0:
                t.left(175)
            else:
                t.left(225)

    def car(self):
        t = turtle.Pen()
        t.reset()
        t.color(1, 0, 0)
        t.begin_fill()
        t.forward(100)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.forward(60)
        t.left(90)
        t.forward(20)
        t.right(90)
        t.forward(20)
        t.left(90)
        t.forward(20)
        t.end_fill()

        t.color(0, 0, 0)
        t.up()
        t.forward(10)
        t.down()
        t.begin_fill()
        t.circle(10)
        t.end_fill()

        t.setheading(0)
        t.up()
        t.forward(90)
        t.right(90)
        t.forward(10)
        t.setheading(0)
        t.begin_fill()
        t.down()
        t.circle(10)
        t.end_fill()

    def circle(self):
        t = turtle.Pen()
        t.reset()
        t.color(1, 1, 0)
        t.begin_fill()
        t.circle(50)
        t.end_fill()

    # 画圆形
    def micircle(self, red, green, blue):
        t = turtle.Pen()
        t.color(red, green, blue)
        t.begin_fill()
        t.circle(50)
        t.end_fill()

    def mysquare(self, size):
        t = turtle.Pen()
        for x in range(1, 5):
            t.forward(size)
            t.left(90)

    def mysquare_2(self, size, filled):
        t = turtle.Pen()
        if (filled == True):
            t.begin_fill()
        for x in range(1, 5):
            t.forward(size)
            t.left(90)
        if (filled == True):
            t.end_fill()

    def octangle(self, filled):
        t = turtle.Pen()
        t.color(1, 0, 0)
        if (filled == True):
            t.begin_fill()
        for i in range(8):
            t.right(45)
            t.forward(90)
        if (filled == True):
            t.end_fill()

    def draw_star(self, size, points):
        t = turtle.Pen()
        for x in range(points):
            t.forward(size)
            if x % 2 == 0:
                t.left(175)
            else:
                t.left(225)


if __name__ == '__main__':
    tle = turtleTest()
    # 画星星、螺旋、锐角星、车、圆形
    # tle.star()
    # tle.sprial()
    # tle.star_2()
    # tle.car()
    # t.color() - 红绿蓝（黄=红+绿）
    # tle.circle()
    # 用不同颜色画填充圆形
    # tle.micircle(0,1,0)
    # tle.micircle(0,0.5,0)
    # tle.micircle(1,0,0)
    # tle.micircle(0.5,0,0)
    # tle.micircle(0,0,1)
    # tle.micircle(0,0,0.5)
    # 画不同尺寸的方形
    # tle.mysquare(25)
    # tle.mysquare(50)
    # tle.mysquare(75)
    # tle.mysquare(100)
    # tle.mysquare(125)
    # 画不同尺寸、填或不填充的方形
    # tle.mysquare_2(50,True)
    # tle.mysquare_2(100,False)
    # 测验1 画八角形
    # tle.octangle(True)
    # 测验2 画不同的尖叫星星
    # tle.draw_star(50, 20)
