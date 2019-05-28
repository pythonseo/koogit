import requests
import os
with open('baidu.jpg','wb') as f:
    file=requests.get('https://www.baidu.com/img/bd_logo1.png')
    if str(file.status_code)=='200':
        f.write(file.content)
        print('下载成功,图片位于：%s'%(os.path.realpath(__file__)))
