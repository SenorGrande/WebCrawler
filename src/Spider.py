'''
Created on 16/09/2017

@author: Connor Hewett 15903849 & Craig Fraser
@author: Connor Hewett 15903849 & Craig Fraser 15889604
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
		self.results = []
	
	def processLinks(self, url):
		# Add links on page to unvisited list
		adjacencies = []
		links = SpiderLeg.getHyperLink(url)
		for link in links:
			if link != None and link is not url:
				parser = urllib.parse.urlparse(link)
				if link in self.visited:
					i = self.visited.index(link)
					if i not in adjacencies:
						adjacencies.append(i)
				elif link in (item[1] for item in self.unvisited):
					try:
						i = len(self.visited) + self.unvisited.index(self.unvisited[:][1])
					except:
						i = -1
						print('???')
					if i not in adjacencies:
						adjacencies.append(i)
				elif self.depth < self.maxDepth and parser.scheme != '' and parser.netloc != '' and parser.scheme != None and parser.netloc != None:
					i = len(self.visited) + len(self.unvisited)
					if i not in adjacencies:
						adjacencies.append(i)
					self.unvisited.append([self.depth, link])
		self.adjacencyList.append(adjacencies)
	
	def keywordSearch(self, url):
		# Search for the keyword in meta tag keywords
		metaData = SpiderLeg.getMeta(url)
		# loop through each thing in meta, if the 0 is keywords, search 1 for the keyword
		for meta in metaData:
			if 'keywords' in meta[0]:
				keywords = meta[1].lower()
				if (self.keyword in keywords) and (url not in self.results):
					self.results.append(url)
	
	def crawl(self):
		print("\n=======VISITED=======")
		
		# open visited file here
		# TO DO: might need to open txt file with w and clear it before a
		file = open("visited.txt", "w")
		
		# loops through URLs in unvisited, adding them to visited
		while len(self.unvisited) > 0:
			print("=====================")
			url = self.unvisited.pop(0)
			#adjacencies = []
			
			self.depth = url[0] # this will get depth value of current URL
			self.depth+=1 # depth for the links we will be adding
			self.visited.append(url[1])
			file.writelines(url[1] + "\r\n")

			print((len(self.visited) - 1), ': ', url[1])
			
			self.keywordSearch(url[1])
			
			self.processLinks(url[1])
		
		# close visited file here 
		file.close()


#TESTING STUFF
lanks = [[0, 'http://www.dustyfeet.com']]
spoder = Spider(lanks, 3, 'tech')
spoder.crawl()

print("\n=====ADJACENCIES=====")
i = 0
for a in spoder.adjacencyList:
	print(i, ': ', a)
	i += 1
	
print("\n=======RESULTS=======")
for r in spoder.results:
	print(r)
print("")


