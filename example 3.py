from bs4 import BeautifulSoup


def read_file(fileName):
    file = open(fileName)
    data = file.read()
    file.close()
    return data


html_file = read_file('intro_to_soup_html.html')
soup = BeautifulSoup(html_file, 'lxml')
print(soup.prettify())

# Result : all html file...
