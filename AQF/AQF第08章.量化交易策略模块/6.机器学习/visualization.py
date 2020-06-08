
import numpy as np
import matplotlib.pyplot as plt


def plot_pic(clf, X_test, y_test):
    x_min = 0.0; x_max = 1.0
    y_min = 0.0; y_max = 1.0
    
    # 画出决策边界，我们为每一个点绘制一个颜色

    step = .01  # 设置步长
    xx, yy = np.meshgrid(np.arange(x_min, x_max, step), np.arange(y_min, y_max, step))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # 绘图
    Z = Z.reshape(xx.shape)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    plt.pcolormesh(xx, yy, Z, cmap=plt.cm.RdYlBu)


    data = X_test.copy()
    data['label'] = y_test
    
    practice_fail = data[data['label']==0]['practice']
    time_period_fail = data[data['label']==0]['time_period']
    practice_pass = data[data['label']==1]['practice']
    time_period_pass = data[data['label']==1]['time_period']


    plt.scatter(practice_fail, time_period_fail, color = 'b', label='fail')
    plt.scatter(practice_pass, time_period_pass, color = 'r', label='pass')
    plt.legend()
    plt.xlabel('practice')
    plt.ylabel('time_period')
    plt.legend(loc='upper right')


