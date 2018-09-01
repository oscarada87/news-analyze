from pprint import pprint
from bs4 import BeautifulSoup
import selenium
import requests


url = 'https://news.cnyes.com/news/id/4193470?exp=a'

def crawl(url):
    data = {'title':'', 'time':'', 'content':'', 'resource':'', 'url':''}
    data['url'] = url
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    data['title'] = soup.find('span', {'itemprop':'headline'}).get_text()
    data['time'] = soup.find('time').get_text()
    data['resource'] = soup.find('span', {'data-reactid':'222'}).get_text()
    return data

data = crawl(url)
pprint(data)
