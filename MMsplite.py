# -*- coding: utf-8 -*-

# 运行库和第3方库版本
# 系统 win10 home 64bit
# Pyhon 3.7.6
# BeautifulSoup4 4.8.2
# bs4 0.0.1

# 说明  爬取源码文件必须放在一个第2级文件夹src里 例 任意路径\MM\src 下.
# 爬取的图片会保存在例：\src的上层MM文件夹里。
# time 只用time.sleep(1),以免爬取太快导致异常。



import requests
from bs4 import BeautifulSoup
import os
import time

all_url = 'https://www.mzitu.com'
 

# http请求头
Hostreferer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'http://www.mzitu.com'
}
# 此请求头Referer破解盗图链接
Picreferer = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Referer': 'http://i.meizitu.net'
}
 
headers = {
    'Cookie':'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1534513371; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1534515349',
    'Referer':'http://www.mzitu.com/xinggan/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

# 对mzitu主页all_url发起请求，将返回的HTML数据保存，便于解析
start_html = requests.get(all_url, headers=headers)

# Linux保存地址
# path = '/home/Nick/Desktop/mzitu/'
 
# Windows保存地址
path = '../'
path1='../'
# 获取最大页数
soup = BeautifulSoup(start_html.text, "html.parser")
page = soup.find_all('a', class_='page-numbers')
max_page = page[-2].text
 
# *********************************要爬取的网页主页*********************************************
# same_url = 'http://www.mzitu.com/page/'   # 主页默认最新图片
# https://www.mzitu.com/xinggan/page/ 也可以指定《性感 MM系列》
# https://www.mzitu.com/japan/page/ 《日本 MM系列》
# https://www.mzitu.com/taiwan/page/ 《台湾 MM系列》
# https://www.mzitu.com/mm/page/   《清纯 MM系列》
# 
# 获取每一类MM的网址  
same_url = 'https://www.mzitu.com/japan/page/'     # 指定获取对应MM的首页

#*********************************指定要爬取的起始页*****************************************
for n in range(1, int(max_page) + 1):
    # 拼接当前类MM的所有url
    ul = same_url + str(n)
 
    # 分别对当前类每一页第一层url发起请求
    start_html = requests.get(ul, headers=headers)
 
    # 提取所有MM的标题
    soup = BeautifulSoup(start_html.text, "html.parser")
    # limit参数  这个参数其实就是控制我们获取数据的数量，效果和SQL语句中的limit一样；
    # all_a = soup.find('div', class_='postlist').find_all('a', target='_blank',limit=20)
    all_a = soup.find('div', class_='postlist').find_all('a', target='_blank')
 
    # 遍历所有MM的标题
    for a in all_a:
        # 提取标题文本，作为文件夹名称
        title = a.get_text()
        if(title != ''):
            print("准备扒取：" + title)
            path_name=title   #可限制保存文件名称的长度 path_name=title[0:18]
            # windows不能创建带？的目录，添加判断逻辑
            # if(os.path.exists(path + title.strip().replace('?', ''))):
            if(os.path.exists(path +path_name.strip().replace('?', ''))):
                # print('目录已存在')
                flag = 1
                # break
            else:
                os.makedirs(path + path_name.strip().replace('?', ''))
                flag = 0
            # 切换到上一步创建的目录
            os.chdir(path + path_name.strip().replace('?', ''))
 
            # 提取第一层每一个MM的url，并发起请求
            href = a['href']
            html = requests.get(href, headers=Hostreferer)
            mess = BeautifulSoup(html.text, "html.parser")
 
            # 获取第二层最大页数
            pic_max = mess.find_all('span')
            pic_max = pic_max[9].text
            # if(flag == 1 and len(os.listdir(path + path_name.strip().replace('?', ''))) >= int(pic_max)):
            if(flag == 1 and len(os.listdir(path1+path_name.strip().replace('?', ''))) >= int(pic_max)):
                print('已经保存完毕，跳过')
                continue
 
            # 遍历第二层每张图片的url
            for num in range(1, int(pic_max) + 1):
                # 拼接每张图片的url
                pic = href + '/' + str(num)
 
                # 发起请求
                html = requests.get(pic, headers=Hostreferer)
                mess = BeautifulSoup(html.text, "html.parser")
                pic_url = mess.find('img', alt=title)
                print(pic_url['src'])
                time.sleep(0.5)
				# 此请求头Referer破解盗图链接
                headerss = {
                'Referer': href,
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
                }
                html = requests.get(pic_url['src'], headers=headerss)
 
                # 提取图片名字
                file_name = pic_url['src'].split(r'/')[-1]

                # 保存图片
                f = open(file_name, 'wb')
                f.write(html.content)
                f.close()
            print('完成')
    print('第', n, '页完成')

# 版权声明：本文为CSDN博主「Nick Peng」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/PY0312/article/details/101087356

