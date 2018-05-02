#-*-coding:utf-8-*-

import numpy as np
import matplotlib.pyplot as plt


def test_drawFunc():
    x = np.arange(-5, 5, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()

def test_ndarray():
    print(np.array([[1,23,4,5],[2,2]]))



if __name__ == '__main__':
    test_ndarray()