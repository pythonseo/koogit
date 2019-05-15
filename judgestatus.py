from selenium import webdriver
from urllib import request
import re
import time
import json
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://library.koolearn.com/")
driver.maximize_window()
#1.执行javascript代码，删除target属性
#2.点击删除target属性后的登录连接
#3.输入用户名、密码等信息，执行登录操作
driver.find_element_by_name('userName').send_keys('0000')
driver.find_element_by_name('password').send_keys('123456')
driver.find_element_by_id('jp-login-btn').click()
time.sleep(3)

#获取cookies
text=driver.page_source
cookie = driver.get_cookies()

jsonCookies = json.dumps(cookie)
with open('videopage.json', 'w') as f:
    f.write(jsonCookies)
str=''
with open('videopage.json','r',encoding='utf-8') as f:
    listCookies=json.loads(f.read())
cookie = [item["name"] + "=" + item["value"] for item in listCookies]
cookiestr = '; '.join(item for item in cookie)
#构建链接库
urlku=[]
for page in range(0,32):
    urlpage='http://library.koolearn.com/course/index?oneCategoryId=3339&subCategoryId=0&productType=2&pageNo={}'.format(page)
    urlku.append(urlpage)
for page in range(0,15):
    urlpage='http://library.koolearn.com/course/index?oneCategoryId=3335&subCategoryId=0&productType=2&pageNo={}'.format(page)
    urlku.append(urlpage)
for page in range(0,13):
    urlpage='http://library.koolearn.com/course/index?oneCategoryId=3357&subCategoryId=0&productType=2&pageNo={}'.format(page)
    urlku.append(urlpage)
for page in range(0,15):
    urlpage='http://library.koolearn.com/course/index?oneCategoryId=3365&subCategoryId=0&productType=2&pageNo={}'.format(page)
    urlku.append(urlpage)
for page in range(0,8):
    urlpage='http://library.koolearn.com/course/index?oneCategoryId=3370&subCategoryId=0&productType=2&pageNo={}'.format(page)
    urlku.append(urlpage)
for page in range(0,2):
    urlpage='http://library.koolearn.com/course/index?oneCategoryId=3376&subCategoryId=0&productType=2&pageNo={}'.format(page)
    urlku.append(urlpage)
for page in range(0,1):
    urlpage='http://library.koolearn.com/course/index?oneCategoryId=3378&subCategoryId=0&productType=2&pageNo={}'.format(page)
    urlku.append(urlpage)
for page in range(1):
    urlpage='http://library.koolearn.com/course/index?oneCategoryId=3380&subCategoryId=0&productType=2&pageNo={}'.format(page)
    urlku.append(urlpage)
#检测播放
for url in urlku:
    head={
        'cookie':cookiestr,
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }
    req = request.Request(url, headers=head)
    html=request.urlopen(req).read()
    html=html.decode('utf-8')
    keurl=[]
    title=re.compile(r'<a class="p-im-bd" href="/course/detail/(.+?)/',re.DOTALL)
    for gettitle in title.findall(html):
            curl='http://library.koolearn.com/lecture/{}/0'.format(gettitle)
            keurl.append(curl)
    video=re.compile(r'//视频播放地址.+?url:"(.+?)",',re.DOTALL)
    time.sleep(3)
    for kec in keurl:
        req1 = request.Request(kec, headers=head)
        html1=request.urlopen(req1).read()
        html1=html1.decode('utf-8')
        for kecheck in video.findall(html1):
            if kecheck=='':
                print("{}无法播放".format(kec))
            else:
                print("{}正常播放'\n'{}".format(kec,kecheck))

