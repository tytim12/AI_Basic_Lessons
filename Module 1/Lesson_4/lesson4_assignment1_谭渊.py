# encoding:utf-8

# 打乱数据集，方法1
import random

x = ['快递太慢了！','不好吃','特别难吃','要齁死我了','很划算','下次还来','味道很不错！','香']
y = ['差评','差评','差评','差评','好评','好评','好评','好评']

def shuffle1(x,y):

    for i in range(len(x)):
        # 遍历列表 -> 每次random一个index出来和第i位的元素交换位置
        rand_index = random.randint(0, len(x)-1)
        
        # 交换位置
        x[i], x[rand_index] = x[rand_index], x[i]
        y[i], y[rand_index] = y[rand_index], y[i]

    return x,y


# 方法2: 
# 1. 用sample函数，不重样抽取样本打乱list
# 2. 打乱后的结果赋值给a,b, 再替换x,y
def shuffle2(x,y):

    a = []
    b = []
    index = [i for i in range(0, len(x))]  # 初始化一个长度与xy相同的列表
    rand_index = random.sample(index, len(x)) # 用sample()随机不放回抽取样本

    # 创建打乱后的列表并赋值给xy
    for i in rand_index: 
        a.append(x[i])
        b.append(y[i])
    x, y = a, b

    return x,y


# print result for certify
if __name__ == '__main__':
    x, y = shuffle1(x, y)
    for i, j in zip(x, y):
        print(i, ':', j)