
import requests
import re
import time
# 构造请求头信息
header = {
"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"
}


# 网页分析# 好听轻音乐榜单第1页url
# http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20
# # 榜单第2页url
# http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20
# # 榜单第3页url
# http://www.htqyy.com/top/musicList/hot?pageIndex=2&pageSize=20

# 歌曲的url http://www.htqyy.com/play/33
# 资源所在url http://f2.htqyy.com/play7/33/mp3/2    'play7 /2 经常变换要灵活运用'
# 歌名，歌ID数据分析
# <span class="title"><a href="/play/261" target="play" title="荡涤心灵的天籁之音" sid="261">荡涤心灵的天籁之音</a></span>


print("******您好！欢迎使用好听轻音乐网热播榜爬虫程序下载轻音乐(好听轻音乐网址http://www.htqyy.com)******")
print("创建歌曲存储路径必须为D:\\music\\htqmusic(请注意存储路径!!!) \n")
page=int(input("请输入您在好听轻音乐网热播榜需要爬取的页数（20首/页）："))
print("\n")

songID=[]
songName=[]


for i in range(0,page):
	url="http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"&pageSize=20"
	# 获取音乐榜单的网页信息
	html=requests.get(url)

	strr=html.text

	pat1=r'title="(.*?)" sid'
	pat2=r'sid="(.*?)"'

	idlist=re.findall(pat2,strr)
	titlelist=re.findall(pat1,strr)

	songID.extend(idlist)
	songName.extend(titlelist)


for i in range(0,len(songID)):
	songurl= "http://f2.htqyy.com/play7/"+str(songID[i])+"/mp3/2"
	songname=songName[i]

	data=requests.get(songurl).content

	print("正在下载好听轻音乐热播榜单第",i+1,"首歌:",songname)

	with open("D:\\music\\htqmusic\\{}.mp3".format(songname),"wb") as f:   #将下载的MP3保存写入到指定位置
		f.write(data)

	time.sleep(1)

print("********下载结束，欢迎使用************")
# print(len(songID))
# print(len(songName))






