# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup 
import lxml
import time

url='https://gaokao.koolearn.com/zhuanye/'
response=requests.get(url)
soup=BeautifulSoup(response.content,'lxml')
print(soup.select('.entry_tit')[0]['href'])
con='''
<p>
    　　新东方在线高考网整理了2019年中央司法警官学院招生面试、体检、体能测试名单（福建），供同学们参考。<br/>
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
                <a href="https://news.koolearn.com/20190622/1180193.html" target="_blank">体育类</a>
            </td>
            <td style="border-top: none; border-left: none;">
                <a href="https://news.koolearn.com/20190622/1180194.html" target="_blank">艺术类</a><br/><br/>
            </td>
        </tr>
    </tbody>
</table>
<p>
    &nbsp;&nbsp;
</p>
<p>
    <strong><span style="font-size: 18px;">　　</span></strong><strong>推荐阅读：</strong><br/>
</p>
<p style="white-space: normal; text-align: center;">
    <a href="https://gaokao.koolearn.com/zhaosheng/" target="_blank" title="" _href="https://gaokao.koolearn.com/zhaosheng/"><img src="https://file.koolearn.com/20190513/15577200685114.jpg" _src="https://file.koolearn.com/20190513/15577200685114.jpg" title="2019年高考招生简章"/></a>
</p>
<p style="white-space: normal;">
    <strong style="text-align: center;"><span style="font-size: 18px;">　　</span></strong><strong><span style="font-size: 18px;"><a href="https://gaokao.koolearn.com/zhiyuan/" target="_blank" title="" _href="https://gaokao.koolearn.com/zhiyuan/">高考志愿填报指南</a>&nbsp;<a href="https://gaokao.koolearn.com/zhuanye/" target="_blank" title="" _href="https://gaokao.koolearn.com/zhuanye/">大学专业解读</a>&nbsp;<a href="http://gaokao.koolearn.com/zt/pici/" target="_blank" title="" _href="http://gaokao.koolearn.com/zt/pici/">高考录取批次</a></span></strong>
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
    　　新东方在线小编整理了<a href="https://gaokao.koolearn.com/zhuanti/lnzhenti/" target="_blank" title="" _href="https://gaokao.koolearn.com/zhuanti/lnzhenti/" textvalue="历年高考试题及答案"><strong>历年高考试题及答案</strong></a><strong><span style="color: rgb(255, 0, 0);">、</span></strong><a href="https://gaokao.koolearn.com/zhuanti/fenshuxian/" target="_blank" title="" _href="https://gaokao.koolearn.com/zhuanti/fenshuxian/" textvalue="高考分数线"><strong>高考分数线</strong></a><strong><span style="color: rgb(255, 0, 0);">、</span></strong><a href="https://gaokao.koolearn.com/zhuanti/gkzuowen/" target="_blank" title="" _href="https://gaokao.koolearn.com/zhuanti/gkzuowen/" textvalue="高考作文"><strong>高考作文</strong></a><strong><span style="color: rgb(255, 0, 0);">、</span></strong><a href="https://gaokao.koolearn.com/zhuanti/gkzwdq/" target="_blank" title="" _href="https://gaokao.koolearn.com/zhuanti/gkzwdq/" textvalue="高考满分作文"><strong>高考满分作文</strong></a><strong>、</strong><a href="http://gaokao.koolearn.com/zt/toudang/" target="_blank" title="" _href="http://gaokao.koolearn.com/zt/toudang/" textvalue="高考录取投档线"><strong>高考录取投档线</strong></a><strong>、<a href="https://gaokao.koolearn.com/zhuanti/cjfdb/" target="_blank" title="" _href="https://gaokao.koolearn.com/zhuanti/cjfdb/" textvalue="高考一分一段分段表"><span style="color: rgb(255, 0, 0);">高考一分一段分段表</span></a><span style="color: rgb(255, 0, 0);">，<a href="https://gaokao.koolearn.com/zhuanti/luqu/" target="_blank" title="" _href="https://gaokao.koolearn.com/zhuanti/luqu/" textvalue="高考录取查询入口"><strong>高考录取查询入口</strong></a><strong>，</strong></span></strong>供参考。
</p>
<p>
    <br/>
</p>
'''
api='http://cmsapp.koolearn.com/collection.php'
data={
      'content':con,
      'title':'123',
      'siteid':'27',
      'nodeid':'321',
      'url':url,
      'time':2020-07-04 18:06:10,
      'keywords':"分数线"
        }
push=requests.post(api,data=data)
print(push.content)
