# -*- coding:utf-8 -*-
# @Time : 2022/7/6 11:00 下午
# @Author : Bin Bin Xue
# @File : 08_类和对象
# @Project : ChildrenCode

import turtle
# 8.1 事物拆分成类 - 包括一个事物的属性和行为，可以重复使用（如一类人）
# 定义类 - Class Things:
#                   pass
# 8.1.1 父母与孩子
# 给为一个类指定父类：在括号中加父类名
# class Animate(Things):
#       pass
# 8.1.2 生成类的对象 - reginald = Giraffes()
#   生成对象才能产生实际的行为方法（每个对象都是新的、独立的存在）
# 8.1.3 定义类中的函数 - class ThisIsMySilly()
#                                           def this_is_a_class_function():
# 8.1.4 用函数表示类的特征 - 如动物会呼吸、行走、吃食物
# class Animals(Animate):
#       def breathe(self):
#               pass
#       def  move(self):
#               pass
#       def eat_food(self):
#               pass
# 子类会继承父类的方法（函数）
# 8.2 对象和类的一些实用功能
# 8.2.1 函数继承 - 任何在父类中定义的函数都可以在子类中使用
# 8.2.2 从函数里调用其他函数  - 在函数定义的位置加其他的函数
#   class Giraffes(Mammals):
#           def dance(self):
#                   self.move()
#                   self.move()
# 8.3 初始化对象 - __init__(self,属性_1):
#          self.giraffe_sports = 属性_1
# 主要初始化的是属性值
# 创建类时就可以指定参数 - ozwald = Giraffes(100)

class Giraffes():
    def left_Foot_Forward(self):
        print('left foot forward')
    def forward_Foot_Forward(self):
        print('forward foot forward')
    def right_Foot_Forward(self):
        print('right foot forward')
    def backward_Foot_Forward(self):
        print('backforward foot forward')

    def dance(self):
        self.left_Foot_Forward()
        self.left_Foot_Forward()
        self.right_Foot_Forward()
        self.right_Foot_Forward()
        self.left_Foot_Forward()
        self.right_Foot_Forward()
        self.right_Foot_Forward()
        self.left_Foot_Forward()


if __name__ == '__main__':
    # 测验1.给长劲鹿添加函数让其前、后、左、右四只脚移动。然后写一个dance函数来教长劲鹿跳舞（跳舞函数中调用前面四个函数）
    Reginald = Giraffes()
    Reginald.dance()
    # 测验2.使用四只pen对象的海龟来创建图中侧向一边的叉子
    t1 = turtle.Pen()
    t2 = turtle.Pen()
    t3 = turtle.Pen()
    t4 = turtle.Pen()
    t1.forward(80)
    t1.left(90)
    t1.forward(10)
    t1.right(90)
    t1.forward(10)
    t2.forward(80)
    t2.right(90)
    t2.forward(10)
    t2.left(90)
    t2.forward(10)
    t3.forward(70)
    t3.left(90)
    t3.forward(30)
    t3.right(90)
    t3.forward(30)
    t4.forward(70)
    t4.right(90)
    t4.forward(30)
    t4.left(90)
    t4.forward(30)

