'''
Created on 16/09/2017

@author: Connor Hewett 15903849 & Craig Fraser 15889604
'''
import SpiderLeg
import urllib.parse

class Spider:

	#Constants
	TUPLE_URL_INDEX = 1
	TUPLE_DEPTH_INDEX = 0
	META_KEY = 0
	META_VALUE = 1
	VISITED_FILE_NAME = "visited.txt"

	def __init__(self, ulinks, udepth, ukeyword):
		self.depth = 0
		self.unvisited = ulinks
		self.visited = []
		self.maxDepth = udepth
		self.searchKeyword = ukeyword
		self.adjacencyList = []
		self.results = []
	
	#Gets a list of hyperlinks, and adds them to visited/unvisited/adjacencyList as appropriate.
	def processLinks(self, url):
		#Create list of adjacencies for this url 'node'
		adjacencies = []
		
		#Get list of hyperlinks
		links = SpiderLeg.getHyperLink(url)
		
		#Iterate through all the scraped links...
		for link in links:
			#If link has already been visited...
			if link in self.visited:
				#Add it to the adjacencies, if it's not already there.
				i = self.visited.index(link)
				if i not in adjacencies:
					adjacencies.append(i)
			
			#If link already in the unvisited list...
			elif link in (item[Spider.TUPLE_URL_INDEX] for item in self.unvisited):
				try:
					#Calculates the future 'visited' index of the link;
					i = len(self.visited) + self.unvisited.index(self.unvisited[:][Spider.TUPLE_URL_INDEX])
				except:#Not sure if this is needed, do some testing.
					i = -1
					print('???')
				#Add the calculated adjacency to the list, if it's not already there.
				if i not in adjacencies:
					adjacencies.append(i)
			
			#If link not already in unvisited/visited, and doesn't exceed max depth...
			elif self.depth < self.maxDepth:
				#Calculate future 'visited' index of the link
				i = len(self.visited) + len(self.unvisited)
				#Add calculated adjacency to list, if it's not already there
				if i not in adjacencies:
					adjacencies.append(i)
				#Add link to unvisited list
				self.unvisited.append([self.depth, link])
		
		#Add list of current link's adjacencies to adjacencyList
		self.adjacencyList.append(adjacencies)
	
	#Searches for a keyword in  a site's 'keywords' metadata
	def keywordSearch(self, url):
		#Get metadata from SpiderLeg.
		#Metadata is a list of key-value pairs; the key is the name, value is the content.
		metaData = SpiderLeg.getMeta(url)
		
		#Search for the key 'keywords' in meta.
		for meta in metaData:
			if 'keywords' in meta[Spider.META_KEY]:
				keywords = meta[Spider.META_VALUE].lower()
				#If key is found, check if the search keyword is in the 'keywords' value
				if (self.searchKeyword.lower() in keywords) and (url not in self.results):
					#Add url to results if keyword match found
					self.results.append(url)
	
	#Crawls websites from a list of seed urls to a given depth
	def crawl(self):
		print("\n=======VISITED=======")
		
		# open visited file here
		file = open(Spider.VISITED_FILE_NAME, "w")
		
		# loops through URLs in unvisited, adding them to visited
		while len(self.unvisited) > 0:
			print("=====================")
			url = self.unvisited.pop(0)
			
			self.depth = url[Spider.TUPLE_DEPTH_INDEX] # this will get depth value of current URL
			self.depth += 1 # depth for the links we will be adding
			self.visited.append(url[Spider.TUPLE_URL_INDEX])#Add to visited list
			file.writelines(url[Spider.TUPLE_URL_INDEX] + "\r\n")#Write to visited text file
			
			#Print the visited URL, and its index in the visited list
			print((len(self.visited) - 1), ': ', url[Spider.TUPLE_URL_INDEX])
			
			self.keywordSearch(url[Spider.TUPLE_URL_INDEX])
			
			self.processLinks(url[Spider.TUPLE_URL_INDEX])
		
		# close visited file here 
		file.close()

'''
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
'''