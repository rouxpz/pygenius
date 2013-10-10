# -*- coding: utf-8 -*-

import sys
import json
import urllib2
import re

from bs4 import BeautifulSoup

def searchSong(artist, query, arg='data'):

	data = []
	lyrics = []

	artist = '-'.join(artist.split())

	query = '-'.join(query.split())
	query = query.replace("'", '')
	query = artist +'-' + query + '-lyrics'

	opener = urllib2.build_opener()
	url = "http://rapgenius.com/%s" % query
	page = opener.open(url)
	soup = BeautifulSoup(page, from_encoding="utf-8")
	text = soup.find_all(class_="lyrics")
	l = len(text)

	for i in range(0, l):
		words = str(text[i])
		words = words.replace("<div", "[<div").replace('">', '">]')
		words = re.sub(r'\[.*?\]', '', words)
		words = words.replace('">]', '">')
		words = words.replace('<br/>', ',')
		words = words.split("</a>")
		m = len(words)

		#print words[3]
		for j in range(0, m-1):
			sections = words[j].split('">')
			lyric = sections[1]
			annotation = sections[0]
			lyrics.append(lyric)

	return lyrics

