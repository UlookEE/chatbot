import requests
from fake_useragent import UserAgent

def write_file(fileName, content):
    file = open(fileName, 'w+')
    for c in content:
        file.write(str(c))
ua = UserAgent()
header = {'user-agent': ua.chrome}
page = requests.get('https://www.google.com', headers=header)
write_file('intro_to_soup_html.html', page)

print(page.content)

# Result : google.com html file...
