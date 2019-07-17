# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:07:07 2019

@author: heyiming
"""


import pandas as pd
import numpy as np
import time
import requests
def artpost(T,C,U):
    api='http://cmsapp.koolearn.com/collection.php'
    data={
          'content':C,
          'title':T,
          'siteid':'5',
          'nodeid':'303',
          'url':U,
          'time':'2020-07-04 18:06:10',
          'copyfrom':'大学招生网',
          'keywords':"大学"
            }
    time.sleep(1)
    push=requests.post(api,data=data)
    print(push.content)
df=pd.read_excel(r'D:\何一鸣新东方在线\其他\coll.xls')
gr=df.groupby('学校名称')
for i in gr:
    name=i[0]
    name=name.replace('(一流大学建设高校)','')
    name=name.replace('（省重点建设高校）','')
    name=name.replace('(一流学科建设高校)','')
    name=name.replace('（入选“2011计划”高校）','')
    name=name.replace('（独立学院）','')
    name=name.replace('（公办收费）','')
    titlepre='%s2019浙江平行投档（一段）分数线'%(i[0])
    title='%s2019浙江平行投档（一段）分数线'%(name)
    print(title)
    sub=list(i[1].专业名称)
    score=list(i[1].分数线)
    conpre=zip(sub,score)
    conlist=[]
    for x in conpre:
        tr='<tr><td>%s</td><td>%s</td></tr>'%(x[0],x[1])
        conlist.append(tr)
    tabletr=''.join(conlist)
    con='''<p>
    　　{}录取分数线陆续公布，新东方在线高考网整理了{}，供同学们参考。<br/>
</p>
<table width="100%" align="center">
    <colgroup>
        <col width="125" span="2" style="width: 125px;"/>
    </colgroup>
    <tbody>
        <tr text-align="center" height="18" style="height: 18px;">
            <td colspan="2" width="100%" height="18" align="center">
                <a href="https://news.koolearn.com/20190622/1180218.html" target="_blank"><strong>2019高考录取分数线汇总</strong></a>
            </td>
        </tr>
        <tr height="18" style="height: 18px;">
            <td height="18" style="border-top: medium none;">
                <a href="https://news.koolearn.com/20190621/1180112.html" target="_blank">本科</a>
            </td>
            <td style="border-top: none; border-left: none;">
                <a href="https://news.koolearn.com/20190621/1180107.html" target="_blank">专科</a>
            </td>
        </tr>
        <tr height="18" style="height: 18px;">
            <td height="18" style="border-top: medium none;">
                <a href="https://news.koolearn.com/20190709/1182199.html" target="_blank" title="" _href="https://news.koolearn.com/20190709/1182199.html" textvalue="31省市投档分数线">31省市投档分数线</a>
            </td>
            <td style="border-top: none; border-left: none;">
                <a href="https://news.koolearn.com/20190710/1182344.html" target="_blank" title="" _href="https://news.koolearn.com/20190710/1182344.html">大学投档线</a>
            </td>
        </tr>
    </tbody>
</table>
<table width="100%" align="center">
    <colgroup>
        <col width="125" span="2" style="width: 125px;"/>
    </colgroup>
    <tbody>
        <tr text-align="center" height="18" style="height: 18px;">
            <td colspan="2" width="100%" height="18" align="center">
                <strong>{}</strong>
            </td>
        </tr>
        {}
    </tbody>
</table>
<p>
    <strong><span style="font-size: 18px;">　　</span></strong><strong>推荐阅读：</strong><br/>
</p>
<p style="white-space: normal; text-align: center;">
    <a href="https://gaokao.koolearn.com/zhaosheng/" target="_blank" title="" _href="https://gaokao.koolearn.com/zhaosheng/"><img src="https://file.koolearn.com/20190513/15577200685114.jpg" _src="https://file.koolearn.com/20190513/15577200685114.jpg" title="2019年高考招生简章"/></a>
</p>
<p style="white-space: normal;">
    <strong style="text-align: center;"><span style="font-size: 18px;">　　</span></strong><a href="https://gaokao.koolearn.com/college/" target="_blank" title="" _href="https://gaokao.koolearn.com/college/" textvalue="高考院校库"><strong><span style="font-size: 18px;">高考院校库</span></strong></a><strong><span style="font-size: 18px;">&nbsp;<a href="https://gaokao.koolearn.com/zhuanye/" target="_blank" title="" _href="https://gaokao.koolearn.com/zhuanye/">大学专业解读</a>&nbsp;<a href="http://gaokao.koolearn.com/zt/pici/" target="_blank" title="" _href="http://gaokao.koolearn.com/zt/pici/">高考录取批次</a></span></strong>
</p>
<p style="white-space: normal;">
    <strong style="text-align: center;"><span style="font-size: 18px;">　　<strong>新东方在线推出了<strong><a href="http://un.koolearn.com/alliance/clickword?userid=ff80808138fed9e801390002fcd60001&amp;kid=ff80808154542a57015456f152a06279&amp;url=http://gaokao.koolearn.com/zhuanti/zycp/" target="_blank"><span style="color: rgb(255, 0, 0);">48道题测出最适合你报考的大学专业</span></a></strong>&nbsp;参考适合你填报的大学专业。<strong>&nbsp;</strong><strong><a href="http://un.koolearn.com/alliance/clickword?userid=ff80808138fed9e801390002fcd60001&amp;kid=ff8080815c31c8da015c331edb881f45&amp;url=http://gaokao.koolearn.com/zhuanti/gfxdx/" target="_blank"><span style="color: rgb(255, 0, 0);">估分选大学</span></a></strong>，通过大数据，选出适合你报考的大学。</strong></span></strong>
</p>
<p style="white-space: normal;">
    <strong><span style="font-size: 18px;">　　</span></strong><strong><span style="font-size: 18px; text-decoration-line: underline;">解析部分</span></strong>
</p>
<p style="white-space: normal;">
    <span style="font-size: 18px; color: rgb(255, 0, 0); text-decoration-line: underline;"></span>
</p>
<p style="white-space: normal;">
    <span style="color: rgb(12, 12, 12);"><strong>　　【试卷解析】</strong></span><span style="color: rgb(255, 0, 0);"><strong>【</strong></span><strong style="color: rgb(255, 0, 0);"><a href="https://news.koolearn.com/20190607/1178130.html" target="_blank" style="color: rgb(255, 0, 0);">视频版</a>】&nbsp; &nbsp;<strong><a href="https://news.koolearn.com/20190607/1178067.html" target="_blank" style="color: rgb(255, 0, 0);">【文字版</a>】</strong></strong>
</p>
<p style="white-space: normal;">
    <span style="color: rgb(12, 12, 12);"><strong>　　【各科解析】</strong></span><strong style="color: rgb(255, 0, 0);">&nbsp;&nbsp;<strong><a href="https://news.koolearn.com/20190607/1178069.html" target="_blank" style="color: rgb(255, 0, 0);">语文</a>&nbsp; &nbsp;<strong><a href="https://news.koolearn.com/20190608/1178271.html" target="_blank" style="color: rgb(255, 0, 0);">数学</a>&nbsp; &nbsp;<strong><a href="https://news.koolearn.com/20190608/1178384.html" target="_blank" style="color: rgb(255, 0, 0);">理综</a>&nbsp;&nbsp;<strong><a href="https://news.koolearn.com/20190608/1178461.html" target="_blank" style="color: rgb(255, 0, 0);">文综</a>&nbsp;&nbsp;<strong><a href="https://news.koolearn.com/20190608/1178588.html" target="_blank" style="color: rgb(255, 0, 0);">英语</a></strong></strong></strong></strong></strong></strong><br/>
</p>
<p style="white-space: normal;">
    <strong style="color: rgb(255, 0, 0);"><strong><strong><strong><strong><strong style="color: rgb(12, 12, 12);">　　【各省市解析】<a href="https://news.koolearn.com/20190609/1178931.html" target="_blank" style="text-align: center; color: rgb(255, 0, 0);">全国卷一</a><span style="color: rgb(255, 0, 0);">&nbsp;</span><a href="https://news.koolearn.com/20190609/1178932.html" target="_blank" style="text-align: center; color: rgb(255, 0, 0);">全国卷二</a><span style="color: rgb(255, 0, 0);">&nbsp;</span><a href="https://news.koolearn.com/20190609/1178933.html" target="_blank" style="text-align: center; color: rgb(255, 0, 0);">全国卷三</a><span style="color: rgb(255, 0, 0);">&nbsp;</span><a href="https://news.koolearn.com/20190609/1178937.html" target="_blank" style="text-align: center; color: rgb(255, 0, 0);">北京</a><span style="color: rgb(255, 0, 0);">&nbsp;</span><a href="https://news.koolearn.com/20190609/1178935.html" target="_blank" style="text-align: center; color: rgb(255, 0, 0);">上海</a><span style="color: rgb(255, 0, 0);">&nbsp;</span><a href="https://news.koolearn.com/20190609/1178934.html" target="_blank" style="text-align: center; color: rgb(255, 0, 0);">浙江</a><span style="color: rgb(255, 0, 0);">&nbsp;</span><span style="text-align: center; color: rgb(255, 0, 0); text-decoration-line: underline;"><a href="https://news.koolearn.com/20190609/1178936.html" target="_blank" style="color: rgb(255, 0, 0);">江苏</a>&nbsp;</span></strong></strong></strong></strong></strong></strong>
</p>
<p style="white-space: normal;">
    <span style="color: rgb(12, 12, 12);"><strong>　　【解析】</strong></span><span style="text-decoration-line: underline; color: rgb(255, 0, 0);"><strong><a href="https://news.koolearn.com/20190608/1178255.html" target="_blank" style="color: rgb(255, 0, 0);">2019高考试题试卷及解析汇总</a></strong></span>
</p>
<p style="white-space: normal;">
    <strong><strong><span style="font-size: 18px;">　　</span></strong></strong><strong><strong><span style="font-size: 18px; text-decoration-line: underline;">真题部分</span></strong></strong>
</p>
<p style="white-space: normal;">
    <strong>　　【作文】</strong><a href="https://news.koolearn.com/20190607/1178064.html" style="color: rgb(255, 0, 0);"><strong>全国各地2019高考作文题汇总</strong></a>
</p>
<p style="white-space: normal;">
    <strong>　　【真题】</strong><strong style="color: rgb(255, 0, 0); text-decoration-line: underline;"><a href="https://news.koolearn.com/20190608/1178825.html" target="_blank" style="color: rgb(255, 0, 0);">2019高考试题及参考答案汇总</a></strong>
</p>
<p style="white-space: normal; text-align: center;">
    <strong><img src="http://file.koolearn.com/20180614/15289465661549.png" _src="http://file.koolearn.com/20180614/15289465661549.png" title="高考分数线"/></strong>
</p>
<p style="white-space: normal; text-align: center;">
    <strong>点击查看&gt;&gt;<a href="http://gaokao.koolearn.com/zhuanti/fenshuxian/" target="_blank" title="" _href="http://gaokao.koolearn.com/zhuanti/fenshuxian/">历年高考分数线</a></strong>
</p>
<p style="white-space: normal;">
    　　以上就是<span style="white-space: normal;">{}，</span>新东方在线小编整理了<a href="https://gaokao.koolearn.com/zhuanti/lnzhenti/" target="_blank" title="" _href="https://gaokao.koolearn.com/zhuanti/lnzhenti/" textvalue="历年高考试题及答案"><strong>历年高考试题及答案</strong></a><strong><span style="color: rgb(255, 0, 0);">、</span></strong><a href="https://gaokao.koolearn.com/zhuanti/fenshuxian/" target="_blank" title="" _href="https://gaokao.koolearn.com/zhuanti/fenshuxian/" textvalue="高考分数线"><strong>高考分数线</strong></a><strong><span style="color: rgb(255, 0, 0);">、</span></strong><a href="https://gaokao.koolearn.com/zhuanti/gkzuowen/" target="_blank" title="" _href="https://gaokao.koolearn.com/zhuanti/gkzuowen/" textvalue="高考作文"><strong>高考作文</strong></a><strong><span style="color: rgb(255, 0, 0);">、</span></strong><a href="https://gaokao.koolearn.com/zhuanti/gkzwdq/" target="_blank" title="" _href="https://gaokao.koolearn.com/zhuanti/gkzwdq/" textvalue="高考满分作文"><strong>高考满分作文</strong></a><strong>、</strong><a href="http://gaokao.koolearn.com/zt/toudang/" target="_blank" title="" _href="http://gaokao.koolearn.com/zt/toudang/" textvalue="高考录取投档线"><strong>高考录取投档线</strong></a><strong>、<a href="https://gaokao.koolearn.com/zhuanti/cjfdb/" target="_blank" title="" _href="https://gaokao.koolearn.com/zhuanti/cjfdb/" textvalue="高考一分一段分段表"><span style="color: rgb(255, 0, 0);">高考一分一段分段表</span></a><span style="color: rgb(255, 0, 0);">，<a href="https://gaokao.koolearn.com/zhuanti/luqu/" target="_blank" title="" _href="https://gaokao.koolearn.com/zhuanti/luqu/" textvalue="高考录取查询入口"><strong>高考录取查询入口</strong></a><strong>，</strong></span></strong>供参考。
</p>
        
        '''.format(name,title,titlepre,tabletr,title)
    print(con)
    url='www.koolearn.com'
    artpost(title,con,url)


