from pprint import pprint
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time
import json
import re
import abc

class Crawler(abc.ABC):
    def __init__(self, url, keyWord):
        self.url = url
        self.keyWord = keyWord
        self.news = []
        self.driver = webdriver.Chrome(r"./driver/chromedriver.exe")

    def GetNews(self):
        return NotImplemented

class IDCrawler(Crawler):
    def __init__(self, keyWord):
        super(IDCrawler, self).__init__("https://www.inside.com.tw/", keyWord)
        self.keyUrl = ""
        self.singleNewsSoup = None
        self.singleNews = {'title':'', 'time':'', 'content':'', 'resource':'', 'url':''}
        self.urlList = []
        self.InitDriver()

    def InitDriver(self):
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1920, 1080)

    def GetKeyUrlsWithkeyWord(self):
        self.driver.get(self.url)
        searchButton = self.driver.find_element_by_class_name("search_submit")
        ActionChains(self.driver).move_to_element(searchButton).perform()
        self.driver.find_element_by_id("search").send_keys(self.keyWord)
        searchButton.click()
        self.keyUrl = self.driver.current_url.split("?")[0] + "page/"

    def SubstitudeFunction(self):
        self.keyUrl = "https://www.inside.com.tw/page/"

    def GetNewsUrls(self):
        for i in range (1, 3):
            res = requests.get(self.keyUrl + str(i) + "?s=" + self.keyWord)
            soup = BeautifulSoup(res.text, 'html.parser')
            for link in soup.findAll('h3',class_='post_title'):
                self.urlList.append(link.find('a')['href'])
        # pprint(self.urlList)

    def GetNewsSoup(self, link):
        res = requests.get(link)
        self.singleNews['url'] = link
        self.singleNewsSoup = BeautifulSoup(res.text, 'html.parser')

    def GetTitle(self):
        self.singleNews['title'] = self.singleNewsSoup.find('h1',class_='post_header_title').get_text().strip()

    def GetTime(self):
        self.singleNews['time'] = self.singleNewsSoup.find('li',class_='post_date').find('span').get_text()

    def GetContent(self):
        temp = self.singleNewsSoup.find('div',class_='post_content article').find_all('p')
        article = ''
        for i in temp:
            article = article + i.get_text()
        self.singleNews['content'] = article

    def GetResource(self):
        self.singleNews['resource'] = self.singleNewsSoup.find('span',class_='post_author').find('a').get_text()

    def CrawlAllNews(self):
        count = 1
        for link in self.urlList:
            self.GetNewsSoup(link)
            self.GetTitle()
            self.GetTime()
            self.GetContent()
            self.GetResource()
            self.news.append(self.singleNews)
            print("第" + str(count) + "則新聞完成!!")
            self.singleNews = {'title':'', 'time':'', 'content':'', 'resource':'', 'url':''}
            count = count + 1

    def Start(self):
        self.GetKeyUrlsWithkeyWord()
        self.GetNewsUrls()
        # pprint(self.urlList)
        self.CrawlAllNews()
        pprint(self.news)

def main():
    keyWord = input("請輸入關鍵字: ")
    CT = IDCrawler(keyWord)
    try:
        CT.Start()
    except:
        pass
    time.sleep(100)

main()
