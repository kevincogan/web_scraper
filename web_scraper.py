from bs4 import BeautifulSoup
import requests
import csv


#Gets the source code from the desired website and adds it to a file
r = requests.get('https://coreyms.com/')
with open('website.txt', 'wb') as target:
    target.write(r.content)

with open('website.txt', 'r') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

csv_file = open('website_data.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Header', 'Summary', 'Link'])

#Parses the video link from the website
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)

    body_text = article.find('div', class_='entry-content').p.text
    print(body_text)

    try:
        youtube_link = article.find('iframe', class_='youtube-player')['src']
        parse = youtube_link.split('/')[4].split('?')[0]
        link = f'https://youtube.com/watch?v={parse}'

    except Exception as e:
        link = ''

    print(link)

    print()

    csv_writer.writerow([headline, body_text, link])
csv_file.close()


#print(soup.prettify())
