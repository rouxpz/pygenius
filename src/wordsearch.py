# -*- coding: utf-8 -*-

import sys
import json
import urllib2

from bs4 import BeautifulSoup

def wordsearch(page, query):

	opener = urllib2.build_opener()
	url = "http://rapgenius.com/search?page=%d&amp;q=%s" % (page, query)
	page = opener.open(url)
	soup = BeautifulSoup(page, from_encoding="utf-8")
	text = soup.find_all(class_="search_result") #finding everything in the class "search_result"
	l = len(text)

	#initialize blank list in which to keep the data
	data = []

	for i in range(0,l):
        #forcing text into a string format, cleaning up the text
		coded = str(text[i])
		#removing extra whitespace
		newcoded = ' '.join(coded.split())
		#getting rid of all the commas that were already in there
		clean = newcoded.replace(',', '') 
		#replacing all the extraneous HTML
		clean = clean.replace('<li class="search_result">', '')
		clean = clean.replace('<a class=" song_link" href="', '')
		clean = clean.replace('"> <span class="title_with_artists"> ', ',')
		clean = clean.replace('<em>', '').replace('</em>', '').replace('</span>', '').replace('</a>', '').replace('</li>', '').replace('<br/>', ' ').replace('</p>', '')
		clean = clean.replace('   <p>', ',')
		clean = clean.replace(' – ', ',')
		clean = clean.replace('&amp;', '&')
		data.append(clean)

	return data
