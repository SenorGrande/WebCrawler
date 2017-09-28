'''
Created on 16/09/2017

@author: Connor
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

class SpiderLeg:
    
    def __init__(self):
        print("=== Spider Leg ===")
    
    def getTitle(self, url):
        page = urlopen(url)
        soup = BeautifulSoup(page, 'lxml')
        return soup.title.string
        
    def getHyperlink(self, url):
        page = urlopen(url)
        soup = BeautifulSoup(page, 'lxml')
        links = []
        for link in soup.find_all('a'):
            links.append(link.get('href'))
        return links
        
    def getImages(self, url):    
        page = urlopen(url)
        soup = BeautifulSoup(page, 'lxml')
        images = []
        for link in soup.find_all('img'):
            images.append(link.get('src'))
        return images
        
    def getMeta(self, url):
        page = urlopen(url)
        soup = BeautifulSoup(page, 'lxml')
        meta = []
        for link in soup.find_all('meta'):
            meta.append(link.get('name'))
        return meta


