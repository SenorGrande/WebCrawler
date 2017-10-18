'''
Created on 10/10/2017

@author: Connor Hewett 15903849 & Craig Fraser
'''

import Spider
import codecs

maxDepth = 3 # the max depth the crawl will travel
RESULT_URL = 0 # Index position for URL
RESULT_RANK = 1 # Index position for Page Rank

# list for seed URLs that user inputs
seeds = [[0,'http://sarsaparilla/crawltest/crawlTest.html']]
usrInput = input("Enter seed URL or press ENTER to continue: ")

while (usrInput != "" and usrInput != " "):
	seed = [0, usrInput]
	seeds.append(seed)
	usrInput = input("Enter seed URL or press ENTER to continue: ")
	# TODO validate the user's input to check its a valid link
		
keyword = input("Enter keyword to search for: ").lower() # TODO: make sure this isnt None or a Space???

spider = Spider.Spider(seeds, maxDepth, keyword) # Create spider object initialised with the users seed urls and keyword
spider.crawl() # Start crawling process

c = 0.5 # This is the damping factor - change this to 0.15 like google?
adjList = spider.adjacencyList
pArray = [[0 for col in range(len(adjList))] for row in range(len(adjList))] # Stores the page ranks matrix
vArray = [1/len(adjList) for col in range(len(adjList))]
scaled = [0 for col in range(len(adjList))]
temp = [0 for col in range(len(adjList))]
scale = 1.0
rankRes = [] # Store the results hyperlinks and corresponding page rank centrality
results = spider.results # Get list of URL results from the Spider

# Write the results to a text file
file = open("results.txt", "w")
for result in results:
	file.write(result+'\r\n')
file.close()

# Calculate page ranks
for i in range(len(adjList)):
	if len(adjList[i]) == 0:
		for j in range(len(adjList)):
			pArray[i][j] = 1.0 / len(adjList) # If node is a sink
	else:
		for k in range(len(adjList)):
			if k in adjList[i]:
				pArray[i][k] = (1.0 - c) / len(adjList) + c/len(adjList[i]) # if k is connected to node i's
			else:
				pArray[i][k] = (1.0 - c) / len(adjList) # otherwise

# Transform the page rank array (flip along main diagonal)
for i in range(0, len(adjList)):
	for j in range(i+1, len(adjList)):
		pArray[i][j],pArray[j][i] = pArray[j][i],pArray[i][j]

# Calculate the page rank centrality
for i in range(len(adjList)):
	for j in range(len(adjList)):
		for k in range(len(adjList)):
			temp[j] += (pArray[j][k] * vArray[k])
	
	vArray = temp
	scale = 1.0 / min(vArray) # TODO: could use max
	
	for l in range(len(adjList)):
		scaled[l] = vArray[l] * scale

# Create list of URL results with their corresponding Page Rank values
for i in range(len(spider.results)):
	rankRes.append([spider.visited.index(spider.results[i]), scaled[spider.visited.index(spider.results[i])]])

rankRes.sort(key=lambda tup: tup[1], reverse=True) # Sort the results from highest page rank to lowest

# Print out the results in order they were sorted into
for i in range(len(rankRes)):
	print("Result: ", spider.visited[rankRes[i][RESULT_URL]])
	print("Rank: ", rankRes[i][RESULT_RANK])
