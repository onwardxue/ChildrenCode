# -*- coding:utf-8 -*-
# @Time : 2022/7/7 9:39 下午
# @Author : Bin Bin Xue
# @File : 10_常用的Python模块
# @Project : ChildrenCode

# 介绍6个常用的python模块

# 10.1 - copy模块 - copy.copy(对象/对象列表)，复制对象或对象列表（还是原来的对象，改变原来的会对复制的有影响）
#                          - copy.deepcopy()，复制对象或对象列表（新建的对象，与原来的之间互相没有影响）
# 10.2 - keyword模块 - 记录了所有的关键字
#           keyword.iskeyword('检查词')    判断是否为关键字
#           keyword.kwlist  列出所有关键字
# 10.3 - random模块 - 获得随机数
#          random.randint(始，终)  - 在数字范围内随机挑选一个数字
#          random.choice(列表) - 从列表中随机选择一个元素
#          random.shuffle(列表) - 将列表元素的顺序打乱
# 10.4 -sys模块 - 使用shell程序
#          sys.exit() - 退出程序或控制台
#          sys.stdin.readline(字符数) - 标准读取输入信息（可指定读取的字符数）
#          sys.stdout.write('字符串') - 标准输出信息（结尾会给出字符个数）
#          sys.version - 输出Python版本信息
# 10.5 - time模块 - 获取时间
#          time.time() - 自1970年000开始的累计秒数（常用于计算程序运行的秒数）
#          time.asctime() - 以可读的方式返回日期和时间（中间可以加元组进行转换）
#          time.localtime() - 以列表结构返回当前时间，列表第一个元素为年，依此类推
#          time.sleep(n) - 程序停止n秒
# 10.6 - pickle模块 - 保存信息
#          pickle.dump(要保存的信息（任意类型），.dat文件变量) - 保存信息（二进制形式，任意类型），又叫序列化（会自动创建.dat文件）
#          pickle.load(保存的文件变量) - 读取信息（用pickle保存的文件），又叫反序列化
#          保存的文件要用'wb'格式，读取的文件要用'rb'格式（二进制）

import pickle

if __name__ == '__main__':
    # 序列化你的最爱
    favorite = ['beautiful girl', 'coding','eating','juice','hamburger',]
    save_file = open('save.dat','wb')
    pickle.dump(favorite, save_file)
    save_file.close()

    load_file = open('save.dat','rb')
    loaded_favorite = pickle.load(load_file)
    print(loaded_favorite)
    load_file.close()