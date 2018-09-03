from pprint import pprint
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import json
import time

url = "http://www.chinatimes.com/realtimenews/260410"

temp = []

def crawl():
    global url
    data = []
    driver = webdriver.Chrome(r"./driver/chromedriver.exe")
    driver.get(url)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    for i in soup.findAll('h2'):
        data.append(i.find('a')['href'])
    # pprint(data)
    driver.find_element_by_link_text('下一頁').click()
    time.sleep(3)
    url = driver.current_url
    driver.quit()
    return data

for i in range(3):
    temp.extend(crawl())
pprint(temp)
