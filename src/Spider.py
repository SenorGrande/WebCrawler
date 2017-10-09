'''
Created on 16/09/2017

@author: Connor
'''
# beautiful soup 4
# lxml
# urlparse

import SpiderLeg
from urllib.parse import urlparse

# need to include depth, first one will be 0
unvisited = [[0,'http://sarsaparilla/crawlTest.html']] # needs to handle multiple
visited = [] # stores hyperlinks that have been visited
links = [] # stores the hyperlinks found on a page
maxDepth = 5 # the max depth the crawl can go
depth = 0 # the current depth of the crawl
keyword = '' # keyword we are searching

images = []
meta = []

spiderleg = None

class Spider:

	def __init__(self):
		print("=== Spider ===")

	def setup(self, ulinks, udepth, ukeyword):
		print("=== Setup ===")
		unvisited = ulinks
		maxDepth = udepth
		keyword = ukeyword
		
	def crawl(self):
		print("=== Crawl ===")
		
		spiderleg = SpiderLeg.SpiderLeg() # MOVE???
		
		# loops through URLs in unvisited, adding them to visited
		while len(unvisited) != 0:
			print("====================")
			url = unvisited.pop(0)
			depth = url[0] # this will get depth value of current URL
			depth+=1 # depth for the links we will be adding
			visited.append(url[1]) # does visited need the depth as well?

			#if contents is HTML ???
			print(url[1])
			if (spiderleg.getTitle(url[1]) != None):
				title = spiderleg.getTitle(url[1])
			print("+++++++++++")
			print(visited)
			print("+++++++++++")
			print("-----------")
			print(unvisited)
			print("-----------")
			#images = spiderleg.getImages(url[1])
			#meta = spiderleg.getMeta(url[1])
			if (spiderleg.getHyperlink(url[1]) != None):
				links = spiderleg.getHyperlink(url[1])
				for link in links:
					if (link not in visited) and (link not in unvisited) and (depth < maxDepth) and (link != None):
						# need to actually check link is a link
						parser = urlparse(link)
						if (parser.scheme != '') and (parser.netloc != '') and (parser.scheme != None) and (parser.netloc != None):
							unvisited.append([depth, link])
			print("====================")


spider = Spider() #Spider.Spider() if importing this class
spider.setup(unvisited, 5, "test")
spider.crawl()
