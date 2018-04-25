import re

s = '''https://camo.githubusercontent.com/d6aaa1fd3e238860cb9ce736cc8bdae628117508/687474703a2f2f692e696d6775722e636f6d2h
"ttps://camo.githubusercontent.com/d6aaa1fd3e238860cb9ce736cc8bdae628117508/687474703a2f2f692e696d6775722e636f6d2f4e45
"66377a4870SpringSide 版TodoList http://i.imgur.com/NEf7zHp.jpg'''.rfind("http")

print(s)