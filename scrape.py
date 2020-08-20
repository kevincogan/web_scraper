from bs4 import BeautifulSoup
import requests

#Gets the source code from the desired website and adds it to a file
r = requests.get('https://computing.dcu.ie/~humphrys/ca318/index.html')
with open('website.txt', 'wb') as target:
    target.write(r.content)

with open('website.txt', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

for headline in soup.find_all('h1'):
    print(headline.text)

#print(soup.prettify())
