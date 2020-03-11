
输入 python -m http.server 3000 打开服务器，
出现如下信息：
Serving HTTP on 0.0.0.0 port 3000 (http://0.0.0.0:3000/) ...

浏览器访问 http://localhost:3000 查看效果。

参考https://lbs.amap.com/api/javascript-api/example/geocoder/regeocoding
center: [113.086094,30.511914],   天门第二医院坐标


index.html  ---定位为武汉积玉桥坐标
index_tm.html  --定位为天门坐标
index_backup.html  --实验楼作者范本


anjukespider.py ---安居客爬虫
beikespider-crawl.py --贝壳网武汉积玉桥房源爬虫，用于地图上的信息
beikespider-whjyqiao.py --贝壳网武汉积玉桥房源爬虫
crawl.py---实验楼作者范本


sample.csv ---实验楼作者范本保存的数据
info.csv ---beikespider-crawl.py保存的信息
贝壳二手房源信息.csv --beikespider-whjyqiao.py保存的信息
贝壳武汉积玉桥二手房源.xlsx --用Excel数据导入csv信息保存的表格文件


房源统计.mpx--minitab做的房源信息分析


