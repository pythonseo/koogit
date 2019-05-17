import os
import os.path
from urllib import request

path='D:\\其他\\'


def alldict():
    with open(path+'dict2.txt',"r",encoding='utf-8') as f:
        for s in f:
            s=s.strip('\n')
            ss=s.split('\t')
            with open(path+'dictid.txt',"r",encoding='utf-8') as f0:
                for i in f0:
                    i=i.strip('\n\t')
                    i=i.split('	')
                    if i[0] == ss[2] and i[1]==ss[3]:
                        print(ss[0],ss[2],ss[3])
alldict()






