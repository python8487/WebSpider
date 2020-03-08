# !/usr/bin/env python
# _*_ coding:utf-8 _*_

# 根据url发生请求，获取服务器响应文件
# 将html内容写入到本地
# 处理每个页面的url


import urllib
# import urllib.request
from urllib import request
import time

# 构造请求头信息
header = {
"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"
}

# url规律
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=0 #第1页 （1-1）*50
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=50 #第2页（2-1）*50
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=100 #第3页（3-1）*50
# http://tieba.baidu.com/f?kw=python&ie=utf-8&pn=150 #第4页 (4-1）*50

# for i in range(1,5):
# 	print("http://tieba.baidu.com/f?kw=python&ie=utf-8&pn="+str((i-1)*50))


def loadpage(fullurl,filename):
	print("正在下载:",filename)
	req = request.Request(fullurl,headers = header)
	resp = request.urlopen(req).read()
	return resp


def writepage(html,filename):
	print("正在保存：",filename)

	with open(filename,"wb") as f:
		f.write(html)

	print("------------------------------------")

# 构造url

def tiebaSpider(url,begin,end):
	for page in range(begin,end+1):
		pn = (page - 1) * 50
		fullurl = url + "&pn=" + str(pn)  #每次请求的完整url
		filename="d:/tieba/"+str(kw)+"贴吧第" + str(page) + "页.html" #每次请求后保存的文件名
		print("http://tieba.baidu.com/f?kw=python&ie=utf-8&pn="+str((page-1)*50))

		html = loadpage(fullurl,filename) #调用爬虫，爬取网页
		writepage(html,filename) #把获取到的网页信息写入本地


if __name__ == '__main__':
	kw = input("请输入贴吧名：")
	begin = int(input("请输入起始页："))
	end = int(input("请输入结束页页："))

	url = "http://tieba.baidu.com/f?"

	key = urllib.parse.urlencode({"kw":kw})

	url = url + key

	tiebaSpider(url,begin,end)

	
	time.sleep(10)
	print("爬取贴吧网页结束")


















