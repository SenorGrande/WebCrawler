'''
Created on 16/09/2017

@author: Connor
'''
# beautiful soup 4
# lxml
# urlparse

import SpiderLeg
from urllib.parse import urlparse

class Spider:

	def __init__(self):
		print("=== Spider ===")
		depth = 0 # the current depth of the crawl
		unvisited = None
		visited = []
		maxDepth = None
		keyword = None
		spiderleg = SpiderLeg.SpiderLeg()
		images = []
		meta = []

	def setup(self, ulinks, udepth, ukeyword):
		print("=== Setup ===")
		self.unvisited = ulinks
		self.maxDepth = udepth
		self.keyword = ukeyword
		
	def crawl(self):
		print("=== Crawl ===")
		
		# loops through URLs in unvisited, adding them to visited
		while len(self.unvisited) != 0:
			print("====================")
			url = self.unvisited.pop(0)
			self.depth = url[0] # this will get depth value of current URL
			self.depth+=1 # depth for the links we will be adding
			self.visited.append(url[1]) # does visited need the depth as well?

			#if contents is HTML ???
			print(url[1])
			if (self.spiderleg.getTitle(url[1]) != None):
				title = self.spiderleg.getTitle(url[1])
			print("+++++++++++")
			print(self.visited)
			print("+++++++++++")
			print("-----------")
			print(self.unvisited)
			print("-----------")
			#images = spiderleg.getImages(url[1])
			#meta = spiderleg.getMeta(url[1])
			if (self.spiderleg.getHyperlink(url[1]) != None):
				links = self.spiderleg.getHyperlink(url[1])
				for link in links:
					if (link not in self.visited) and (link not in self.unvisited) and (self.depth < self.maxDepth) and (link != None):
						# need to actually check link is a link
						parser = urlparse(link)
						if (parser.scheme != '') and (parser.netloc != '') and (parser.scheme != None) and (parser.netloc != None):
							self.unvisited.append([self.depth, link])
			print("====================")
		
		# the visited array - print this out once done crawling

	def getResults(self):
		# return list of links that had keyword in meta
		links = ["look", "im", "a", "pickle", "morty"]
		return links
	
	