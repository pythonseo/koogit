import requests
from bs4 import BeautifulSoup
import time

#存储URL
def store(ul):
    with open('anhuiksy.txt','a',encoding="utf-8") as f:
        f.write(ul+'\n')
        print('store sucess')
#推送到内部接口
def push(title,url):
    api='http://cmsapp.koolearn.com/collection.php'
    data={
        'content':"海琨，请访问网址获取内容。",
        'title':title,
        'siteid':'5',
        'nodeid':'229',
        'url':url,
        'time':time.time(),
        'keywords':"安徽"
        }
    reponse=requests.post(api,data=data)
    print(reponse.content)
#获取标题
def getcon(link):
    try:
        conhtml=requests.get(link)
        conhtml.encoding='gb18030'
        soupcon=BeautifulSoup(conhtml.text,'lxml')
        contitle=soupcon.head.title.text
        print(contitle)
        push(contitle,link)
    except Exception as e:
        print(e)

#已经存在的URL
ahksyurl=[]
with open('anhuiksy.txt','r',encoding="utf-8") as fu:
    for urlexist in fu:
        urlexist=urlexist.strip('\n')
        ahksyurl.append(urlexist)
#获取新闻URL并判断
response=requests.get('https://www.ahzsks.cn/ptgxzs/')
print(response.status_code)
if int(response.status_code)==200:
    soup=BeautifulSoup(response.text,'lxml')
    x=soup.select('body .sylm ul a')
    for u in x:
        if '..' in u['href']:
            link=u['href'].replace('..','https://www.ahzsks.cn')
            print('get url:{}'.format(link))
            if link in ahksyurl:
                print(link+'exist')
            else:
                store(link)
                getcon(link)
        else:
            link='https://www.ahzsks.cn/ptgxzs/'+u['href']
            print('get url:{}'.format(link))
            if link in ahksyurl:
                print(link+'exist')
            else:
                store(link)
                getcon(link)
        
        
        
    

