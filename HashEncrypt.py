#-*-coding:utf-8-*-
import hashlib

def encrypt():
    m = hashlib.md5(u'A'.encode('utf-8')).hexdigest()
    print(m)

    q = hashlib.sha3_224(b'123').hexdigest()
    print(q)

    f = open("C:/Users/Am/Desktop/22.ttf")
    lines = f.readlines()
    line_str = ''
    for x in lines:
        line_str +=x
    # print(encode(line_str))
    # print(hashlib.md5(line_str.encode('utf-8')).hexdigest())
    print(hashlib.md5(line_str).hexdigest())
    f.close()

    pass

def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])

def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])

if __name__ == '__main__':
    encrypt()