# -*- coding:utf-8 -*-
import urllib.request
import re
from bs4 import BeautifulSoup

url = 'http://www.qiushibaike.com/hot/page/2/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

request = urllib.request.Request(url, headers = headers)
content = urllib.request.urlopen(request).read()
soup = BeautifulSoup(content, 'html.parser')

#test = soup.find_all(name = 'div', attrs = {'class':'content'})

pics = soup.select('div[class="author clearfix"]')

for pic in pics:
    pic_src = pic.find('img').get('src')
    pic_name = pic.find('img').get('alt') + '.jpg'
    urllib.request.urlretrieve(pic_src, pic_name)
    

