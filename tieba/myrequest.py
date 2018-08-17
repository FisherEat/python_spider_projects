'''
本案例是使用 requests框架请求某网站的内容
'''

import requests

payload = dict(catCircleId=440,token="WI2mckjyehQREIKq3h4_AndAYrVxUKsy3498", type=1)
r = requests.post("http://app.yirimao.com/cat-circle/like", data=payload)
print(r.text)


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Something wrong!"


if __name__ == '__main__':
    print('shit')
   # print(getHtmlText("http://www.baidu.com"))
