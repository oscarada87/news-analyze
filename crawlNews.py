from pprint import pprint
from bs4 import BeautifulSoup
import selenium
import requests
import json

with open('news.json', 'r') as f:
    # json.dump(data, f)
    data = json.load(f)
# data = []
url2 = 'https://news.cnyes.com/news/id/4193535?exp=a'
url = 'https://news.cnyes.com/news/id/4193470?exp=a'

def crawl(url):
    data = {'title':'', 'time':'', 'content':'', 'resource':'', 'url':''}
    data['url'] = url
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    data['title'] = soup.find('span', {'itemprop':'headline'}).get_text()
    data['time'] = soup.find('time').get_text()
    data['resource'] = soup.find('span', {'data-reactid':'222'}).get_text()
    temp = soup.findAll('p')
    # pprint(temp)
    content = ''
    for i in temp:
        content = content + i.get_text() + '\n'
    data['content'] = content
    return data

# data.append(crawl(url))
# data.append(crawl(url2))

# with open('news.json', 'w') as f:
    # json.dump(data, f)
    # temp = json.load(f)

pprint(data)
