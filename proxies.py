import requests
import random
import time
import sys

def timecount(fu):
    def counttime():
        fu()
        t=time.process_time()
        print(t)
    return counttime
@timecount
def run():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
    proxies =[
        {
        "https":"123.7.61.8:53281"
    },
        {
        "https":"219.234.5.128:3128"
    },
        {
        "https":"60.191.201.38:45461"
    }
        ]
    url='https://www.so.com/'
    response=requests.get(url, headers=headers,proxies=random.choice(proxies))
    status=response.status_code # 状态码
    print(status,proxies)
run()

