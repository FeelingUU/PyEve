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
    # a = np.arange(12).reshape([2,2,3])
    # print(a.shape)
    # print(a)
    # print(np.ravel(a))
    # print(a.flatten())
    # print("---------------------")
    # print(a.transpose(0, 2, 1))
    # print("---------------------")
    # print(a.transpose(2,0,1))


    # a = np.arange(24).reshape(2,3,4)
    # print(a)
    # print("---------------------")
    # print(np.rollaxis(a,1,0))
    # print("---------------------")
    # print(np.swapaxes(a,1,0))


    # a = np.array([[1],[2],[3]])
    # b = np.array([1,2,3])
    # c = np.broadcast(a,b)
    # print(c.shape)


    # a = np.arange(12).reshape(1,3,4)
    # b = np.arange(13,25).reshape(1,3,4)
    # print(a)
    # print(b)
    # print("---------")
    # print(np.stack((a,b),0))
    # print(np.stack((a,b),0).shape)
    # print(np.hstack((a,b)))
    # print(np.vstack((a,b)))

    # a = np.arange(12).reshape(3,4)
    # print(a.ndim)
    # print(a)
    # print(np.resize(a,(5,13)))
    # print(np.append(a,[[1,1,1,1],[1,1,1,1],[1,1,1,1]],axis=1))
    # print(np.insert(a,0,[3,4,32],axis=1))
    # print(np.stack((a,a)))
    # print(np.delete(a,2,axis=1))
    # print(np.unique(np.stack((a,a)),return_counts=True))

    # print(np.invert(-13))
    # print(np.invert(242))
    print(np.left_shift(15,2))

    print(np.char.add("aaa"," aaa"))
    print(np.char.add(["aaa"," aaa"],['dsd ',u'都是']))

    pass
