# import spotipy
# spotify = spotipy.Spotify()
# name= "Drake"

import json
# import spotipy
import requests
import random
import datetime
import csv

# from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data
# client_id = "bc66b8532c394a5cb916de445e2ba45b"
# client_secret = "14d1aa898da940f2b06947620e366578"
# client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

# For Artist
# name = "Drake" #chosen artist
# result = sp.search(q='artist:' + name, type='artist')
# result['tracks']['items'][0]['artists']
# For Playlist
# result = sp.search(q='United States Top 50', type='playlist')

# For Multiple Playlits---------
	# playlist_id=['37i9dQZEVXbLRQDuF5jeBp','37i9dQZEVXbKuaTI1Z1Afx']
	# auth_key='BQBkt5GvvtxIomiHtfqjCQnw-JlhE56Jlpt77ReLZRpwB2e8cT6_omn9cvJRtgz4cFpeRIAydBXhORCDYXxbdvmtGpV0lTd_krFuyeymYVYHw2NdOqhvM0RPXNf5CIQpIWNJCJLkOB3c6K7JHoiragAwmkOhQ-8yIQ'
	# data_points = []

	# for i in playlist_id:
	# 	url= "https://api.spotify.com/v1/playlists/"+i+"/tracks"
	# 	# parameters = dict(q='transfer AND football AND ' + cname, from_parameter="2017-12-01", to="2018-01-31",language='en', pageSize=10, page=1,apiKey="d3e56214150b4ef6821131c9ef777faa")
	# 	auth_key='BQBkt5GvvtxIomiHtfqjCQnw-JlhE56Jlpt77ReLZRpwB2e8cT6_omn9cvJRtgz4cFpeRIAydBXhORCDYXxbdvmtGpV0lTd_krFuyeymYVYHw2NdOqhvM0RPXNf5CIQpIWNJCJLkOB3c6K7JHoiragAwmkOhQ-8yIQ'
	# 	result = requests.get(url, headers={'Authorization': 'Bearer %s' % auth_key})#, params=parameters)
	# 	print (result.status_code)
	# 	data_points.append(json.loads(result.text))

	# with open('spotify_play.json', 'a+') as file:
	# 		file.write(json.dumps(data_points, indent=4, sort_keys=True))
# -------
# Source, Artist_id, artist_name, track_id, track_name, popularity_of_track

# For One playlist
playlist_id='37i9dQZEVXbLRQDuF5jeBp'
auth_key='BQBkt5GvvtxIomiHtfqjCQnw-JlhE56Jlpt77ReLZRpwB2e8cT6_omn9cvJRtgz4cFpeRIAydBXhORCDYXxbdvmtGpV0lTd_krFuyeymYVYHw2NdOqhvM0RPXNf5CIQpIWNJCJLkOB3c6K7JHoiragAwmkOhQ-8yIQ'
data_points = []


url= "https://api.spotify.com/v1/playlists/37i9dQZEVXbLRQDuF5jeBp/tracks"
# parameters = dict(q='transfer AND football AND ' + cname, from_parameter="2017-12-01", to="2018-01-31",language='en', pageSize=10, page=1,apiKey="d3e56214150b4ef6821131c9ef777faa")
auth_key='BQA1oavr699iukLhxmw-IX_WDa5nJHbApWE4VGygJ9a__QQKuzHLslMnzF9NUWNqiusaWxsbZNMZXxP9XxmMoPu1MBHegFTcr-ftuiPyxtCSLuCztDGWqAvGmHX6T43Ws9_jooMzmNYEG_vO'
result = requests.get(url, headers={'Authorization': 'Bearer %s' % auth_key})#, params=parameters)
print (result.status_code)
val1 = json.loads(result.text)
print val1["items"]["track"]
	# data_points.append(json.loads(result.text))

with open('spotify_play.json', 'a+') as file:
		file.write(json.dumps(val1, indent=4, sort_keys=True))
