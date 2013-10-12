import urllib2
from bs4 import BeautifulSoup

def openPage(url):

	opener = urllib2.build_opener()
	page = opener.open(url)
	soup = BeautifulSoup(page, from_encoding="utf-8")

	opener.close()

	return soup