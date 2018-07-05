# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import re
from pip._vendor.distlib.compat import raw_input
 
adr =[]
 
''''对搜素资源名字进行url编码'''
search_text = input('请输入搜索资源名：')
#search_text = raw_input('请输入搜索资源名：')
#search_text = search_text.decode('gbk')
#search_text = search_text.encode('utf-8')
print(search_text)
search_text = urllib.request.quote(search_text)
 
 
''''获取文件地址'''
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
url = ('http://www.panduoduo.net/s/name/'+search_text)
print(url)
req=urllib.request.Request(url=url,headers=headers) 
home = urllib.request.urlopen(req).read()
#home = urllib.request.urlopen(url)
 
 
'''获取百度云地址'''
def getbaidu(adr):
  print(adr)
  for i in adr:
    urlt = 'http://www.panduoduo.net'+i
    requrl =urllib.request.Request(url=urlt,headers=headers) 
    url = urllib.request.urlopen(requrl).read()
    bs = BeautifulSoup(url)
    bs1 = bs.select('.dbutton2')
    href = re.compile('http\%(\%|\d|\w|\/\/|\/|\.)*')
    b = href.search(str(bs1))
    name = str(bs.select('.center'))#.decode('utf-8')
    text1 = re.compile('\<h1\sclass\=\"center"\>[\d|\w|\D|\W]*\</h1\>')
    text2 = text1.search(name)
    rag1 = re.compile('\>[\d|\w|\D|\W]*\<')
    if text2:
      text3 = rag1.search(text2.group())
      if text3:
        print (text3.group())
    if b:
      text = urllib.unquote(str(b.group())).decode('utf-8')
      print (text)
 
'''初始化'''
def init(adr):
  soup = BeautifulSoup(home,"lxml")
  print(soup.p.string)
  soup = soup.select('.row')
  pattern = re.compile('\/r\/\d+')
  for i in soup:
    i = str(i)
    adress = pattern.search(i)
    adress = adress.group()
    adr.append(adress)
 
 
print ('running---------')   
init(adr)
print ('running++++++---------')   
getbaidu(adr)
print ('running******---------')   

