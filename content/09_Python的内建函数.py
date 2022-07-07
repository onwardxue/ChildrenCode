# -*- coding:utf-8 -*-
# @Time : 2022/7/7 8:47 下午
# @Author : Bin Bin Xue
# @File : 09_Python的内建函数
# @Project : ChildrenCode

# 介绍python常用的12个内建函数

# 9.1.1 abs(变量) - 绝对值
# 9.1.2 bool(变量) - bool函数，0返回False，1返回True（input()接受输入信息，.rstrip()把字符串结尾的空白和回车删除
# 9.1.3 dir(变量) - 可以返回变量所带有的所有方法
#          help(变量.方法) - 显示函数的简短描述
# 9.1.4 eval('10*15') - 把一个字符串作为参数并返回它作为一个函数表达式的结果（本次结果为150），常用于接收用户的输入信息
#           eval(input('请输入计算的表达式，如12*15'))
# 9.1.5 exec(变量) - 运行从文件中读入的小程序，如：
#           program = '''print('a') print('b')'''
#          exec(program)   - 得到结果（a，b）
# 9.1.6 float(变量) - 将字符串或数字转成浮点型
# 9.1.7 int(变量) - 字符串或数字转成整型
# 9.1.8 len(字符串) - 返回字符串中的字符个数
# 9.1.9 max()min() - 返回列表、字符串、元组中最大的元素或最小的元素
# 9.1.10 range(开始，结束，步长)
# 9.1.11 sum(列表) - 求列表元素之和
# 9.2 文件操作
# 9.2.1 打开文件 - 文件变量 = open('路径')
# 9.2.2  写入文件 - file = open('路径','w')
#                             file.write('写入内容')
#                             file.close()

if __name__ == '__main__':
    # 问题1：猜测下面程序的结果
    a = abs(10) + abs(-10)
    print(a)
    b = abs(-10) + -10
    print(b)
    # 问题2：字符串拆成单词
    str1 = 'this if is you not are a reading very this good then way you to have hide done a it message wrong'
    print(dir(str1))
    print(help(str1.split()))
    str2 = str1.split(' ')
    for x in str2:
        print(x)
