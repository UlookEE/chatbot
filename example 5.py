from bs4 import BeautifulSoup


def read_file(fileName):
    file = open(fileName)
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file('intro_to_soup_html.html'), 'lxml')
meta = soup.meta
print(meta)
print(meta.get('charset'))

body = soup.body
print(body)