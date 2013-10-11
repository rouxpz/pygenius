# PyGenius: a Python Rap Genius Module

Want to use data from [Rap Genius](http://rapgenius.com) in your Python scripts but bummed that they don't have an actual API?  

Well guess what?  NOW U CAN, DAWG.

Welcome to PyGenius -- the Python Rap Genius scraper.

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

**wordsearch.searchWords(page, keyword, arg)**
Returns results for a key word search, for the specified number of pages.  Default return is artist and song name, but if the optional third argument is set to 'link', a link to the song is returned.

**songs.searchSong(artist, title, arg)**
Returns lyrics for a specified song title.  If the optional third argument is set to 'lyrics', only the lyrics will be returned; if it's 'annotations', only links to each lyric's annotations are returned (and can be passed into the searchAnnotations function); otherwise, both are returned by default.

**songs.searchAnnotations(query)**
Will return content of a specified annotation link, including HTML links to pictures, videos and GIFs, as well as links to external sites referenced.

Thanks to David Rios for inspiration.
