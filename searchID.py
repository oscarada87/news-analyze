from pprint import pprint
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import requests
import time
import json
import re

class Crawler():
    def __init__(self, url):
        self.url = url
        self.urlList = []
        self.news = []
        self.driver = webdriver.Chrome(r"./driver/chromedriver.exe")


class IDCrawler(Crawler):
    def __init__(self, keyWord):
        super(IDCrawler, self).__init__("https://www.inside.com.tw/")
        self.keyWord = keyWord
        self.keyUrl = ""
        self.singleNewsSoup = None
        self.singleNews = {'title':'', 'time':'', 'content':'', 'resource':'', 'url':''}
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
        pass

    def GetTime(self):
        pass

    def GetContent(self):
        pass

    def GetResource(self):
        pass

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
        # pprint(self.news)

def main():
    keyWord = input("請輸入關鍵字: ")
    CT = IDCrawler(keyWord)
    CT.Start()
    time.sleep(100)

main()
