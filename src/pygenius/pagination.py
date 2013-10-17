import re
import pageopen

#works around infinite scroll to return the total number of pages of info available
def openPage(artist):

	artist = '-'.join(artist.split())
	url = "http://rapgenius.com/artists/%s" % artist

	soup = pageopen.openPage(url)

	pages = soup.find_all(class_="pagination")
	pages = str(pages)
	pages = pages.split('</a>')

	pageLink = pages[len(pages) - 3]
	pageLink = pageLink.replace('<a href="', 'http://rapgenius.com')
	pageLink = pageLink.split('"')[0]
	pageLink = pageLink.strip()

	return pageLink

#gets the total pages available as an integer, for use with wordsearch
def getTotalPages(query):

	url = 'http://rapgenius.com/search?q=%s' % query

	soup = pageopen.openPage(url)

	pages = soup.find_all(class_="pagination")
	pages = str(pages)
	pages = pages.split('</a>')

	pageLink = pages[len(pages) - 3]
	pageLink = pageLink.replace('<a href="', '')
	pageLink = pageLink.split('"')[0]
	pageLink = pageLink.strip()

	l = re.search(r'\/.*?\&', pageLink)
	l = l.group(0)
	l = l.replace('/search?page=', '').replace('&', '')
	l = int(l)

	return l


#for use with artists.findAllSongs()
def getSongs(link):

	data = []
	tracks = []
	links = []

	l = re.search(r';page\=.*?\;', link)
	l = l.group(0)
	l = l.replace(';page=', '').replace('&amp;', '')
	l = int(l)

	for i in range (1, l+1):

		pageNo = ';page=%d&amp;' % i

		url = re.sub(r';page\=.*?\;', '{', link)
		url = pageNo.join(url.split('{'))

		soup = pageopen.openPage(url)

		songs = soup.find_all(class_="song_list")
		songs = str(songs)
		songsList = songs.split('</li>')

		if len(songsList) > 1:

			for song in songsList:
				song = ' '.join(song.split())

				if song != '</ul>]':
					p = re.search(r'\/.*?\"', song)
					page = p.group(0)
					page = page.replace('"', '')
					page = 'http://rapgenius.com%s' % page
					links.append(page)

				song = re.sub(r'\<.*?\>', '', song)
				song = song.replace('&amp;', '&').replace('[', '')
				song = song.strip()
				if song != ']':
					tracks.append(song)

		l = len(tracks)

		for i in range(0, l):
			data.append([links[i], tracks[i]])

	return data
