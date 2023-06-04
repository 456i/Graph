import requests
from bs4 import BeautifulSoup as bs

page = 0
url = 'https://acmp.ru/index.asp?main=tasks&str=%20&page=' + str(page) + '&id_type=0'

req = requests.get(url=url)
text = req.content.decode('cp1251')

soup = bs(text, 'html.parser')
ides = soup.find_all('tr', class_='white')


with open('data.txt', 'a', encoding='utf-8') as file:
    for i in ides:
        array = i.text
        string = str(array)
        # string = string.replace(' ', '')
        string = string.replace('\n', '')
        print(string)
        file.write(string)

# with open('data.html', 'a', encoding='utf-8') as file:
#     file.write(text)

with open('data.txt', 'r', encoding='utf-8') as file:
    source = file.read()
    source = source.replace('\n', '')
    print(source)
