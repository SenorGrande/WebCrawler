'''
Created on 10/10/2017

@author: Connor Hewett 15903849 & Craig Fraser
'''

import Spider
import codecs

# Ask for seed URLs until a space, enter, q is entered
# Ask for keyword
# Specify d for the user, or ask them?

# if keyword in meta keywords, add to list, write to txt & display to screen

seeds = [[0,'http://sarsaparilla/crawlTest.html']] # needs to handle multiple REMOVE THIS http://www.dustyfeet.com 
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

maxDepth = 2 # the max depth the crawl can go

spider = Spider.Spider(seeds, maxDepth, keyword)
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
print("Results List: ")
print(results)
