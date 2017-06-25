# pyscdl
Python Soundcloud downloader

You must find a client ID and a track ID to download a song.
Both can be obtained via the developer console. Go to network,
and you can find many XMLHTTPRequests with client_id as a argument.

The track ID can be found in the XMLHTTPRequest URLs.
It looks something like this: https://api.soundcloud.com/v1/track/1923384721/playlist. Where the number is the track ID.

Put any client IDs you find in client_ids file in this 
document, so others can use them and I can potentially
reverse engineer their client_id algorithm

Invoke scdl.py like so: `python scdl.py client_id track_id`
The song will be written to stdout in MPEG ADTS format