# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 13:02:19 2017

@author: Administrator
"""
import numpy as np
import pandas as pd

def produce_data(n_points=1000):
    # 创建储存数据的DataFrame
    data = pd.DataFrame()
    
    # 生成虚拟研究数据
    np.random.seed(0)
    # 生成学习特征
    data['practice'] = np.random.random(n_points)
    data['time_period'] = np.random.random(n_points)
    data['error'] = np.random.random(n_points)
    # 生成类别标签
    data['label'] = np.round(data['practice']*data['time_period'] + 0.3 + 0.1*data['error'])
    data['label'][data['practice']>0.8] = 1
    data['label'][data['time_period']>0.8] = 1
    
    return(data)
    
if __name__ == '__main__':
    data = produce_data()