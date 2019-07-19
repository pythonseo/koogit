# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 11:26:04 2019

@author: heyiming
"""

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

path='D:\何一鸣新东方在线\业务处理\转化分析'
def getfile(file):
    df=pd.read_excel(file)
    adloc=[]
    sales=[]
    for ad in df.推广位:
        adloc.append(ad)
    for sale in df.总金额:
        sales.append(sale)
    saleline=zip(adloc,sales)
    name=[]
    totla=[]
    for x in saleline:
        if '小学' in str(x[0]):
            name.append(x[0])
            totla.append(x[1])
    return sum(totla)

num=[]
for fid in range(1,19):
    file=r'{}\7.{}.xls'.format(path,fid)
    print(file)
    num.append(getfile(file))
print(num)
dataid=['7.1','7.2','7.3','7.4','7.5','7.6','7.7','7.8','7.9','7.10','7.11','7.12','7.13','7.14','7.15','7.16','7.17','7.18']
plt.figure(figsize=(10,5))
plt.xlabel('Date')
plt.ylabel('sales')
plt.title('TOEFL')
plt.plot(dataid,num,color='r',marker='^', mec='g')
plt.axhline(y=0.0,c='g',ls='-.',lw=2)    
for a,b in zip(dataid,num):
    plt.text(a,b,(b),ha='center',va='bottom')
plt.show()
