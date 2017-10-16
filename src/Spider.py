'''
Created on 16/09/2017

@author: Connor
@author: Connor, Craig
@author: Connor Hewett 15903849 & Craig Fraser
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
		
		# open visited file here
		# TO DO: might need to open txt file with w and clear it before a
		file = open("visited.txt", "w")
		
		# loops through URLs in unvisited, adding them to visited
		while len(self.unvisited) > 0:
			print("====================")
			url = self.unvisited.pop(0)
			adjacencies = []
			
			self.depth = url[0] # this will get depth value of current URL
			self.depth+=1 # depth for the links we will be adding
			self.visited.append(url[1])
			file.writelines(url[1])

			print((len(self.visited) - 1), ': ', url[1])
			
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
		
		# close visited file here 
		file.close()

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
	i += 1	i += 1
	i += 1
=======
#lanks = [[0, 'http://www.dustyfeet.com']]
#spoder = Spider(lanks, 3, 'useless')
#spoder.crawl()
