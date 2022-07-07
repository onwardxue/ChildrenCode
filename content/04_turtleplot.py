# -*- coding:utf-8 -*-
# @Time : 2022/7/6 8:18 下午
# @Author : Bin Bin Xue
# @File : 04_turtleplot
# @Project : ChildrenCode

import turtle


# 4.1 使用turtle绘图
# 4.1.1 创建画布 t=turtle.Pen()
# 4.1.2 移动海龟 - 像人的行走一样
# 前进50米-t.forward(50)
# 箭头左转90度-t.left(90)
# 停笔-t.up()
# 继续画-t.down()
# 重置-t.reset()
# 清除绘制但不重置-t.clear()

def work1():
    t1 = turtle.Pen()
    for i in range(4):
        t1.forward(200)
        t1.left(90)


def parallel():
    t = turtle.Pen()
    t.reset()
    t.backward(100)
    t.up()
    t.right(90)
    t.forward(20)
    t.left(90)
    t.down()
    t.forward(100)


def work2():
    t2 = turtle.Pen()
    for i in range(3):
        t2.forward(200)
        t2.left(120)


def work3():
    t3 = turtle.Pen()
    for i in range(4):
        t3.forward(180)
        t3.up()
        t3.forward(10)
        t3.left(90)
        t3.forward(10)
        t3.down()


if __name__ == '__main__':
    # 绘制平行线
    # parallel()
    # 作业1：绘制长方形
    # work1()
    # 作业2：三角形
    # work2()
    # 作业3：画没有角的正方形
    work3()