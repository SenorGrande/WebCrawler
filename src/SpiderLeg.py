'''
Created on 16/09/2017

@author: Connor
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

print("testing")

class SpiderLeg:
    
    def __init__(self):
        url = 'http://www.ace-hire.com/'
    
    def getTitle(self, url):
        page = urlopen(url)
        soup = BeautifulSoup(page, 'lxml')
        print(soup.title.string)
        
    def getHyperlink(self, url):
        page = urlopen(url)
        soup = BeautifulSoup(page, 'lxml')
        for link in soup.find_all('a'):
            print(link.get('href'))
        
        
    def getImages(self, url):
        print("get names of all image files in the web page url, as well as the height, width and alt attributes")
        page = urlopen(url)
        soup = BeautifulSoup(page, 'lxml')
        for link in soup.find_all('img'):
            print(link.get('src'))
        
        
    def getMeta(self, url):
        print("get the meta data, including meta description, and meta keywords of the web page url")
        page = urlopen(url)
        soup = BeautifulSoup(page, 'lxml')
        for link in soup.find_all('meta'):
            print(link.get('name'))


url = 'http://www.ace-hire.com/'
test = SpiderLeg().getTitle(url)
test = SpiderLeg().getHyperlink(url)
test = SpiderLeg().getImages(url)
test = SpiderLeg().getMeta(url)

