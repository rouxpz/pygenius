# -*- coding: utf-8 -*-

import sys
import re
import pageopen

#returns song lyrics and the link to the annotations.
#when arg="annotations", the results can be passed into the searchAnnotations() function below.
def searchSong(artist, query, arg='data'):

	data = []
	lyrics = []
	annotations = []

	artist = '-'.join(artist.split())

	query = '-'.join(query.split())
	query = query.replace("'", '')
	query = artist +'-' + query + '-lyrics'

	url = "http://rapgenius.com/%s" % query
	soup = pageopen.openPage(url)
	text = soup.find_all(class_="lyrics")
	l = len(text)

	for i in range(0, l):
		words = str(text[i])
		words = words.replace("<div", "{<div").replace('">', '">}')
		words = re.sub(r'\{.*?\}', '', words)
		words = words.replace('">}', '">')
		words = words.replace("<i>", '').replace("</i>", '')
		words = words.replace('<br/>', '')
		words = words.replace("<p>", '').replace("</p>", '')
		words = words.split("</a>")
		m = len(words)

		for j in range(0, m-1):
			a = re.search(r'\<.*?\>', words[j])
			lyric = re.sub(r'\<.*?\>', '', words[j])
			lyric = lyric.strip()
			#lyric = ' '.join(lyric.split())
			annotation = a.group(0)
			lyrics.append(lyric)

			search1 = annotation.find('"no_annotation"')
			search2 = annotation.find('data-editorial-state')

			if search1 != -1:
				annotations.append("Not annotated")
			elif search2 != -1:
				annotation = re.sub(r'\<.*?\/', '', annotation)
				annotation = annotation.replace('">', '')
				annotations.append('http://rapgenius.com/' + annotation)

	m = len(lyrics)

	for i in range (0, m):
		data.append([lyrics[i], annotations[i]])

	if arg == 'lyrics':
		return lyrics
	elif arg == 'annotations':
		return annotations
	else:
		return data

#returns content of annotations
def searchAnnotations(query):

	url = query
	soup = pageopen.openPage(url)
	text = soup.find_all(id="main")

	note = str(text)

	note = note.split("</div>")[1]
	note = note.split("<p><em>")[0]
	note = note.replace("<p>", '').replace("</p>", '').replace('<strong>', '').replace('</strong>','').replace('<em>', '"').replace('</em>', '"')

	return note