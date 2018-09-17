from pprint import pprint
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import json
import time



temp = []

def crawl():
    url = "http://www.chinatimes.com/realtimenews/260410?page="
    data = []
    # driver = webdriver.Chrome(r"./driver/chromedriver.exe")
    # driver.get(url)
    for i in range (1, 31):
        res = requests.get(url+str(i))
        soup = BeautifulSoup(res.text, 'html.parser')
        for i in soup.findAll('h2'):
            data.append(i.find('a')['href'])
    # pprint(data)
    # driver.find_element_by_link_text('下一頁').click()
    # time.sleep(3)
    # url = driver.current_url
    # driver.quit()
    return data

data = crawl()
with open('url.json', 'w') as f:
    json.dump(data, f)


with open('url.json', 'r') as f:
    data = json.load(f)

pprint(data)
