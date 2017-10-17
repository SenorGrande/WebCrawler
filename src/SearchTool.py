'''
Created on 10/10/2017

@author: Connor Hewett 15903849 & Craig Fraser
'''

import Spider
import codecs
from operator import itemgetter

# Ask for seed URLs until a space, enter, q is entered
# Ask for keyword
# Specify d for the user, or ask them?

# if keyword in meta keywords, add to list, write to txt & display to screen

seeds = [[0,'http://sarsaparilla/crawltest/crawlTest.html']] # needs to handle multiple REMOVE THIS http://www.dustyfeet.com 
# list for seed URLs that user inputs
usrInput = input("Enter seed URL or press ENTER to continue: ") # TO DO: do we make this lowercase ???

while (usrInput != "" and usrInput != " "):
	seed = [0, usrInput]
	seeds.append(seed)
	usrInput = input("Enter seed URL or press ENTER to continue: ")
	# TODO validate the user's input to check its a valid link
	#if (usrInput != "" and usrInput != " "):
		

keyword = input("Enter keyword to search for: ") # make sure this isnt None or a Space

# Create Spider, passing parameters, searching for meta
links = []

maxDepth = 3 # the max depth the crawl can go

spider = Spider.Spider(seeds, maxDepth, keyword)
spider.crawl()

# Write the links to a text file
results = spider.results

file = open("results.txt", "w")
for result in results:
	file.write(result+'\r\n')
file.close()
	
# Print links to screen
print("Results List: ", results)
print("Adjacenccy: ", spider.adjacencyList)


# Calculate the page ranks using the adjacency list
c = 0.5 # change this to 0.15 like google?
adjList = spider.adjacencyList
pArray = [[0 for col in range(len(adjList))] for row in range(len(adjList))] # Stores the page ranks matrix
transformed = [[0 for col in range(len(adjList))] for row in range(len(adjList))] # flipped version of pArray

# Calculate page ranks
for i in range(len(adjList)):
	if len(adjList[i]) == 0:
		for j in range(len(adjList)):
			pArray[i][j] = 1.0 / len(adjList) # Sinks
	else:
		for k in range(len(adjList)):
			if k in adjList[i]:
				pArray[i][k] = (1.0 - c) / len(adjList) + c/len(adjList[i])
			else:
				pArray[i][k] = (1.0 - c) / len(adjList)

# Now we need to transform array (flip along main diagonal)
for j in range(0, len(adjList)):
	for k in range(j+1, len(adjList)):
		pArray[j][k],pArray[k][j] = pArray[k][j],pArray[j][k]

vArray = [1/len(adjList) for col in range(len(adjList))]
scaled = [0 for col in range(len(adjList))]
temp = [0 for col in range(len(adjList))]
scale = 1.0

# Calculate the page rank centrality
for i in range(len(adjList)):
	for j in range(len(adjList)):
		for k in range(len(adjList)):
			temp[j] += (pArray[j][k] * vArray[k])
	
	vArray = temp
	scale = 1.0 / min(vArray)
	
	for l in range(len(adjList)):
		scaled[l] = vArray[l] * scale

rankRes = []

for z in range(len(spider.results)):
	rankRes.append([spider.visited.index(spider.results[z]), scaled[spider.visited.index(spider.results[z])]])

#rankRes.sort(key=lambda tup: tup[1], reverse=True) # This is slower but reversed
rankRes.sort(key=itemgetter(1), reverse=True) # This is faster but no need to import something

for y in range(len(rankRes)):
	print("Result: ", spider.visited[rankRes[y][0]])
	print("Rank: ", rankRes[y][1])
