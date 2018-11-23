# -*- coding:utf-8 -*-
"""
@author:Fan Yanyan
@file:knn.py
@time:2018/11/22 14:13
"""
import numpy as np
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
import math

from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号，显示为方块的问题。


# 创建数据源，返回数据集和类标签
def creat_datasets():
    datasets = array([[8, 4, 2], [7, 1, 1], [1, 4, 4], [3, 0, 5], [9, 4, 2], [7, 2, 1], [1, 5, 4], [3, 1, 5]])  # 数据集
    labels = [0, 0, 1, 1, 0, 0, 1, 1]  # 类标签 0代表非常热，1代表一般热
    return datasets, labels


# 可视化分析数据
def analyze_data_plot(x, y):
    fig = plt.figure()
    # 将画布划分1行1列1块
    ax = fig.add_subplot(111)
    ax.scatter(x, y)
    # 设置散点图标题和横纵坐标
    plt.title("游客冷热感知点散点图")
    plt.xlabel("天热吃冰激凌数目")
    plt.ylabel("天热喝水数目")

    plt.show()


# 构造KNN分类器
def knn_Classfier(newV, datasets, labels, k):

    # 1.计算样本数据与样本库数据之间的距离
    SqrtDist = EuclideanDistance3(newV, datasets)
    # 2.根据距离进行排序
    sortdDistindexs = SqrtDist.argsort(axis=0)
    # 3.针对k个点，统计各个类别的数量
    classCount = {}  # 统计各个类别分别的数量
    for i in range(k):
        votelabel = labels[sortdDistindexs[i]]
        # 统计标签的键值对
        classCount[votelabel] = classCount.get(votelabel, 0) + 1

    # 4.投票机制,少数服从多数原则,输入类别
    # 对各个分类字典进行排序，降序，itemtgetter按照value排序
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


# 欧式距离计算：d=(x1-x2)2 + (y1-y2)2
def ComputeEuclideanDistance(x1, y1, x2, y2):
    d = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2))
    return d


# 欧式距离计算2
def EuclideanDistance(instance1, instance2, length):
    d = 0
    for x in range(length):
        d += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(d)


# 欧式距离计算3
def EuclideanDistance3(newV, datasets):
    # 获取数据向量的行向量维度和列向量维度
    rowsize, colsize = datasets.shape

    # 各特征向量间做差值
    diffMat = tile(newV, (rowsize, 1)) - datasets

    # 对差值平方
    sqDiffMat = diffMat ** 2

    # 差值平方和进行开方
    sqDist = sqDiffMat.sum(axis=1) ** 0.5
    return sqDist


if __name__ == '__main__':
    # 创建数据集和类标签
    datasets, labels = creat_datasets()

    # 可视化分析数据
    # print(type(datasets[:, 0]))
    # analyze_data_plot(datasets[:, 0], datasets[:, 1])

    # 欧拉距离计算1
    # d1 = ComputeEuclideanDistance(2, 4, 8, 2)
    # print('欧拉距离计算1:', d1)

    # 欧拉距离计算2
    # d2 = EuclideanDistance([2, 4, 4], [7, 1, 1], 3)
    # print('欧拉距离计算2', d2)

    # 欧拉距离计算3
    # d3 = EuclideanDistance3([2, 4, 4], datasets)
    # print('欧拉距离计算3', d3)

    # 单实例构造KNN分类器
    # newV = [2, 4, 0]
    # res = knn_Classfier([2, 4, 4], datasets, labels, 3)

    # 多实例构造KNN分类器
    vecs = array([[2, 4, 4], [3, 0, 0], [5, 7, 2]])
    for vec in vecs:
        res = knn_Classfier(vec, datasets, labels, 3)
        print(str(vec) + ' KNN投票预测结果是：', '非常热' if res == 0 else '一般热')
