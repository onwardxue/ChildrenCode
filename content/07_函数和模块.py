# -*- coding:utf-8 -*-
# @Time : 2022/7/6 9:57 下午
# @Author : Bin Bin Xue
# @File : 07_函数和模块
# @Project : ChildrenCode

# 7.1 函数 - 函数名+参数+函数体
# def testfunc(myname):
#       print('hello %s') % myname
# 参数可以有多个，中间用逗号隔开
# 函数体内可以使用返回值 - return, return内也可以做一些简单计算
# 7.1.2 变量和作用域 - 变量定义在函数体内为局部变量，在函数外为全局变量
# 7.2 使用模块（如 import turtle就是引入海龟模块）
# 使用点号来使用模块中的方法（如time.asctime()）
# 介绍用sys.stdin.readline()接收输入信息
import sys

def moon_weight(init, add):
    weight = init
    moon_weight = 0
    for i in range(15):
        moon_weight = weight * 0.165
        weight += add
    return moon_weight


def moon_weight_2(init, add, year):
    weight = init
    moon_weight = 0
    for i in range(year):
        moon_weight = weight * 0.165
        weight += add
    return moon_weight


def moon_weight_3():
    print('Please enter your current Earth weight：')
    init = int(sys.stdin.readline())
    print('Please enter the amount your weight might increase each year：')
    add = int(sys.stdin.readline())
    print('Please enter the number of years：')
    year = int(sys.stdin.readline())

    weight = init
    moon_weight = 0
    for i in range(year):
        moon_weight = weight * 0.165
        weight += add
    return moon_weight

if __name__ == '__main__':
    # 问题1：建立一个for循环计算15年后你在月球上的体重。设为一个函数，参数为你的起始体重、每年增加的体重。
    print(moon_weight(30, 0.25))

    # 问题2：将前一个问题改成三个参数，即n年后
    print(moon_weight_2(90, 0.25, 5))

    # 问题3：使用sys.stdin.readline()提示输入这三个值
    print(moon_weight_3())
