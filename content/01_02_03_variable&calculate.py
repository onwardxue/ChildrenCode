# -*- coding:utf-8 -*-
# @Time : 2022/7/4 9:15 下午
# @Author : Bin Bin Xue
# @File : __init__.py
# @Project : ChildrenCode

# 2.1python运算符：+、-、*、/ 、（）（括号>乘除>加减）
# 2.2 变量：减少重复、只改变一次即可对其他都有影响
# 3.1 字符串-单引号或双引号，多行用三引号
# 3.1.1 转义符号'\'
# 3.1.2 占位符替换成变量 '%s' % (变量,)
# 3.1.3 字符串乘法 - 复制作用
# 3.2 列表-中括号'[' ',' ']'
# 3.2.1 列表索引：从0开始
# 3.2.2 列表值取用：列表名[2:5]（含左不含右）
# 3.2.3 列表中可以存放数值、字符串、列表
# 3.2.4 列表添加元素：列表名.append(' ')，删除指定位置的元素：del 列表名[pos]
# 3.2.5 列表算术：列表相加-合并列表；列表相乘-复制列表
# 3.3 元组-圆括号()，特点是无法更改
# 3.4  字典-大括号加冒号{' ':' ',..}，冒号前是key，后是value


if __name__ == '__main__':
    # 问题一：最爱-列出爱好到列表，变量名为games；列出食物喜好到列表，变量名为foods，合并起来结果为favorites
    games = ['basketball', 'League of Legends', 'reading', 'coding', 'videos']
    foods = ['pork', 'noodles', 'rice', 'potato', 'hamburger']
    favorites = games + foods
    print(favorites)

    # 问题二：战士计数-有三座建筑，每座的房顶有25个忍着，还有2个地道，每个地道里藏有40个武士，问一共有多少人准备投入战斗？
    amount = 3 * 25 + 2 * 40
    print(amount)

    # 问题三：打招呼-创建两个变量，一个指向你的姓，一个指向你的名。创建一个字符串，用占位符使用这两个变量来打印带有你名字的信息，如"你好，郑伊健！"
    surname = '彭'
    name = '于晏'
    print('你好，%s%s!' % (surname, name))
