# 爬取豆瓣电影排行榜


import re
import urllib.request

# 构造请求头信息
headers = {
"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"
}

# https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=
# https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=100豆瓣剧情片排名url
# https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=0&limit=100豆瓣科幻片排名url
# https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=100豆瓣喜剧片排名url
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=100豆瓣动作片排行榜url
# https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&start=0&limit=100豆瓣动画片分类排行榜url
# https://movie.douban.com/j/chart/top_list?type=20&interval_id=100%3A90&action=&start=0&limit=100豆瓣恐怖片分类排行榜url
# https://movie.douban.com/j/chart/top_list?type=1&interval_id=100%3A90&action=&start=0&limit=100豆瓣纪录片分类排行榜url
# https://movie.douban.com/j/chart/top_list?type=16&interval_id=100%3A90&action=&start=0&limit=100豆瓣奇幻片排行榜url
# https://movie.douban.com/j/chart/top_list?type=29&interval_id=100%3A90&action=&start=0&limit=100豆瓣武侠片排行榜url
# https://movie.douban.com/j/chart/top_list?type=12&interval_id=100%3A90&action=&start=0&limit=100豆瓣灾难片排行榜url





url="https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&start=0&limit=100" 

req=urllib.request.Request(url,headers=headers)

data=urllib.request.urlopen(req).read().decode() #拿都数据

# print(data) #验证是否拿到数据


# 对数据进行清洗

# "rating":["9.7","50"]
# "title":"肖申克的救赎"

pat1=r'"rating":\["(.*?)","\d+"\]'
pat2=r'"title":"(.*?)"'

pattern1=re.compile(pat1,re.I)
pattern2=re.compile(pat2,re.I)

data1=pattern1.findall(data)
data2=pattern2.findall(data)
# print(data1,data2)

for i in range(len(data1)):
	print("排名:",i+1,"电影名:",data2[i],"豆瓣评分:",data1[i])