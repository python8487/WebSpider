# 用户接口输入
# key = input("请输入需要翻译的文字：")
# !/usr/bin/env python
# _*_ coding:utf-8 _*_

# 根据url发生请求，获取服务器响应文件
# 将html内容写入到本地
# 处理每个页面的url


import urllib
# import urllib.request
from urllib import request
import re
import time
# 构造请求头信息
header = {
"User-Agent":"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"
}

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"



key = str(input("请输入要翻译的文字:"))


# post请求需要提交的数据
formdata = {
"i":key,
"from":"AUTO",
"to":"AUTO",
"smartresult":"dict",
"client":"fanyideskweb",
"salt":"15813339630907",
"sign":"8350813fc54ef4f4aa0c7d058218e078",
"ts":"1581333963090",
"bv":"901200199a98c590144a961dac532964",
"doctype":"json",
"version":"2.1",
"keyfrom":"fanyi.web",
"action":"FY_BY_REALTlME"
}

data = urllib.parse.urlencode(formdata).encode(encoding="utf-8")

req = request.Request(url,data=data,headers=header)

resp = request.urlopen(req).read().decode()

# 正则表达式，提取"tgt":"和"}]]中间的任意内容
pat = r'"tgt":"(.*?)"}]]'

result = re.findall(pat,resp)

print("有道翻译的信息："+result[0])
print("**************翻译结束***************")
time.sleep(10)