import urllib.request
from bs4 import BeautifulSoup

def getTitle( url ):
	ret = 'No Title Found'
	soup = openUrl(url)# urlopen
	if soup is not None and soup.title is not None:
		ret = soup.title.text
	return ret

def getHyperLink( url ):
	links = []
	soup = openUrl(url)
	if soup != None:
		for link in soup.find_all('a'):
			absLink = urllib.parse.urljoin(url, link.get('href'))
			if 'mailto' not in absLink:
				links.append(absLink)
	return links

def getImages( url ):
	soup = openUrl(url)
	images = []
	if soup != None:
		imageTags = soup.find_all(['img', 'image'])
		for tag in imageTags:
			if tag is not None:
				images.append([tag.get('src')])
				images[-1].append(imageHelper(tag, 'alt'))
				images[-1].append(imageHelper(tag, 'width'))
				images[-1].append(imageHelper(tag, 'height'))
	return images
	
def getMeta( url ):
	soup = openUrl(url)
	meta = []
	if soup != None:
		metaTags = soup.find_all('meta')
		for tag in metaTags:
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
	return soup

def imageHelper( tag, attr ):
	result = 'No ' + attr
	if tag.get(attr) is not None:
		result = tag.get(attr)
	return result	

