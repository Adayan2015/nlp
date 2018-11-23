# -*- coding:utf-8 -*-
"""
@author:Fan Yanyan
@file:knnsklearn.py
@time:2018/11/22 18:21
"""
from sklearn import neighbors
from numpy import *
import knn as KNN


def knn_sklearn_predict(newV, datasets, labels):
    # 调用机器学习库knn分类器算法
    knn = neighbors.KNeighborsClassifier()
    # 传入参数，特征数据，分类标签
    knn.fit(datasets, labels)
    # knn预测
    predictRes = knn.predict([newV])

    print('该访客认为成都的天气是:\t', '非常热' if predictRes[0] == 0 else '一般热')
    return predictRes


# 利用KNN分类器预测随机访客天气感知度
def Predict_temperature():
    # 创建数据集和类标签
    datasets, labels = KNN.creat_datasets()
    # 采访新游客
    iceCream = float(input('Q:请问你今天吃了几个冰激凌？\n'))
    drinkWater = float(input('Q:请问你今天喝了几瓶水？\n'))
    palyAct = float(input('Q:请问你今天户外活动几个小时？\n'))

    newV = [iceCream, drinkWater, palyAct]
    knn_sklearn_predict(newV, datasets, labels)



if __name__ == '__main__':
    Predict_temperature()
