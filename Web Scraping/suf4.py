'''import bs4
from bs4 import BeautifulSoup
import requests
url = "https://www.google.com/search?q=google"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data,'lxml')
print(soup.prettify())'''
#PROGRAM TO GET THE TITLES USING REQUESTS
# import requests
# from requests_html import HTMLSession
# session = HTMLSession()
# r = session.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
# listerlist = r.html.find('.lister-list',first=True)
# #print(listerlist)
# title = listerlist.find('.titleColumn')
# print(title)
# for i in range(0,len(title)):
#     print(title[i].text)
#PROGRAM TO GET TITLE USING BS4
# import bs4
# import requests
# from bs4 import BeautifulSoup
# url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
# response = requests.get(url)
# data = response.text
# soup = BeautifulSoup(data,'lxml')
# #print(soup.prettify())
# title=soup.find_all(class_='titleColumn')
# for i in title:
#     print(i.get_text())
#PROGRAM TO GET THE URL OF ALL PAGES
# for i in range(1,51):
#     url = 'http://books.toscrape.com/catalogue/page-{}.html'.format(i)
#     print(url)
# PROGRAM TO GET HTML CODE OF ALL PAGES 
# import requests
# from bs4 import  BeautifulSoup
# for i in range(1,51):
#     url = 'http://books.toscrape.com/catalogue/page-'+str(i)+'.html'
#     response = requests.get(url)
#     data = response.text
#     soup = BeautifulSoup(data,'lxml')
#     print(soup.prettify())
#     print()
#     print()
#     print("****END OF"+str(i)+"****")
# PROGRAM TO GET THE HTML CODE OF GIVEN WEB PAGES 
import requests
from bs4 import  BeautifulSoup
x =int(input("enter the starting range"))
y =int(input("enter the ending range"))
for i in range(x,y+1):
    url = 'https://www.freepik.com/search?dates=any&format=search&page=1&query=wallpaper&sort=popular'+str(i)+'.html'
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data,'lxml')
    print(soup.prettify())
    print()
    print()
    print("****END OF"+str(i)+"****")