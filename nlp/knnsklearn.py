# -*- coding:utf-8 -*-
"""
@author:Fan Yanyan
@file:knnsklearn.py
@time:2018/11/22 18:21
"""
from sklearn import neighbors
import knn as KNN

def knn_sklearn_predict():
    # 调用机器学习库knn分类器算法
    knn = neighbors.KNeighborsClassifier()
    # 调用模块下的方法，返回数据特征集和类标签
    datasets,labels = KNN.create_dateset()
    # 传入参数，特征数据，分类标签
    knn.fit(datasets,labels)
     # knn预测
    predictRes = knn.predict([[2,4,0]])
    print(predictRes)
    print('该访客认为成都的天气是:\t','非常热' if predictRes[0] ==0 else '一般热')
    return predictRes




if __name__ == '__main__':
    knn_sklearn_predict()