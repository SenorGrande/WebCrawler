'''
Created on 16/09/2017

@author: Connor
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

def openUrl(url):
        try:
            page = urlopen(url)
            soup = BeautifulSoup(page, 'lxml')
        except:
            print("Unable to open url")
            return None
        return soup

class SpiderLeg:
    
    def __init__(self):
        print("=== Spider Leg ===")
    
    def getTitle(self, url):
        soup = openUrl(url) # urlopen
        if soup == None:
            return None
        return soup.title.string
        
    def getHyperlink(self, url):
        soup = openUrl(url)
        if soup == None:
            return None
        links = []
        for link in soup.find_all('a'):
            links.append(link.get('href'))
        return links
        
    def getImages(self, url):
        soup = openUrl(url)
        if soup == None:
            return None
        images = []
        for link in soup.find_all('img'):
            images.append(link.get('src'))
        return images
        
    def getMeta(self, url):
        soup = openUrl(url)
        if soup == None:
            return None
        meta = []
        for link in soup.find_all('meta'):
                if (link.get('content') != None):
                        meta.append(link.get('content')) # get name tag also ??? multiple arrays for diff tags or 2D array?
        return meta
