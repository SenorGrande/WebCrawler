'''
Created on 16/09/2017

@author: Connor Hewett 15903849 & Craig Fraser 15889604
'''
import urllib.request
from bs4 import BeautifulSoup

def getTitle( url ):
	ret = 'No Title Found'
	soup = openUrl(url)
	#If title exists in the site, return its text
	if soup is not None and soup.title is not None:
		ret = soup.title.text
	return ret

def getHyperLink( url ):
	links = []
	soup = openUrl(url)
	#If url opened successfully, finds all links, add them to the list
	if soup != None:
		#For all <a> tags
		for link in soup.find_all('a'):
			#Gets href value from <a> tags, also converts relative urls to absolute urls
			absLink = urllib.parse.urljoin(url, link.get('href'))
			
			#Parse the link to ensure it's valid
			parsedUrl = urllib.parse.urlparse(absLink)
			
			#If url can be parsed correctly, and is not a mailto: link, add it to the list
			if 'mailto' not in absLink and absLink != None and absLink != url and parsedUrl.scheme != '' and parsedUrl.netloc != '' and parsedUrl.scheme != None and parsedUrl.netloc != None:#Gotta be a better way to do this
				links.append(absLink)
	return links

def getImages( url ):
	soup = openUrl(url)
	images = []
	#If url opened successfully, find all <img> and <image> tags
	if soup != None:
		imageTags = soup.find_all(['img', 'image'])
		#For each <img> and <image> tag...
		for tag in imageTags:
			if tag is not None:
				#...create a sub-list containing the src, add it to the 'images' list
				images.append([tag.get('src')])
				#Append the alt, width and height to the sub-list
				images[-1].append(imageHelper(tag, 'alt'))
				images[-1].append(imageHelper(tag, 'width'))
				images[-1].append(imageHelper(tag, 'height'))
	return images
	
def getMeta( url ):
	soup = openUrl(url)
	meta = []
	#If url opened successfully, find all <meta> tags.
	if soup != None:
		metaTags = soup.find_all('meta')
		#For each meta tag...
		for tag in metaTags:
			#Extract the name and content and add them to the metadata list as a key-value pair
			if tag is not None and tag.get('name') is not None:
				if tag.get('content') is not None:
					meta.append([tag.get('name'), tag.get('content')])
				else:
					meta.append([tag.get('name'), 'None'])
	return meta

def openUrl(url):
	try:
		page = urllib.request.urlopen(url)
		soup = BeautifulSoup(page, 'lxml')
	except urllib.error.URLError as e:
		#print(e.reason)
		soup = None
	except:
		soup = None
	return soup

def imageHelper( tag, attr ):
	result = 'No ' + attr
	if tag.get(attr) is not None:
		result = tag.get(attr)
	return result	

