#-*-coding:utf-8-*-
import threading

def target_func():
    print(threading.current_thread().name)

def test_thread():
    try:
        thread_list = [threading.Thread(target=target_func,name="thr"+str(x)) for x in range(0,11)]
        for i in thread_list:
            i.start()
        for i in thread_list:
            i.join()
    except BaseException as e:
        print(e)

if __name__ == '__main__':
    test_thread();
    print("asdads")

