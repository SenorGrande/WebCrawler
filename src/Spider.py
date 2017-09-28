'''
Created on 16/09/2017

@author: Connor
'''

import SpiderLeg

depth = 5
unvisited = ['http://www.android.com/'] # needs to handle multiple
visited = []
links = []
images = []
meta = []
spider = SpiderLeg.SpiderLeg()

# loops through URLs in unvisited, adding them to visited
for i in range(len(unvisited)):
    url = unvisited.pop(0)
    visited.append(url)

    title = spider.getTitle(url)
    print(title)
    links = spider.getHyperlink(url)
    images = spider.getImages(url)
    meta = spider.getMeta(url)
