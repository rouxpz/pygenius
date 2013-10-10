# -*- coding: utf-8 -*-

import sys
import json
import urllib2

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
		#lyric = lyric.split('<br/')
		#lyric = lyric.split("<p>")[1]
		words = words.split("<br/>")
		m = len(words)
		for j in range(0, 10):
			if j == 0:
				words[j] = words[j].split("p>")[1]
				print words[j]		
			elif j > 0:
				lyric = words[j].split(">")[1]
				lyric = lyric.split("<")[0]
				#print lyric
				lyrics.append(lyric)
				#n = len(wordsnew)
				#print n
	print lyrics