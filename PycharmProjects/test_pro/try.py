#coding:utf-8
#__author__ =='xuxu'
import unit
import requests
from config.config import header, host, logger

url =host + '/student/page/alumni/book'
header = header
payload = {"page":1,"pageSize":20,"openId":"o8kH70a0j3EoUNHBnIfw8OlUqmLI"}
r = requests.get(url = url,params = payload,timeout = 1)
print(r)
a = r.json()['data']['list'][0]['isHideInfo']
print(r.text)
print(a)
print(r.elapsed)