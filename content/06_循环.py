# -*- coding:utf-8 -*-
# @Time : 2022/7/6 9:25 下午
# @Author : Bin Bin Xue
# @File : 06_循环
# @Project : ChildrenCode

# 6.1 使用for循环 for i in range(次数) - 左闭右开原则
# for i in range(0,5)
# for i in 列表名: - 遍历列表
# 嵌套循环 for i in .. :
#                       for j in ..:
# 6.2 while循环 - 用于你不知道何时停止的情况 
# while 条件: 语句快 - 条件为真时，进入语句块
# while True 是永远循环，用break跳出


def pro_1():
    for x in range(0, 20):
        print('hello,%s' % x)
        if x < 9:
            break


def pro_2():
    age = int(input('请输入您的年龄：'))
    if(age%2==0):
        for i in range(2,age+2,2):
            print(i)
    else:
        for i in range(1,age+2,2):
            print(i)


def pro_3():
    ingrediants = ['snails','leeches','gorilla belly-button lint','caterpillar eyebrows','centipede toes']
    for x in ingrediants:
        print(x)


def pro_4():
    weight=int(input('请输入您当前的体重（公斤）：'))
    for i in range(16):
        moon_weight = weight*0.165
        print('第%d年，在月球上的体重是%f' %(i,moon_weight))
        weight+=1


if __name__ == '__main__':
    # 问题1：猜猜下面的程序结果
    pro_1()
    # 问题2：偶数-创建一个循环打印偶数，直到你的年龄。如果你的年龄是奇数，则创建一个循环打印奇数，直到你的年龄
    pro_2()
    # 问题3：我最喜欢的食材-创建一个列表，包含5种不同的制作三明治的食材，建立一个循环来遍历这个列表
    pro_3()
    # 问题4：在月球上的体重-月球上的体重只是你当前的16.5%。如果在接下来的15年里，你每年长一公斤，用for循环来打印你每年在月球上的体重
    pro_4()
