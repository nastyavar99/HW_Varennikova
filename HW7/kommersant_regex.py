import requests as req
import re
from bs4 import BeautifulSoup

request = req.get('https://www.kommersant.ru/archive/rubric/4/month/2020-10-01')
soup = BeautifulSoup(request.content, features='html.parser')
titles = []

for tag in soup.find_all('h3', class_='article_name'):
    covid_title = re.findall(r'корона\w+|COVID', tag.text, re.IGNORECASE)
    if covid_title:
        titles.append(tag.text)

print(titles)
