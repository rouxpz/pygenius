import wordsearch
import artists
import songs

#testing search by keyword
term = "twerk"
for item in range(1, 2): #for each page of results returned...
	data = wordsearch.searchWords(item, term)
	l = len(data)
	for i in range(0, l):
		#target.write(i)
		#target.write("\n")
		info = data[i]
		print info


#testing album listing for an artist
record1 = artists.albumList("Pusha T")
l = len(record1)

for i in range(0, l):
	print record1[i]

#testing getting dates for albums
record2 = artists.getDates("Nicki Minaj")
m = len(record2)

for i in range(0, m):
	#if record2[i][1] == "2010":
	print record2[i]
	#break


#testing searching through songs for lyrics
lyrics = songs.searchSong("drake", "worst behavior", "lyrics")
l = len(lyrics)

for i in range(0, l):
	print lyrics[i]


#searching annotations
annotated = songs.searchSong("drake", "started from the bottom")
n = len(annotated)

#print annotated[0]

for i in range(0,10):
	lyric = annotated[i][0]
	link = annotated[i][1]
	#print notes
	if link != "Not annotated":
		note = songs.searchAnnotations(link)
		print lyric + ': ' + note
	else:
		note = "No annotation"
		print lyric + ': \n' + note + '\n'


#grabbing album metadata
metadata = artists.getAlbumData("diddy", "press play")

l = len(metadata)

for i in range(0, l):
	print metadata[i]


#grabbing artist bio
bio = artists.getArtistBio("earl sweatshirt")
print bio
