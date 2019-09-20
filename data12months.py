# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 11:22:10 2019

@author: heyiming
"""

import pandas as pd
from matplotlib import pyplot as plt

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']

path=r'D:\何一鸣新东方在线\业务处理\2018'
class Dataana(object):
    def __init__(self):
        print('start')

    
#    def getnum(self,start,end):
    def getnum(self,datas):
        num=[]
        zonedata=[]
#        for i in range(start,end):
        for i in datas:
            file=r'{}\{}.xls'.format(path,i)
#            print(file)
            
            df=pd.read_excel(file)
            
            
            adloc=[]
            sales=[]
            for ad in df.推广位:
                adloc.append(ad)
            for sale in df.点击次数:
                sales.append(sale)
            numzone=[]
            for salesdata in zip(adloc,sales):
                if '中考' in str(salesdata[0]) and int(salesdata[1])>0:
                    num.append(salesdata[1])
                    numzone.append(salesdata[1])
#                    print(salesdata)
            print(sum(numzone))
            zonedata.append(sum(numzone))

#            file2=r'{}\2019-{}detail.xlsx'.format(path,i)
#            print(file2)
#            df2=pd.read_excel(file2)
#            adcopy=[]
#            product=[]
#            for ads in df2.推广位:
#                adcopy.append(ads)
#            for pro in df2.产品:
#                product.append(pro)
#            for productdata in zip(adcopy,product):
#                if '微信' in str(productdata[0]):
#                    print('ok')
#        print(int(sum(num)))
        self.drawpic(dates,zonedata)
    def drawpic(self,dates,zonedata):
        plt.figure(figsize=(15,5))
        plt.bar(dates,zonedata)
        plt.xlabel('Date')
        plt.ylabel('Datas')
        plt.title('近12个月数据变动')
        for x,y in zip(dates,zonedata):
            plt.text(x,y,str(y),va='top',ha='center',fontsize='15',color='w')
        plt.show()
dates=['2018-9','2018-10','2018-11','2018-12','2019-1','2019-2','2019-3','2019-4','2019-5','2019-6','2019-7','2019-8']
if __name__=='__main__':
    data2018=Dataana()
    data2018.getnum(dates)