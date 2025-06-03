import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.in/'
web_data = requests.get(url)
soup = BeautifulSoup(web_data.content,'html.parser')
print(soup.p)
print(soup.title)
print(soup.h1)
print(soup.h2)
print(soup.a)
print(soup.h1.string)
print(soup.body.prettify()) # arrange a systematic format
print(soup.p.string)  # comment find
print(soup.find('h1')) # first tag
print(soup.findAll('h1')) # all tags