import os
def check(fun):
    with open('D:\何一鸣新东方在线\频道日常事务\高考\高考院校库\caiji\pro.txt','r',encoding="utf-8") as f:
        for i in f:
            i=i.strip('\n')
            i=i.split(',')
            if fun[1] == i[0]:
                print(fun,i[1])

with open('D:\何一鸣新东方在线\频道日常事务\高考\高考院校库\caiji\pro0.txt','r',encoding="utf-8") as k:
    for kw in k:
        kw=kw.strip('\n')
        kw=kw.split(',')
        check(kw)
