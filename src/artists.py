# -*- coding: utf-8 -*-

import sys
import json
import urllib2

from bs4 import BeautifulSoup

def albumList(query, arg):
#returns a list of album titles or links to the album on rapgenius.

	albums = []
	links = []

	query = '-'.join(query.split())
	opener = urllib2.build_opener()
	url = "http://rapgenius.com/artists/%s" % query
	page = opener.open(url)
	soup = BeautifulSoup(page, from_encoding="utf-8")
	text = soup.find_all(class_="album_link")

	l = len(text)

	for i in range(0, l):
		raw = str(text[i])
		raw = raw.replace('<a class="album_link" href="', '')
		raw = raw.replace('">', ',')
		raw = raw.replace('</a>', '')
		new = raw.split(',')

		album = new[1]
		albums.append(album)
		
		link = 'http://rapgenius.com%s' % new[0]
		links.append(link)

	if (arg == 'links'):
		return links
	elif (arg == 'titles'):
		return albums
	else:
		return "ERROR"

def returnDates(query):

	titles = albumList(query, 'titles')
	links = albumList(query, 'links')

	l = len(links)

	dates = []
	info = []

	for i in range(0, l):
		opener = urllib2.build_opener()
		url = links[i]
		page = opener.open(url)

		soup = BeautifulSoup(page, from_encoding="utf-8")
		names = soup.find_all('h1', class_="name")

		k = len(names)

		for j in range(0, k):
			date = str(names[j])
			date = ' '.join(date.split())
			search1 = date.find('(1')
			search2 = date.find('(2')
			if search1 != -1:
				date = '1'+ date.split('(1')[1] #strip everything before the date
				date = date.split(')')[0] #stripping everything after the date
				dates.append(date)
			elif search2 != -1:
				date = '2'+ date.split('(2')[1] #strip everything before the date
				date = date.split(')')[0] #stripping everything after the date
				dates.append(date)
			else:
				dates.append('None')

		info.append([titles[i], dates[i]])

	return info



		#print url
