import requests
import re
##starturl='https://pinyin.sogou.com/dict/cate/index/1'
##def getdalei():
##    reponse1=requests.get(starturl)
##    url1=re.compile(r'''<div class='cate_no_child no_select'>.+?<a href="(.+?)">(.+?)<span class="cate_num_font">''',re.DOTALL)
##    for urllist1 in url1.findall(reponse1.text):
##        print(urllist1)
##getdalei()
urllist='https://pinyin.sogou.com/dict/cate/index/3'
def getwordlist(x):
    reponse2=requests.get(x)
    getwurl=re.findall('''<div class="detail_title"><a href='(.*?)'>(.*?)</a></div>''',reponse2.text,re.S)
    return getwurl
getwordlist(urllist)
p=2
while(1):
        pageurl=urllist+'/default/%s'%(p)
        print(pageurl)
        getwordlist(pageurl)
        deurl=getwordlist(pageurl)
        print(deurl)
        p+=1
        if deurl==[]:
            break
