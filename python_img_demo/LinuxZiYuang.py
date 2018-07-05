#coding=utf-8
import re
import requests
from tenacity import retry, stop_after_attempt
 
@retry(stop=stop_after_attempt(3))
def get_html(url):
    '''获取页面源代码'''
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
    page = requests.get(url,headers = headers)
    html = page.text
    return html
 
def get_real_url(url,reg):
    '''获取真实的页面地址'''
    mainurl = 'http://linux.linuxidc.com/'
    html = get_html(url)
    items = re.findall(reg,html)
    for item in items:
        realurl = '{}{}'.format(mainurl,item)
        yield realurl
 
def get_year_url():
    '''获取**年的页面地址'''
    url = 'http://linux.linuxidc.com/index.php'
    reg = re.compile(r'href="(.*?)">\d+年资料')
    year_urls = get_real_url(url,reg)
    for year_url in year_urls:
        yield year_url
 
def get_month_url():
    '''获取**月的页面地址'''
    reg = re.compile(r'href="(.*?)">\d+月')
    year_urls = get_year_url()
    for year_url in year_urls:
        month_urls =  get_real_url(year_url,reg)
        for month_url in month_urls:
            yield month_url
 
def get_day_url():
    '''获取**日的页面地址'''
    reg = re.compile(r'href="(.*?)">\d+日')
    month_urls = get_month_url()
    for month_url in month_urls:
        day_urls =  get_real_url(month_url,reg)
        for day_url in day_urls:
            yield day_url
 
def get_books_urls(urls):
    '''获取资料名称及下载页'''
    for url in urls:
        reg = re.compile(r'href="(index.*?)">(.*?)</a></div></td><td width="100">')
        html = get_html(url)
        items = re.findall(reg,html)
        for item in items:
            yield item
 
def get_other_url(url):
    '''获取其他链接的资料'''
    print()
    reg = re.compile(r'href="(index.*?)">.*?</a></div></td><td width="100">')
    all_urls = get_real_url(url,reg)
    for all_url in all_urls:
        yield all_url
            
def print_book_url(book,book_url):
    '''打印可下载的书籍及链接'''
    url = 'http://linux.linuxidc.com/'
    book = book.lower()
    item = book_url
    if len(item) == 2:
        bookname = item[1].lower()
        if book in bookname:
            print ('\n'+ item[1])
            print ("资料下载链接:")
            dlurl = '{}{}'.format(url,item[0])
            reg = re.compile(r'href="(linuxconf/download.php.*?)">.*?</a></div></td><td width="100">')
            download_urls = get_real_url(dlurl,reg)
            for download_url in download_urls:
                print (download_url)
 
def get_download_url(book):
    url_2011 = 'http://linux.linuxidc.com/index.php?folder=MjAxMcTq18rBzw=='
    # print(book)
    all_urls = get_other_url(url_2011)
    books_urls = get_books_urls(all_urls)
    for book_url in books_urls:
        print_book_url (book,book_url)
    day_urls = get_day_url()
    books_urls = get_books_urls(day_urls)
    for book_url in books_urls:
        print_book_url (book,book_url)
 
if __name__=='__main__':
    #book = input ("请输入资料名称:")
    book = "freemind"
    print(book)
    get_download_url(book)