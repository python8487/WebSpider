#本爬虫仅用于学习，纯属爱好，虽然本爬虫很简单，但还是请大家不要滥用
#python3, Firefox浏览器
 
import requests
from bs4 import BeautifulSoup
import time
import csv
import re
 
# 定制请求头，请求头在浏览器中查看，具体方法见附录一
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
}
 
# 将要访问的网址


# 贝壳二手房地址
# https://wh.ke.com/ershoufang/jiyuqiao/
# https://wh.ke.com/ershoufang/jiyuqiao/pg3/


link = 'https://wh.ke.com/ershoufang/jiyuqiao/'
# 武汉积玉桥二手房源地址
# https://wh.ke.com/ershoufang/jiyuqiao/pg1/


    # 将爬取的内容写入 test.csv中，编码格式为 'UTF-8'
# with open('贝壳二手房源信息.csv', 'w+', encoding='UTF-8', newline='') as csvfile:
#     w = csv.writer(csvfile)
#     csv_title = ["名称", "地址", "房屋信息", "总价", "单价", "房屋标签", "对应网址"]
#     w.writerow(csv_title)





# 访问该网站
for i in range(1,3):
    print("爬取第{:2.0f}页数据".format(i))
    # ****指定需要爬取地址的网页信息
    url = 'https://wh.ke.com/ershoufang/jiyuqiao/pg'+str(i)
    # print(url)
    r = requests.get(url, headers=headers, timeout=100)
     
    # 使用BeautifulSoup提取html中的内容
    # BeautifulSoup 中文官方文档：https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id37
    soup = BeautifulSoup(r.text, 'lxml')

# <li class="list-item" data-from="">网页分析
    house_list = soup.find_all('li', class_="clear")
    # house_list = soup.find_all('div', class_="zu-info")

    with open('info.csv', 'w+', encoding='UTF-8', newline='') as csvfile:
        # with open('test.csv', 'a+', encoding='UTF-8', newline='') as csvfile:
        w = csv.writer(csvfile)
        # csv_title = ["名称", "地址", "房屋信息", "总价", "单价", "房屋标签", "对应网址"]
        # w.writerow(csv_title)


        for house in house_list:
            temp = []


            name = house.find('div', class_="title").a.text.strip()
            address = house.find('div', class_='address').a.text.strip()
            houseinfo = house.find('div', class_='houseInfo').text.strip()
            # 用正则表达式清洗抓取数据里的特殊字符
            a = re.compile(r'\n|&nbsp|\xa0|\\xa0|\u3000|\\u3000|\\u0020|\u0020|\t|\r')
            clean_houseinfo = a.sub('', houseinfo)

            '''
            <div class="tag">
                <span class="subway">近地铁</span>
                <span class="isVrFutureHome">VR房源</span>
                <span class="is_key">随时看房</span>
            </div>
            '''
            house_tag = house.find('div', class_='tag').get_text("|",strip=True)

            price = house.find('div', class_='totalPrice').text.strip()
            untiPrice = house.find('div', class_='unitPrice').span.text.strip()

            '''
            <a class="img  CLICKDATA maidian-detail" data-hreftype="0" data-agentid="" data-maidian="289817724040429593" href="https://wh.ke.com/ershoufang/18082910510101140675.html" target="_blank" title="绿地名邸公馆毛坯两房，无遮挡，交通便利，看房方便！" >
                <img class="lj-lazy" src="https://ke-image.ljcdn.com/420100-inspection/test-58ab606f-b6bf-49e1-8c29-5cbd4e28a888.png!m_fill,w_280,h_210,f_jpg?from=ke.com" data-original="https://ke-image.ljcdn.com/420100-inspection/test-58ab606f-b6bf-49e1-8c29-5cbd4e28a888.png!m_fill>
                <img src="https://s1.ljcdn.com/pegasus/redskull/images/common/vrlogo@2x.png?_v=20200310144440" class="vr_logo">
            </a>
            '''
            # 分析上面的html语句抓取相应url地址
            house_url = house.select("a")[0]["href"]
            print(house_url)


            temp = [name + clean_houseinfo, address, price, house_url, untiPrice, house_tag]
            print(temp)


            time.sleep(0.5)
            # 写入表格（贝壳二手房源信息.csv）
            w.writerow(temp)




