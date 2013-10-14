from pygenius import artists
from pygenius import songs
from pygenius import wordsearch


###search by keyword###
term = "twerk"
data = wordsearch.searchWords(term)

print data[0] #returns first result


###grab albums for an artist###
records1 = artists.albumList('Pusha T')

for record in records1:
	print record


###getting dates for albums###
records2 = artists.getDates('Nicki Minaj')

for record in records2:
	print record


###searching through songs for just the lyrics###
lyrics = songs.searchSong('lil wayne', 'got money', 'lyrics')

for lyric in lyrics:
	print lyric


###searching through songs for annotations###
annotated = songs.searchSong('drake', 'started from the bottom')
n = len(annotated)

for i in range(0,n):
	lyric = annotated[i][0]
	link = annotated[i][1]

	#print notes
	if link != "Not annotated":
		note = songs.searchAnnotations(link)
		print lyric + ': ' + note
	else:
		note = "No annotation"
		print lyric + ': \n' + note + '\n'


###grabbing album metadata###
metadata = artists.getAlbumData('kanye west', 'yeezus')

l = len(metadata)

for i in range(0, l):
	print metadata[i]


###grabbing artist bio###
bio = artists.getArtistBio('ol dirty bastard')
print bio


###grabbing list of popular songs###
songs = artists.getPopularSongs('lil kim')

for song in songs:
	print song


###listing all songs by an artist###
songs = songs.findAllSongs('Kid Cudi')

for song in songs:
	print song
