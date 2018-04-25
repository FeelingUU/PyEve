import requests
import json
import time
from Crypto.Cipher import AES
import base64

action_data = {
    "score": 1888,
    "times": 10,
   
}

session_id = "K+p56s4U0E73Upeck27euf3/LrHg6N6ftfL27fCjdsDFaP+Cma91op1YQd6UecV1moDE5vKuxRjZRmN/gszgtLjzTwZMLrm6x67Z3Q51XefIJggUvKdsPC4+c/hUf6MJNGdQay5IQ2HD8Rb4nlSQQw=="

aes_key = session_id[0:16]
aes_iv  = aes_key

cryptor = AES.new(aes_key, AES.MODE_CBC, aes_iv)

str_action_data = json.dumps(action_data).encode("utf-8")
print("json_str_action_data ", str_action_data)

#Pkcs7
length = 16 - (len(str_action_data) % 16)
str_action_data += chr(length)*length

cipher_action_data = base64.b64encode(cryptor.encrypt(str_action_data)).decode("utf-8")
print("action_data ", cipher_action_data)

post_data = {
  "base_req": {
    "session_id": session_id,
    "fast": 1,
  },
  "action_data": cipher_action_data
}

headers = {
    "charset": "utf-8",
    "Accept-Encoding": "gzip",
    "referer": "https://servicewechat.com/wx7c8d593b2c3a7703/3/page-frame.html",
    "content-type": "application/json",
    "User-Agent": "MicroMessenger/6.6.1.1200(0x26060130) NetType/WIFI Language/zh_CN",
    "Content-Length": "0",
    "Host": "mp.weixin.qq.com",
    "Connection": "Keep-Alive"
}

url = "https://mp.weixin.qq.com/wxagame/wxagame_settlement"


response = requests.post(url, json=post_data, headers=headers)
print(json.loads(response.text))
