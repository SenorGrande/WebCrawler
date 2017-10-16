'''
Created on 10/10/2017

@author: Connor Hewett 15903849 & Craig Fraser
'''

# Add page rank stuff
# will need to get visited and visited adj list

import Spider
import codecs

# Ask for seed URLs until a space, enter, q is entered
# Ask for keyword
# Specify d for the user, or ask them?

# if keyword in meta keywords, add to list, write to txt & display to screen

seeds = [] # list for seed URLs that user inputs
usrInput = "input"

while (usrInput != "" and usrInput != " "):
	usrInput = input("Enter seed URL or press ENTER to continue: ")
	# TODO validate the user's input to check its a valid link
	if (usrInput != "" and usrInput != " "):
		seeds.append(usrInput)

keyword = input("Enter keyword to search for: ")

# Create Spider, passing parameters, searching for meta
links = []

seeds = [[0,'http://sarsaparilla/crawlTest.html']] # needs to handle multiple REMOVE THIS
maxDepth = 2 # the max depth the crawl can go

spider = Spider.Spider()
spider.setup(seeds, maxDepth, keyword) # This has no effect whatsoever
spider.crawl()

# Write the links to a text file
results = spider.getResults()

with codecs.open("link.txt", "w", "utf-8") as resFile:
	#file = open("link.txt", "w")
	#file.writelines(results)
	for result in results:
                resFile.write(result+'\n')
	#resFile.close()
	
# Print links to screen
print("List: ")
print(results)
test = open("link.txt", "r")
print("File: ")
print(test.read())
