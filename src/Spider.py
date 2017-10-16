'''
Created on 16/09/2017

@author: Connor
@author: Connor, Craig
'''
import SpiderLeg
import urllib.parse

class Spider:

	def __init__(self, ulinks, udepth, ukeyword):
		self.depth = 0
		self.unvisited = ulinks
		self.visited = []
		self.maxDepth = udepth
		self.keyword = ukeyword
		self.adjacencyList = []
		#self.images = []
		#self.meta = []
		#self.results = []
		
	def crawl(self):
		print("=== Visited ===")
		
		# loops through URLs in unvisited, adding them to visited
		while len(self.unvisited) > 0:
			print("====================")
			url = self.unvisited.pop(0)
			adjacencies = []
			
			self.depth = url[0] # this will get depth value of current URL
			self.depth+=1 # depth for the links we will be adding
			self.visited.append(url[1])

			print((len(self.visited) - 1), ': ', url[1])
			
			links = SpiderLeg.getHyperLink(url[1])
			for link in links:
				if link != None and link is not url[1]:
					parser = urllib.parse.urlparse(link)
					if link in self.visited:
						i = self.visited.index(link)
						if i not in adjacencies:
							adjacencies.append(i)
					elif link in (item[1] for item in self.unvisited):
						i = len(self.visited) + self.unvisited.index(self.unvisited[:][1])
						if i not in adjacencies:
							adjacencies.append(i)
					elif self.depth < self.maxDepth and parser.scheme != '' and parser.netloc != '' and parser.scheme != None and parser.netloc != None:
						i = len(self.visited) + len(self.unvisited)
						if i not in adjacencies:
							adjacencies.append(i)
						self.unvisited.append([self.depth, link])
			self.adjacencyList.append(adjacencies)
			
			
	def getResults(self):
		# return list of links that had keyword in meta
		links = self.results
		return links

lanks = [[0, 'http://home.mcom.com/home/welcome.html']]
spoder = Spider(lanks, 3, 'useless')
spoder.crawl()

i = 0
for a in spoder.adjacencyList:
	print(i, ': ', a)
	i += 1