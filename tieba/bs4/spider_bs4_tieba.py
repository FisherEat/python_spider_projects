"""
抓取百度贴吧---生活大爆炸吧的基本内容
爬虫线路： requests - bs4
Python版本： 3.6
OS： mac os 12.12.4
"""

# 字符串编码的坑: http://blog.csdn.net/zm2714/article/details/8012474
# -*- coding: utf-8 -*-

import requests
import codecs
from bs4 import BeautifulSoup


# 首先我们写好抓取网页的函数
def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # 这里我们知道百度贴吧的编码是utf-8，所以手动设置的。爬取其他的页面时建议使用：
        # r.endcodding = r.apparent_endconding
        r.encoding = 'utf-8'
        return r.text
    except:
        return " ERROR "


def get_content(url):
    """
    分析贴吧的网页文件，整理信息，保存在列表变量中
    """

    # 初始化一个列表来保存所有的帖子信息：
    comments = []
    # 首先，我们把需要爬取信息的网页下载到本地
    html = get_html(url)

    # 我们来做一锅汤
    soup = BeautifulSoup(html, 'lxml')

    # 按照之前的分析，我们找到所有具有‘ j_thread_list clearfix’属性的li标签。返回一个列表类型。
    li_tags = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})

    # 通过循环找到每个帖子里的我们需要的信息：
    for li in li_tags:
        # 初始化一个字典来存储文章信息
        comment = {}
        # 这里使用一个try except 防止爬虫找不到信息从而停止运行
        try:
            # 开始筛选信息，并保存到字典中
            a = li.find('a', attrs={'class': 'j_th_tit '})

            comment['title'] = a.text

            comment['link'] = "http://tieba.baidu.com/" + \
                              li.find('a', attrs={'class': 'j_th_tit '})['href']

            name = li.find('span', attrs={'class': 'tb_icon_author '})

            comment['name'] = name.text

            time_tag = li.find('span', attrs={'class': 'pull-right is_show_create_time'})

            comment['time'] = time_tag.text

            reply = li.find('span', attrs={'class': 'threadlist_rep_num center_text'})

            comment['replyNum'] = reply.text

            comments.append(comment)
        except:
            print('出了点小问题')

    return comments


def out_file(dict):
    """
    将爬取到的文件写入到本地
    保存到当前目录的 TT.txt文件中。
    此处之前使用系统builtin的open方法,一直报Unicode编码错误
    改成codecs方法打开文本文件后,解决了该问题
    """
    with codecs.open('TT.txt', 'a+', 'utf-8') as f:
        for comment in dict:
            f.write('标题： {} \t 链接：{} \t 发帖人：{} \t 发帖时间：{} \t 回复数量： {} \n'.format(
                    comment['title'], comment['link'], comment['name'], comment['time'], comment['replyNum']))

        print('当前页面爬取完成')


def main(base_url, deep):
    url_list = []
    # 将所有需要爬去的url存入列表
    for i in range(0, deep):
        url_list.append(base_url + '&pn=' + str(50 * i))
    print('所有的网页已经下载到本地！ 开始筛选信息。。。。')

    # 循环写入所有的数据
    for url in url_list:
        content = get_content(url)
        out_file(content)
    print('所有的信息都已经保存完毕！')

base_url = 'http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8'
# 设置需要爬取的页码数量
deep = 1

if __name__ == '__main__':
    main(base_url, deep)
