from bs4 import BeautifulSoup
import re

def read_file(fileName):
    file = open(fileName)
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file('intro_to_soup_html.html'), 'lxml')
body = soup.body

a_tags = soup.find_all('a')
print(a_tags)

attrs = {'class' : "gb_Kd"}
first_a = soup.find_all('a', attrs=attrs)
print(first_a)
regex = re.compile('Google')
print(regex)

title = soup.find_all(string= regex)
print(title)

