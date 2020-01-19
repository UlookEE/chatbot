from bs4 import BeautifulSoup


def read_file(fileName):
    file = open(fileName)
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file('intro_to_soup_html.html'), 'lxml')

title = soup.title
print(title.string)

title.string.replace_with("title has been changed")
print(title.string)