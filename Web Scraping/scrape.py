'''import requests
from requests_html import HTMLSession
session = HTMLSession()
r = session.get("https://www.imdb.com/title/tt1187043/")
print(r)'''
'''import requests
from requests_html import HTMLSession
session = HTMLSession()
r = session.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
listerlist = r.html.find('.lister-list',first=True)
#print(listerlist)
title = listerlist.find('.titleColumn')
rating = listerlist.find('.ratingColumn strong')
img = listerlist.find('.posterColumn a img')
for i in range(0,len(title)):
    print(title[i].text)
    print(rating[i].text)
    print(i.attrs['src'])
img = listerlist.find('.posterColumn a img')
for i in img:
    print(i.attrs['src'])'''
'''import requests
from requests_html import HTMLSession
session = HTMLSession()
r = session.get("https://www.imdb.com/movies-coming-soon/?ref_=nv_mv_cs")
listdetail = r.html.find(".list.detail",first=True)
title = listdetail.find('.overview-top h4 a')
for i in range(0,len(title)):
    print(title[i].text)'''
'''import requests
from requests_html import HTMLSession
session = HTMLSession()
r = session.get("https://www.imdb.com/title/tt1187043/?ref_=nv_sr_srsg_0")
titlebar = r.html.find(".titleBar",first=True)
title = titlebar.find('.title_wrapper h1')
ratingvalue = r.html.find(".ratingValue strong")
credits = r.html.find(".credit_summary_item")
cast = r.html.find(".cast_list td a")
for i in range(0,len(title)):
    print(title[i].text)
    print(ratingvalue[i].text)
    print(credits[i].text)
for d in range(0,len(cast)):    
    print(cast[d].text)'''
'''import requests
from requests_html import HTMLSession
session = HTMLSession()
r = session.get("https://www.imdb.com/movies-coming-soon/?ref_=nv_mv_cs")
listdetail = r.html.find(".list.detail",first=True)
title = listdetail.find(".overview-top")
for i in range(0,len(title)):
    print(title[i].text)
    print('no ratings')
    print()'''
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import csv
session = HTMLSession()
urls=[]
for i in range(1,51):
    urls.append(f'http://books.toscrape.com/catalogue/page-{i}.html')

csv_file = open('book.csv','w')
csv_writer = csv.writer(csv_file,lineterminator='\n')

csv_writer.writerow(['TITLE','PRICE','IMAGE URL'])
count = 1

for url in urls:
    source = session.get(url).html.html
    soup = BeautifulSoup(source,'lxml')
    box = soup.find('ol')
    elements = box.find_all('li')
    title = []
    picture = []
    cost = []
    for element in elements:
        name = element.select('h3 a')[0]['title']
        title.append(name)
        image = element.select('img')[0]['src']
        image_url = r'http://books.toscrape.com'+image
        picture.append(image_url)
        price = element.find('p', class_='price_color').text
        cost.append(price)
        csv_writer.writerow([name,price,image_url])
        print(count,end=" ")
        count+=1    

csv_file.close()