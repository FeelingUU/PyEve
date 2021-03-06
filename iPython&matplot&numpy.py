# -*-coding:utf-8-*-

import numpy as np
import matplotlib.pyplot as plt
import numpy.matlib
import os



def test_ndarray():
    print(np.array([[1, 23, 4, 5], [2, 2]]))


def test_numpy():
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
    # print(np.left_shift(15,2))

    # print(np.char.add(["aaa"],[" aaa"]))
    # print(np.char.add(["aaa"," aaa"],['dsd ',u'都是']))
    # print(np.char.multiply('hey ',3))
    # print('hey '*3)
    # print(np.char.center('dadasdf',14,fillchar="*"))
    # print(np.char.capitalize('dsad,asda'))
    # print(np.char.title('1dsad.asda'))
    # print(np.char.lower(['wDSADS','DASDASD']))
    # print(np.char.split('sds s,dsd'))
    # print(np.char.split('sds s,dsd',sep=","))
    # print(str.strip('epweweeq','eq'))
    # print('das '.strip())
    # print(np.char.join('-!','asdasd'))
    # print(np.char.join(['-',':'],['12e22','asdasd']))
    # print(np.char.decode(b'sdasdasd','utf-8'))

    # print(np.sin(np.array([30,60,45])*np.pi/180))
    # print(np.cos(30*np.pi/180))
    # print(np.tan(30*np.pi/180))
    # print(np.tan(60*np.pi/180))
    #
    # print(np.arcsin(0.5)*180/np.pi)
    # print(np.around(9.0,decimals=0))
    # print(np.ceil(1.1))

    # a = np.array([[1,2,3],[4,4,4]])
    # b = np.array([1,1,4])
    #
    # print(np.add(a,b))
    # print(np.subtract(a,b))
    # print(np.multiply(a,b))
    # print(np.divide(a,b))

    # print(np.reciprocal([2.0,3.0]))
    # print(np.power(np.array([1,2,3]),[2,3,4]))
    #
    # print(np.mod(np.array([1,2,3]),[1,2,4]))
    # print(np.remainder(np.array([1,2,3]),2))

    # a = -2 - 0j
    # print(np.angle(a, deg=True))
    # print(np.amax([[4, 2, 1], [22, 23, 54], [0, 44, 33]], axis=0))
    # print(np.maximum([1, 23, 3], [2, 3, 4]))

    print('--------------------')

    # print(np.amax(b,2))
    # print(np.ptp(b,axis=0))
    # print(np.percentile(b, 50, axis=2))
    # print(np.percentile(b, 60, axis=2))
    # print(np.percentile(a,70))
    # print(np.median(b))
    # print(np.mean(b,axis=2))
    # print(np.average(b,axis=2,weights=b))
    # print(np.var(a))
    # print(np.std(a))

    # b = np.array([[[1, 2, 3, 4], [3, 4, 30, 40]], [[1.5, 2, 4, 3], [1, 2, 6, 10]]])
    # a = np.array([1, 3, 7, 12, 10])
    # c = np.array([16, 17, 21, 32, 26])
    # d = a.copy()
    # a[0] = 1112
    # print(np.sort(b,axis=2))
    # print(b)
    # print('--------------------')
    # print(np.sort(b,axis=2,kind='quicksort'))
    # print('--------------------')
    # print(np.sort(b,axis=2,kind='mergesort'))
    # print(np.argsort(a))
    # print(np.lexsort((c,a)))
    # print([str(a[i])+" "+str(c[i]) for i in np.lexsort((c,a))])
    #
    # print(np.argmax(a))
    # # print(np.nonzero(b))
    # print(np.where(a>3))
    # print(np.extract(a>1,a))
    # a.byteswap()
    # print(id(a))
    # print(id(d))
    # print(a)
    # print(d)

    # print(np.matlib.empty((3,3)))
    # print(np.matlib.zeros((3,3)))
    # print(np.matlib.ones((3,3)))
    # print(np.matlib.eye(n=3,M=3,k=1))
    # print(np.matlib.identity(5))
    # print(np.matlib.rand(3,3))

    a = np.array([[1, 3, 4], [12, 10, 0], [12, 10, 1]])
    b = np.array([[2, 4], [1, 2]])
    c = np.array([1, 1, 3])

    # print(np.dot(a,b))
    # print(np.vdot(a,b))
    # print(np.inner(a,b))
    # print(np.matmul(a,b))
    print(np.linalg.det(a))
    print(np.linalg.solve(a, c))
    print(np.dot(np.linalg.inv(a), a))


def test_ddd():
    iu = plt.imread(os.path.join(os.path.expanduser("~"), 'Desktop') + r'/20150.jpeg')
    print(iu.shape)
    iu2 = iu[:,::-1]
    plt.imshow(iu2)
    plt.show()


def test_fft():
    from numpy.fft import fft,ifft
    from PIL import Image

    cp = Image.open('C:/Users/Am/Desktop/chuanpu.jpg')
    cp_data = np.fromstring(cp.tobytes(),dtype=np.int8)
    cp_fft = fft(cp_data)

    cp_fft_where = np.where(np.abs(cp_fft) < 1e5, 0, cp_fft)
    cp_ifft_where = ifft(cp_fft_where)
    cp_new = Image.frombytes(data=np.int8(cp_ifft_where.real),size=cp.size,mode=cp.mode)
    cp_new.show()


    pass

def test_drawFunc():
    x = np.arange(-10, 10, 0.01)
    # y = np.sin(x)
    # y1 = x  + np.square(x) + np.sqrt(x**3)
    y1 = 1/(1+np.power(np.e,-x))
    # y2 = 10*x
    # plt.subplot(2,1,1)
    # plt.plot(x, y1,"|",color='red')
    # plt.subplot(2, 1, 2)
    # plt.plot(x, y2,"|",color='red')
    # plt.show()

    plt.figure()
    plt.plot(x,y1)
    # plt.figure()
    # plt.plot(x, y1,color='red',linewidth = 2.0,linestyle='--')
    # plt.plot(x, y2)
    plt.show()


    # 柱状图
    # x = [5, 8, 11]
    # y = [12, 16, 6]
    # x2 = [6, 9, 12]
    # y2 = [6, 15, 7]
    # plt.bar(x, y, align='center')
    # plt.bar(x2, y2, color='g', align='center')
    # plt.title('Bar graph')
    # plt.ylabel('Y axis')
    # plt.xlabel('X axis')
    # plt.show()


if __name__ == '__main__':
    test_drawFunc()
    pass
