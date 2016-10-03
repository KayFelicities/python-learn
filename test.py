# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
 

url = 'http://www.zhihu.com/explore'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    #print content
    pattern = re.compile('<div class="explore-feed.*?>.*?<a class=".*?>(.*?)</a>.*?<a class="author-link.*?>(.*?)</a>.*?<div class="zh-summary.*?>(.*?)<a href="',re.S)    
    
    kay =  re.findall(pattern,content)
    for x in kay:
        print x[0], x[1], x[2]
    
    #items = re.findall(pattern,content)
    #for item in items:
    #    print item[0]
    #    haveImg = re.search("img",item[2])
    #    if not haveImg:
    #        print item[0],item[1],item[3]
except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason