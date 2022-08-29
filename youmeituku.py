# 使用者：姜海波
# 创建时间：2022/8/29  15:45

import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
resp = requests.get(url)
resp.encoding = 'utf-8'
# head={
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47"
#     }
# print(resp.text)
main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div", class_="swiper-wrapper after").find_all("a")
# print(alist)

for a in alist:
    # print(a.get('href'))
    href="https://www.umei.cc"+a.get('href')
    # print(a.get('title'))
    # print(href)
    child_page_resp=requests.get(href)
    child_page_resp.encoding='utf-8'
    child_page_text=child_page_resp.text
    child_page=BeautifulSoup(child_page_text,"html.parser")
    p=child_page.find("section",class_="img-content")
    img=p.find("img")
    # print(img)
    """find返回值,fand_all返回数组,不可混用"""
    # print(img.get("src"))

    # 下载图片
    src=img.get("src")
    img_resp=requests.get(src)
    #img_resp.content这里是字节
    img_name=src.split("/")[-1]
    with open("image"+img_name,mode="wb") as f:
        f.write((img_resp.content))
    print("over",img_name)
    time.sleep(5)
f.close()



