#-*-coding:utf-8-*-


class mi(object):
    def __init__(self):
        pass

    def mitest(self):
        print('mi test')

class ni(object):
    def __init__(self):
        pass

    def nitest(self):
        print('ni test')

class TT(mi):
    def __init__(self):
        pass

    def test(self):
        try:
            print('sdasd')
            self.mitest()
            mi.mitest(self)
        except BaseException as e:
            print(e.with_traceback())
        pass


if __name__ == '__main__':
    t = TT()
    t.test()
    pass