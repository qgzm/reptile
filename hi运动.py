# 使用者：姜海波
# 创建时间：2022/8/13  20:56
import time

import requests
import re
import csv
for page in range(1,445,1):
    url='https://food.hiyd.com/list-6-html?page={}'.format(page)
    head={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47"
    }
    # pargam={'start': 50}
    resp=requests.get(url,headers=head)
    #print(resp.text)
    page_content=resp.text

    #解析数据
    #参数越多匹配越精准
    obj = re.compile(r'<div class="img-wrap">.*?<img src="(?P<urll>.*?)" alt="(?P<name>.*?)">.*?<p>热量：(?P<heat>.*?)</p>',re.S)
    result=obj.finditer(page_content)
    f=open("data44.csv",mode="a",newline="",encoding='utf-8')     #碰到文件有空行的,加入参数newline=""
    csvwriter=csv.writer(f)         #在csvwriter中写入等于直接在文件流中写入
    for it in result:
        '''print(it.group("name"))
        print(it.group("year").strip())     #.strip为了去掉换行和空格
        print(it.group("score"))'''
        dic=it.groupdict()          #所得到的放入字典
        # dic['urll']=dic['urll'].strip()             #同上
        csvwriter.writerow(dic.values())        #将字典中的值写入
    time.sleep(15)


f.close()
print('over')