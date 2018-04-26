#-*-coding:utf-8-*-

import numpy as np
import matplotlib.pyplot as plt


def test_drawFunc():
    x = np.arange(-5, 5, 0.1)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()



if __name__ == '__main__':
    test_drawFunc()