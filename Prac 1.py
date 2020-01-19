from bs4 import BeautifulSoup
import requests
import re
from fake_useragent import UserAgent

ua = UserAgent()
header = {'user-agent': ua.chrome}
url = "https://www.consumerreports.org/cro/a-to-z-index/products/index.htm"
data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')

products = soup.find_all('a', attrs={'class':"products-a-z__results__item"})
for p in products:
    print(p.text.strip('\n').ljust(30), p['href'])