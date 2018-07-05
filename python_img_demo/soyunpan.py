# -*- encoding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

def yunpan_search(key):
    url='http://www.wangpansou.cn/s.php?q='+key
    print(url)
    html=requests.get(url)
    print(html)
    soup=BeautifulSoup(html.text,"lxml")
    url_get=soup.find_all('a',{'class':'cse-search-result_content_item_top_a'})
    info_get=soup.find_all('div',{'class':'cse-search-result_content_item_mid'})
    f = open('baidu_source.txt','w')
    for i in range(len(url_get)):
        href=url_get[i]['href']
        title=''
        for c in url_get[i].children:
            title+=c.string.strip()

        information=''
        for info in info_get[i].children:
            information+=info.string.strip().replace('\n','')

        print (str(i+1)+'_'*60)
        print ('下载地址--'+href+'\n'+'链接标题--'+title+'\n'+'链接详情--'+information+'\n\n')
        f.write(str(i+1)+'. _____________________________________________________________________\n')
        f.write('下载地址--'+href+'\n'+'链接标题--'+title+'\n'+'链接详情--'+information+'\n\n')
    f.close()


if __name__=='__main__':
    #key=raw_input('please input what you want to look for:')
    key = 'vim'
    yunpan_search(key)
    print('finish')