'''
爬取最新电影排行榜单
URL:http://dianying.2345.com/top/
使用requests --- bs4线路
Python版本:3.6
OS: mac os
'''

import requests
import codecs
import bs4

def get_html(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        #该网站采用gbk编码
        r.ecoding='gbk'
        return r.text
    except:
        return "Something wrong"

def get_content(url):
    html = get_html(url)
    soup = bs4.BeautifulSoup(html, 'lxml')
     # 找到电影排行榜的ul列表
    movies_list = soup.find('ul', class_='picList clearfix')
    movies = movies_list.find_all('li')

    for top in movies:
        #找到图片连接
        img_url = top.find('img')['src']
        name = top.find('span', class_='sTit').a.text
        #这里做一个异常捕获，防止没有上映时间的出现
        try:
            time = top.find('span', class_='slntro').text
        except:
            time="暂无上映时间"

        #这里用bs4库迭代找出“pACtor”的所有子孙节点，即每一位演员解决了名字分割的问题
        try:
            actors = top.find('p', class_='pActor')
            actor = ''
            for act in actors.contents:
                actor = actor+act.string+''
        except:
            print('Actors error')
        #找到影片简介
        intro = top.find('p', class_='pTxt pIntroShow').text
        print("片名：{}\t{}\n{}\n{} \n \n ".format(name,time,actors,intro) )

        #我们来把图片下载下来：
        with codecs.open('/Users/gl/Desktop/untitled/img/'+name+'.png','wb+') as f:
            f.write(requests.get(img_url).content)



def main():
    url = 'http://dianying.2345.com/top/'
    get_content(url)

if __name__ == '__main__':
    main()

