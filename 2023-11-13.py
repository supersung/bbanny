from bs4 import BeautifulSoup as bs
import requests as rq

""" url = "https://table.cafe.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')
item = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > strong")


print(item)
print(item.get_text())

wt = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_detail > a > div > span.txt_name")
print(wt)
print(wt.get_text())


goods = res_html.select_one("#content_table > div.table_group > div:nth-child(3) > div.item_reply > div > button > strong")
print(goods)
print(goods.get_tet()) """

""" url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, "html.parser")

iss = res_html.select("a.wrap_thumb")
print(iss)

print("\n--------------\n")
ct = res_html.select('a.wrap_thumb')
for j in ct :
    c = j.attrs["data-tiara-id"]
    print(c+"\n") """
    
import os
from urllib.request import urlretrieve

url = "https://news.daum.net/"
res = rq.get(url)

hmltxt = res.text
res_html = bs(hmltxt, 'html.parser')


imgs = res_html.select("img")
print(imgs)



linkimgs = []

for i in imgs:
    irs = i.attrs["src"]
    print(irs + "\n")
    linkimgs.append(irs)
    
    
    

    