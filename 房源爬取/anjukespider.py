#本爬虫仅用于学习，纯属爱好，虽然本爬虫很简单，但还是请大家不要滥用
#python3, Firefox浏览器
 
import requests
from bs4 import BeautifulSoup
import time
import csv
 
# 定制请求头，请求头在浏览器中查看，具体方法见附录一
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0',
}
 
# 将要访问的网址


# 天门安居客租房房源分析
# https://tm.zu.anjuke.com/fangyuan/p1/
# https://wuhan.anjuke.com/sale/wuchanga-q-jiyuqiao/p2

# 天门安居客二手房房源分析
# https://tianmen.anjuke.com/sale/p1
# https://tianmen.anjuke.com/sale/p2
# link = 'https://beijing.anjuke.com/sale/'
link = 'https://tianmen.anjuke.com/sale/'
# https://tianmen.anjuke.com/sale/p1/
# 
# https://tianmen.anjuke.com/sale/p3/#filtersort
# 访问该网站

for i in range(1,11):
    print("爬取第{:2.0f}页数据".format(i))
    # ****指定需要爬取地址的网页信息
    url = 'https://wuhan.anjuke.com/sale/wuchanga-q-jiyuqiao/p'+str(i)
    print(url)
    r = requests.get(url, headers=headers, timeout=100)
     
    # 使用BeautifulSoup提取html中的内容
    # BeautifulSoup 中文官方文档：https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id37
    soup = BeautifulSoup(r.text, 'lxml')

# <li class="list-item" data-from="">网页分析
    house_list = soup.find_all('li', class_="list-item")
    # house_list = soup.find_all('div', class_="zu-info")

    # 将爬取的内容写入 test.csv中，编码格式为 'UTF-8'
    with open('test.csv', 'a+', encoding='UTF-8', newline='') as csvfile:

    # with open('test.csv', 'w+', encoding='UTF-8', newline='') as csvfile:
        w = csv.writer(csvfile)
        csv_title = ["名称", "价格", "价格/米", "户型", "面积", "楼层", "建造日期", "代理人姓名", "地址", "评价"]
        w.writerow(csv_title)

        for house in house_list:
            temp = []

            # name = house.find('b', class_="strongbox").text.strip()

            # <div class="house-details">
            # <div class="house-title">
            #                                         <a data-from="" data-company="" title="楚天旁华泰学 区房 华泰丽晶 毛坯三房 南北通透 谁时看房" href="https://tianmen.anjuke.com/prop/view/A1956326640?from=filter&amp;spread=commsearch_p&amp;uniqid=pc5e674c3ab31a09.15179881&amp;position=1&amp;kwtype=filter&amp;now_time=1583828026" target="_blank" class="houseListTitle">
            #     楚天旁华泰学 区房 华泰丽晶 毛坯三房 南北通透 谁时看房</a>网页分析
            name = house.find('div', class_="house-title").a.text.strip()



            # <span class="price-det"><strong>64</strong>万</span> 网页分析
            price = house.find('span', class_='price-det').text.strip()

            # <span class="unit-price">5334元/m²</span>
            price_area = house.find('span', class_='unit-price').text.strip()

            # <div class="details-item">
            #   <span>3室2厅</span> 
                    # <em class="spe-lines">|</em>
            #   <span>120m²</span> 
                    # <em class="spe-lines">|</em>
            # <span>低层(共31层)</span>
                     # <em class="spe-lines">|</em>
            # <span>2018年建造</span>
            # </div>
            no_room = house.find('div', class_='details-item').span.text
            area = house.find('div', class_='details-item').contents[3].text
            floor = house.find('div', class_='details-item').contents[5].text
            year = house.find('div', class_='details-item').contents[7].text

            # <span class="broker-name broker-text">吴宇田</span>
            broker = house.find('span', class_='broker-name broker-text').text
            # broker = broker[1:]

            # <span class="comm-address" title="百里太子湾&nbsp;&nbsp;竟陵-天门世贸中心-广沟路">
            #         百里太子湾&nbsp;&nbsp;
            #         竟陵-天门世贸中心-广沟路                </span>
            address = house.find('span', class_='comm-address').text.strip()
            address = address.replace('\xa0\xa0\n                  ', ' ')

            # <div class="tags-bottom">
            # <span class="item-tags tag-others">环境优美</span>
            # <span class="item-tags tag-others">南北通透</span>
            # <span class="item-tags tag-others">品质小区</span></div>
            tag_list = house.find_all('span', class_='item-tags tag-others')
            tags = [i.text for i in tag_list]

            temp = [name, price, price_area, no_room, area,
                    floor, year, broker, address, tags]
            print(temp)
            
            # temp = [name]
            # print(temp)

            time.sleep(0.3)
            # 写入表格（test.csv）
            w.writerow(temp)




