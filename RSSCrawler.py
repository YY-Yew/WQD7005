import requests
from bs4 import BeautifulSoup

url = "http://nexttrade.blogspot.com/feeds/posts/default"
resp = requests.get(url)
soup = BeautifulSoup( resp.content, features="xml")

updates = soup.findAll('entry')


import datetime
now = datetime.datetime.now()
filename = "nexttradefeed_%s-%s-%s.txt" % (now.day, now.month, now.year)

with open (filename,'w') as r:
   for updates in updates:
        news_item = {}
        r.write(updates.title.text)
        r.write('\n')
        r.write(updates.content.text)
        r.write('\n')
        r.write('\n')

