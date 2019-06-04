
import requests
import re
import pandas as pd
##starturl='https://pinyin.sogou.com/dict/cate/index/1'
##def getdalei():
##    reponse1=requests.get(starturl)
##    url1=re.compile(r'''<div class='cate_no_child no_select'>.+?<a href="(.+?)">(.+?)<span class="cate_num_font">''',re.DOTALL)
##    for urllist1 in url1.findall(reponse1.text):
##        print(urllist1)
##getdalei()
urllist='https://pinyin.sogou.com/dict/cate/index/3'
#获取词表链接
def getwordlist(x):
    reponse2=requests.get(x)
    getwurl=re.findall('''<div class="detail_title"><a href='(.*?)'>(.*?)</a></div>''',reponse2.text,re.S)
    for u1 in getwurl:
        for u2 in u1:
            if 'dict' in u2:
                realu=u2.replace('detail/index','dialog/word_list')
                realus='https://pinyin.sogou.com'+realu
                pageid=re.findall('\d\d\d\d\d',realus)
                print(pageid)
                getword(realus,pageid)
#获取词表
def getword(w,p):
    try:
        rp=requests.get(w)
        rp.encoding='utf-8'
        tb = pd.read_html(rp.text)[1]
        print(tb)
        filename=p[0]+'.csv'
        tb.to_csv(filename,encoding='utf_8_sig')
    except Exception as e:
        pass
        print(w,p,e)
#遍历分页
p=1
while(p<5):
        pageurl=urllist+'/default/%s'%(p)
        print(pageurl)
        getwordlist(pageurl)
        deurl=getwordlist(pageurl)
        print(deurl)
        p+=1
        if deurl==[]:
            break
