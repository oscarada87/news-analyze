from pprint import pprint
from bs4 import BeautifulSoup
import selenium
import requests
import json
import re

with open('url.json', 'r') as f:
    urlList = json.load(f)
# pprint(urlList)

# with open('news.json', 'r') as f:
    # json.dump(data, f)
    # data = json.load(f)
data = []
# url2 = 'https://news.cnyes.com/news/id/4193535?exp=a'
# url = 'https://news.cnyes.com/news/id/4193470?exp=a'
url = 'http://www.chinatimes.com'

def crawl(url):
    regex = re.compile(r'[\n\r\t]')
    data = {'title':'', 'time':'', 'content':'', 'resource':'', 'url':''}
    data['url'] = url
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    data['title'] = regex.sub(' ', soup.find('h1', {'id':'h1'}).get_text()).strip()
    data['time'] = regex.sub(' ', soup.find('time').get_text()).strip()
    data['resource'] = '中時電子報'
    temp = soup.findAll('p')
    # pprint(temp)
    content = ''
    for i in temp:
        content = content + i.get_text() + '\n'
    data['content'] = content
    # pprint(content)
    return data

# for index, i in enumerate(urlList):
#     data.append(crawl(url + i))
#     print('{}/{} ---done---'.format(index + 1, len(urlList)))
# data.append(crawl(url2))

# with open('news.json', 'w') as f:
#     json.dump(data, f)

with open('news.json', 'r') as f:
    # json.dump(data, f)
    data = json.load(f)

pprint(data)
