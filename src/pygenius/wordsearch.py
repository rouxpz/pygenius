# -*- coding: utf-8 -*-

import sys
import re
import pageopen
import pagination

def searchWords(query, arg='data'):

	#initialize blank list in which to keep the data
	data = []
	links = []

	num = pagination.getTotalPages(query)

	for i in range(1, num+1):
	
		url = "http://rapgenius.com/search?page=%d&amp;q=%s" % (i, query)
		
		soup = pageopen.openPage(url)
		text = soup.find_all(class_="search_result") #finding everything in the class "search_result"
		l = len(text)

		for j in range(0,l):
        	#forcing text into a string format, cleaning up the text
			coded = str(text[j])

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

			#splitting into list
			results = clean.split(',')
			results[0] = 'http://rapgenius.com/%s' % results[0]
			results[2] = results[2].strip()
			data.append([results[1], results[2]])
			links.append(results[0])


	if arg == 'link':
		return links
	else:
		return data

