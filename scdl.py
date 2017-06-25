import sys
import requests
import os

def main():
	if len(sys.argv) != 3:
		sys.stderr.write(sys.argv[0] + " client_id track_id\n")
		return 1
	user_agent = "Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0"
	app_version = 1498223919
	client_id = sys.argv[1]
	track_id = sys.argv[2]
	stream_headers = {
		"Referer" : "https://api.soundcloud.com/",
		"Origin" : "https://soundcloud.com",
		"User-Agent" : user_agent
	}
	stream_params = {
		"client_id" : client_id,
		"app_version" : app_version
	}
	streams = requests.get("https://api.soundcloud.com/i1/tracks/" + str(track_id) + "/streams",headers=stream_headers,params=stream_params)
	if streams.status_code == 401:
		sys.stderr.write("401 Unauthorized - invalid client ID\n")
		return 2
	if streams.status_code == 404:
		sys.stderr.write("404 Not Found - invalid track ID\n")
		return 3
	if streams.status_code != 200:
		sys.stderr.write("Unknown error occurred in request for track URLs,dumping request\n")
		sys.stderr.write("GET " + streams.url + "\n")
		sys.stderr.write("JSON is as follows:\n")
		sys.stderr.write(streams.text + "\n")
		return 4
	#sys.stderr.write("GET " + streams.url + " " + str(streams.status_code) + "\n")
	playlist_headers = {
		"Referer" : "https://cf-hls-media.sndcdn.com/",
		"Origin" : "https://soundcloud.com",
		"User-Agent" : user_agent
	}
	playlist = requests.get(streams.json()["http_mp3_128_url"],headers=playlist_headers,stream=True)
	#sys.stderr.write("GET " + playlist.url + " " + str(streams.status_code) + "\n")
	sys.stdout.buffer.write(playlist.raw.read())

if __name__ == "__main__":
	try:
		sys.exit(main())
	except KeyboardInterrupt:
		sys.exit(1)