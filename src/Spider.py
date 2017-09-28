'''
Created on 16/09/2017

@author: Connor
'''

import SpiderLeg

depth = 5
unvisited = ['http://www.android.com/'] # needs to handle multiple
visited = []

spider = SpiderLeg.SpiderLeg()

# loops through URLs in unvisited, adding them to visited
for i in range(len(unvisited)):
    url = unvisited.pop(0)
    visited.append(url)

    test = spider.getTitle(url)
    test = spider.getHyperlink(url)
    test = spider.getImages(url)
    test = spider.getMeta(url)
