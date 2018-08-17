#!/user/bin/python
#-*- coding: utf-8 -*-
#encoding=utf-8

'''
使用bs4框架爬取花瓣网图片资源
'''

# import urllib2
# import urllib
# import os
# from BeautifulSoup import BeautifulSoup
# def getAllImageLink():
#     html = urllib2.urlopen('http://huaban.com').read()
#     soup = BeautifulSoup(html)
#
#     liRequest = soup.findAll('li', attrs={"class":"span3"})
#
#     for li in liRequest:
#         imageEntityArray = li.findAll('img')
#         for image in imageEntityArray:
#             link = image.get('data-src')
#             imageName = image.get('data-id');
#             filesavepath = '/Users/gaolong/Desktop/pics/%s.jpg'%imageName
#             urllib.urlretrieve(link,filesavepath);
#             print filesavepath
#
# if __name__ == '__main__':
#  getAllImageLink()


'''
使用bs4库解析一段html代码
'''
from bs4 import BeautifulSoup


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# html: 文本 parser:解析器,默认为html.parser
def dealHtmlDoc(html, parser='html.parser'):
    soup = BeautifulSoup(html, parser)
    print(soup.prettify())
    print(soup.title)
    print(soup.find_all('a'))
    print(soup.head)
    for string in soup.strings:
        print(repr(string))
    for link in soup.find_all('a'):
        print(link.get('href'))

# dealHtmlDoc(html_doc)
dealHtmlDoc(html_doc, 'lxml')

'''
本案例用来爬取图片
'''
# import urllib2
# import urllib
# import os
# from BeautifulSoup import BeautifulSoup
# def getAllImageLink():
#     html = urllib2.urlopen('http://image.baidu.com/').read()
#     soup = BeautifulSoup(html)
#
#     liResult = soup.findAll('li',attrs={"class":"span3"})
#
#     for li in liResult:
#         imageEntityArray = li.findAll('img')
#         for image in imageEntityArray:
#             link = image.get('data-src')
#             imageName = image.get('data-id')
#             filesavepath = '/Users/weihua0618/Desktop/meizipicture/%s.jpg' % imageName
#             urllib.urlretrieve(link,filesavepath)
#             print filesavepath
#
# if __name__ == '__main__':
#     getAllImageLink()




