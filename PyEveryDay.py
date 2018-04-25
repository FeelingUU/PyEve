# -*-coding:utf-8-*-
import time, sys, random, string, pymysql, redis, os,urllib.request,re
from PIL import Image, ImageFont, ImageDraw


# 图片右上角添加红色数字
def _0001():
    try:
        pic = Image.open('C:/Users/Am/Desktop/237.png')
        font = ImageFont.truetype("C:/Users/Am/Desktop/22.ttf", 24)

        draw = ImageDraw.Draw(pic)
        draw.text((200, 5), "66", (255, 100, 245), font=font)

        pic.save("C:/Users/Am/Desktop/237.png")
    except BaseException:
        print('error')


# 生成验证码图片
def _0002():
    pic = Image.new("RGBA", (300, 150), (255, 255, 255))

    for x in range(0, pic.width):
        for y in range(0, pic.height):
            pic.putpixel((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    font = ImageFont.truetype("C:/Users/Am/Desktop/22.ttf", 50)
    draw = ImageDraw.Draw(pic)
    text = ''.join(random.sample(string.ascii_uppercase + string.digits, 4))
    draw.text((90, 30), text, (0, 0, 0), font=font)

    pic.save("C:/Users/Am/Desktop/11.png")
    pass


# 连接mysql并执行
def _0003():
    con = pymysql.connect(host="", port=1, user='', passwd='', db='', charset='utf-8')
    cursor = con.cursor()
    data = cursor.execute("select * from wdawdaw")

    pass


# 连接redis
def _0004():
    r = redis.Redis(host='', port=1, password='')
    r.get('')

    pass


# 图片缩小
def _0005():
    for x,y,z in os.walk('H:/2235'):
        for file in z :
            print(x+file)
    # pic = Image.open("")
    # out = pic.resize((pic.width//2, pic.height//2))
    # out.show()
    pass

#爬图片
def _0006():

    url = "https://www.zhihu.com/question/36704909"
    fileType = 'jpg'
    filePath = 'H:/2236/'
    if not os.path.isdir(filePath):
        os.makedirs(filePath)
    try:
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8')

        reg = "http.*?."+fileType
        patten = re.compile(reg)
        url_list = re.findall(patten,html)

        url_list = [str(x)[str(x).rfind("http"):len(x)].strip().replace('&amp;','').replace("\\","") for x in url_list]
        url_list = list(set(url_list))

        index = len(os.listdir(filePath))+1

        for x in url_list:
            if "_xs.jpg" in x or "_is.jpg" in x or "_l.jpg" in x or "_hd.jpg" not in x:
                continue
            print(str(index)+' '+x)
            try:
                urllib.request.urlretrieve(x,filePath+str(index)+"."+fileType)
                index+=1
            except BaseException:
                print("下载失败 "+ x)
    except BaseException as e:
        print(e)

    pass

if __name__ == '__main__':
    _0006()
