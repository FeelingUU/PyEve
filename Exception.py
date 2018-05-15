#-*-coding:utf-8-*-
def test():
    try:
        print(1/0)
    except BaseException as e:
        print(e.with_traceback())
    pass

if __name__ == '__main__':
    test()