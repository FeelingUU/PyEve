# coding:utf-8
import requests,re
from bs4 import BeautifulSoup as bs
def test_reptile():
    html = requests.get('http://tieba.baidu.com/p/2166231880').content.decode('utf-8')
    patten = '(http.*?.jpg)'
    url_list = re.findall(patten,html)
    index = 1
    for x in url_list:
        x = x[x.rfind('http'):]
        if 'head_80' in x or '://' not in x:
            continue

        image = requests.get(x)
        with open('F:/2236/'+str(index)+'.jpg','wb') as f:
            f.write(image.content)
        index +=1
    pass

def test_reptile2():
    html = requests.get('http://tieba.baidu.com/p/2166231880').content.decode('utf-8')
    # print(html)

    soup = bs(html,features='lxml')
    a_tag = soup.find_all('a')

    for x in a_tag:

        if 'href' in str(x):
            print(x)
            print(x['href'].replace('&amp;','&'))


    pass

def test_xinlangPingLun():
    html = requests.get('https://weibo.com/1776448504/GoNKlkzpR?filter=hot&root_comment_id=0&type=comment#_rnd1530991303459').content.decode('gbk')
    print(html)

    # soup = bs(html,features='lxml')
    # a_tag = soup.find_all('a')
    #
    # for x in a_tag:
    #
    #     if 'href' in str(x):
    #         print(x)
    #         print(x['href'].replace('&amp;','&'))


    pass

if __name__ == '__main__':
    test_xinlangPingLun()