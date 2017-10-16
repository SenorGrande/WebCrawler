'''
Created on 16/09/2017

@author: Connor
'''
# beautiful soup 4
# lxml
# urlparse

import SpiderLeg
import urllib.parse

class Spider:

	def __init__(self, ulinks, udepth, ukeyword):
		self.depth = 0
		self.unvisited = ulinks
		self.visited = []
		#self.visitedAdj = []
		self.maxDepth = udepth
		self.keyword = ukeyword
		self.images = []
		self.meta = []
		self.results = []
		
	def crawl(self):
		print("=== Crawl ===")
		
		# loops through URLs in unvisited, adding them to visited
		while len(self.unvisited) > 0:
			print("====================")
			currentAdj = []
			url = self.unvisited.pop(0)

			self.depth = url[0] # this will get depth value of current URL
			self.depth+=1 # depth for the links we will be adding
			self.visited.append(url[1]) # does visited need the depth as well?

			#if contents is HTML ???
			print(url[1])
			
			#images = self.spiderleg.getImages(url[1])
			
			# Search for the keyword in meta tag keywords
			metaData = SpiderLeg.getMeta(url[1])
			# loop through each thing in meta, if the 0 is keywords, search 1 for the keyword
			for meta in metaData:
				if meta[0] == 'keywords':
					keywords = meta[1].lower()
					if (self.keyword in keywords) and (url[1] not in self.results):
						self.results.append(url[1])

			# Add links on page to unvisited list
			links = SpiderLeg.getHyperLink(url[1])
			for link in links:
				if link not in self.visited and link not in (item[1] for item in self.unvisited) and self.depth < self.maxDepth and link != None:
					# need to actually check link is a link
					parser = urllib.parse.urlparse(link)
					if parser.scheme != '' and parser.netloc != '' and parser.scheme != None and parser.netloc != None:
						self.unvisited.append([self.depth, link])
			
			#
			"""
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
			"""
		
		# the visited array - print this out once done crawling
		print("Visited: ")
		print(self.visited)
		#print("Adjacency List")
		#print(self.visitedAdj)

	def getResults(self):
		# return list of links that had keyword in meta
		links = self.results
		return links

#lanks = [[0, 'http://www.dustyfeet.com']]
#spoder = Spider(lanks, 3, 'useless')
#spoder.crawl()