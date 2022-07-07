# -*- coding:utf-8 -*-
# @Time : 2022/7/6 8:18 下午
# @Author : Bin Bin Xue
# @File : 04_turtleplot
# @Project : ChildrenCode

# 5.1 if语句 - if 条件: 语句块
# 5.2 注意缩进
# 5.3 条件符号：等于、不等于、大于等于..
# 5.4 if else
# 5.5 if elif else
# 5.6 组合条件：and 且、or 或
# 5.7 空值 None
# 数值型和字符串-10和'10'不相等，要用强制转换int()或str()，浮点型用float()


def pro1():
    twinkies = int(input('请输入蛋糕的数量：'))
    if 100 > twinkies or twinkies> 500:
        print('不是太多就是太少')


def pro2():
    money = int(input('请输入您口袋中的钱：'))
    if 100 < money < 500:
        print('您的钱在100到500之间')
    elif 1000 < money < 5000:
        print('您的钱在1000到5000之间')


def pro3():
    ninjas=int(input('请输入敌方忍者的数量：'))
    if 30<=ninjas<50:
        print('太多了')
    elif 10<=ninjas<30:
        print('有点难，不过我能应付！')
    elif ninjas<10:
        print('我打得过那些忍着')


if __name__ == '__main__':
    # 问题1 小蛋糕：用if语句检查小蛋糕的数量，如果是少于100活着大于500，就输出"不是太少就是太多"
    pro1()
    # 问题2 数字刚刚好：创建一个if语句检查money中包含的钱，是不是在100到500之间，还是在1000到5000之间
    pro2()
    # 问题3 我打得过那些忍着：在变量ninjas所包含的数字小于50时，输出"太多了"；小于30时，输出"有点难，不过我能应付"；小于10时，输出"我能打得过"
    pro3()
