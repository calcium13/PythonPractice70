#coding:utf-8
'''
Created on 2018��9��11��

@author: zh
'''
import urllib
import urllib.request
import chardet
import ssl
import http.client
import re


ssl._create_default_https_context = ssl._create_unverified_context
url = "https://exchange.xforce.ibmcloud.com"
head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
        'Host': 'exchange.xforce.ibmcloud.com'
}
req=urllib.request.Request(url=url,headers=head) 
html=urllib.request.urlopen(req).read()
html = html.decode('utf-8')

print(html)

    