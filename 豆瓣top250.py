# 使用者：姜海波
# 创建时间：2021/10/23  22:12
#拿到页面源代码,--->requests
#通过re来提取想要的有效信息---->re
import requests
import re
import csv
for page in range(0,250,25):
    url='https://movie.douban.com/top250?start={}&filter='.format(page)
    head={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50"
    }
    pargam={'start': 50}
    resp=requests.get(url,headers=head)
    #print(resp.text)
    page_content=resp.text

    #解析数据
    #参数越多匹配越精准
    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
                     r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>',re.S)
    result=obj.finditer(page_content)
    f=open("data.csv",mode="a",newline="",encoding='utf-8')     #碰到文件有空行的,加入参数newline=""
    csvwriter=csv.writer(f)         #在csvwriter中写入等于直接在文件流中写入
    for it in result:
        '''print(it.group("name"))
        print(it.group("year").strip())     #.strip为了去掉换行和空格
        print(it.group("score"))'''
        dic=it.groupdict()          #所得到的放入字典
        dic['year']=dic['year'].strip()             #同上
        csvwriter.writerow(dic.values())        #将字典中的值写入

f.close()
print('over')



resp.close()
