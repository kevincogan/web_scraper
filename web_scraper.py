from bs4 import BeautifulSoup
import requests

#Gets the source code from the desired website and adds it to a file
r = requests.get('https://coreyms.com/')
with open('website.txt', 'wb') as target:
    target.write(r.content)

with open('website.txt', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

#Parses the video link from the website
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)
    #print()

    body_text = article.find('div', class_='entry-content')
    print(body_text.p.text)
    #print()

    try:
        youtube_link = article.find('iframe', class_='youtube-player')['src']
        parse = youtube_link.split('/')[4].split('?')[0]
        link = f'https://youtube.com/watch?v={parse}'

    except Exception as e:
        link = ''

    print(link)

    print()



#print(soup.prettify())
