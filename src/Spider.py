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
		visitedAdj = []
		maxDepth = None
		keyword = None
		spiderleg = SpiderLeg.SpiderLeg()
		images = []
		meta = []
		results = []

	def setup(self, ulinks, udepth, ukeyword):
		print("=== Setup ===")
		self.unvisited = ulinks
		self.visited = []
		self.visitedAdj = []
		self.maxDepth = udepth
		self.keyword = ukeyword
		self.spiderleg = SpiderLeg.SpiderLeg()
		self.images = []
		self.meta = []
		self.results = []
		
	def crawl(self):
		print("=== Crawl ===")
		
		# loops through URLs in unvisited, adding them to visited
		while len(self.unvisited) != 0:
			print("====================")
			currentAdj = []
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
			
			#images = self.spiderleg.getImages(url[1])
			meta = self.spiderleg.getMeta(url[1])
			for content in meta:
				if (self.keyword in content) and (url[1] not in self.results):
					self.results.append(url[1])
			
			# 
			if (self.spiderleg.getHyperlink(url[1]) != None):
				links = self.spiderleg.getHyperlink(url[1])
				for link in links:
					if (link not in self.visited) and (link not in self.unvisited) and (self.depth < self.maxDepth) and (link != None):
						# need to actually check link is a link
						parser = urlparse(link)
						if (parser.scheme != '') and (parser.netloc != '') and (parser.scheme != None) and (parser.netloc != None):
							self.unvisited.append([self.depth, link])
							currentAdj.append(len(self.unvisited))# also need to add link to adj matrix ???
			self.visitedAdj.append(currentAdj)
			print("====================")
		
		# the visited array - print this out once done crawling
		print(self.visited)
		print("Adjacency List")
		print(self.visitedAdj)

	def getResults(self):
		# return list of links that had keyword in meta
		links = self.results
		return links
