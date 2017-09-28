'''
Created on 16/09/2017

@author: Connor
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

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
        page = urlopen(url)
        soup = BeautifulSoup(page, 'lxml')
        for link in soup.find_all('img'):
            print(link.get('src'))    
        
    def getMeta(self, url):
        page = urlopen(url)
        soup = BeautifulSoup(page, 'lxml')
        for link in soup.find_all('meta'):
            print(link.get('name'))


