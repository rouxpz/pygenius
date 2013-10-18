# PyGenius

Want to use data from rap songs in your Python scripts but bummed that there's no API to do so?  
Well guess what?  NOW U CAN, DAWG.

Welcome to PyGenius.

All functions should be run through the examples.py file, or any other script you create.

##Installation

`pip install pygenius`  
`easy_install pygenius`

If you download the source from here, please make sure you have BeautifulSoup installed (`pip install beautifulsoup4`).

###To import the library

At the top of your script, include the following:

`from pygenius import artists, songs, wordsearch`


###Functions currently available
**artists.albumList(artist, arg)**  
Returns a list of albums that the specified artist has recorded.
If second argument is set as 'links', the links to the albums will be returned.

**artists.getDates(artist)**  
Returns a list of albums recorded by a specific artist, as well as the release year.

**artists.getAlbumData(artist, album)**  
Returns the metadata about an album: description, track numbers, and track names.

**artists.getArtistBio(artist)**  
Returns an artist's bio.

**artists.getPopularSongs(artist, arg)**  
Returns the most popular songs by a specified artist.  If the optional second argument is 'link', will return links to songs that can be passed in to other functions.

**wordsearch.searchWords(keyword, arg)**  
Returns results for a key word search.  Default return is artist and song name, but if the optional second argument is set to 'link', a link to the song is returned.

**songs.searchSong(artist, title, arg)**  
Returns lyrics for a specified song title.  If the optional third argument is set to 'lyrics', only the lyrics will be returned; if it's 'link', only links to each lyric's annotations are returned (and can be passed into the searchAnnotations function); otherwise, both are returned by default.

**songs.searchAnnotations(query)**  
Will return content of a specified annotation link, including HTML links to pictures, videos and GIFs, as well as links to external sites referenced.

**songs.findAllSongs(artist, arg)**  
Will return all songs attributed to the specified artist.  If second argument is specified as 'links', will return the links to the songs; if 'titles', will return the song titles; otherwise, will return both by default.


###---###

Thanks to David Rios for inspiration.
