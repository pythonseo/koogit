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
        if '号' not in str(x[0]):
            name.append(x[0])
            totla.append(int(x[1]))
    return sum(totla)

num=[]
dataid=[]
for fid in range(1,32):
    file=r'{}\7.{}.xls'.format(path,fid)
    print(file)
    num.append(getfile(file))
    dataid.append('{}'.format(fid))
print(num)
plt.figure(figsize=(10,5))
plt.xlabel('Date')
plt.ylabel('sales')
plt.title('TOEFL')
plt.plot(dataid,num,color='r',marker='^', mec='g')
plt.axhline(y=0.0,c='g',ls='-.',lw=2)    
for a,b in zip(dataid,num):
    plt.text(a,b,(b),ha='center',va='bottom')
plt.show()
