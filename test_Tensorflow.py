# coding:utf-8/
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import time
import matplotlib.animation as ani

def test_tensorflow():
    # 数据源
    x_data = np.random.rand(100).astype(np.float32)
    y_data = x_data*0.1 +0.3

    # 创建结构

    Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
    biases = tf.Variable(tf.zeros([1]))

    y = Weights*x_data + biases

    loss = tf.reduce_mean(tf.square(y-y_data))
    optimizer = tf.train.GradientDescentOptimizer(0.5)
    train = optimizer.minimize(loss)

    init = tf.global_variables_initializer()

    # 初始化
    sess = tf.Session()
    sess.run(init)    #激活init

    for x in range(201):
        sess.run(train)
        if x%20 == 0:
            print(x,sess.run(Weights),sess.run(biases))
    pass


def test_tensorflow2():
    matrix1 = tf.constant([[3,3]])
    matrix2 = tf.constant([[2],[2]])

    product = tf.matmul(matrix1,matrix2)

    # sess = tf.Session()
    # res = sess.run(product)

    # print(res)
    # sess.close()

    with tf.Session() as sess2:
        res2 = sess2.run(product)
        print(res2)

    pass

def test_tensorflow3():

    state = tf.Variable(0,name='counter')
    # print(state.name)
    one = tf.constant(1)

    new_value = tf.add(state,one)
    update = tf.assign(state,new_value)

    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        for _ in range(3):
            sess.run(update)
            print(sess.run(state))



    pass

def test_tensorflow4():
    input1 = tf.placeholder(tf.float32)
    input2 = tf.placeholder(tf.float32)

    output = tf.multiply(input1,input2)

    tf.global_variables_initializer()
    with tf.Session() as sess:
        print(sess.run(output,feed_dict={input1:[3.0],input2:[3.0]}))
    pass


def add_layer(inputs,in_size,out_size,layer_name,activition_function=None):
    with tf.name_scope(layer_name):
        with tf.name_scope('weights'):
            Weights = tf.Variable(tf.random_normal([in_size,out_size]),name='weights')
            tf.summary.histogram(layer_name+'weights',Weights)
        with tf.name_scope('biases'):
            biases = tf.Variable(tf.zeros([1,out_size])+0.1,name='biases')
            tf.summary.histogram(layer_name + 'biases',biases)
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b = tf.matmul(np.power(inputs,2),Weights)+biases

        if activition_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activition_function(Wx_plus_b)
            tf.summary.histogram(layer_name + 'outputs',outputs)
        return outputs

    pass

def test_tensorflow5():
    x_data = np.linspace(-1,1,300)[:,np.newaxis]
    noise = np.random.normal(0,0.05,x_data.shape)
    y_data = np.square(x_data) - 0.5 + noise

    with tf.name_scope('inputs'):
        xs = tf.placeholder(tf.float32,[None,1],name='x_input')
        ys = tf.placeholder(tf.float32,[None,1],name='y_input')


    l1 = add_layer(xs,1,10,layer_name='layer_1',activition_function=tf.nn.relu)
    prediction = add_layer(l1,10,1,layer_name='layer_2',activition_function=None)
    with tf.name_scope('loss'):
        loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))
        tf.summary.scalar('loss',loss)
    with tf.name_scope('train_step'):
        train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    init = tf.global_variables_initializer()


    with tf.Session() as sess:
        # merge = tf.summary.merge_all()
        # writer = tf.summary.FileWriter('E:/',sess.graph)

        sess.run(init)

        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.scatter(x_data, y_data)

        for x in range(1000):
            sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
            if x%100 ==0:
                # print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
                try:
                    ax.lines.remove(lines[0])
                except BaseException:
                    print('pass')

                prediction_value = sess.run(prediction,feed_dict={xs:x_data})
                lines = ax.plot(x_data,prediction_value,'r-',lw = 5)

                # result = sess.run(merge,feed_dict={xs:x_data,ys:y_data})
                # writer.add_summary(result,x)

                plt.pause(0.1)
        plt.ioff()
        plt.show()



    pass

if __name__ == '__main__':
    test_tensorflow5()