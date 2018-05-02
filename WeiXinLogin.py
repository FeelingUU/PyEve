#-*-coding:utf-8-*-
import itchat
def login():
    itchat.login()

    itchat.send(u'你好', 'filehelper')
    pass

if __name__ == '__main__':
    login()
