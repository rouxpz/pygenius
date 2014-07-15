import urllib2
from bs4 import BeautifulSoup

def openPage(url):

	opener = urllib2.build_opener()
	opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
	page = opener.open(url)
	soup = BeautifulSoup(page, from_encoding="utf-8")

	opener.close()

	return soup