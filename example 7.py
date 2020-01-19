from bs4 import BeautifulSoup


def read_file(fileName):
    file = open(fileName)
    data = file.read()
    file.close()
    return data


soup = BeautifulSoup(read_file('intro_to_soup_html.html'), 'lxml')
body = soup.body
print(type(body.children))
for child in body.children:
    print(child if child is not None else '', end = '\n\n\n\n')

for index, child in enumerate(soup.body.descendants):
    print(index, '\t', child if child != '\n' else '\\n')
    print(child.parent.name)
    print(type(child.parent))
    print(child.next_sibling)
    print(child.previous_sibling)
    if index == 3:
        break
