# import spotipy
# spotify = spotipy.Spotify()
# name= "Drake"

import json
# import spotipy
import requests
import random
import datetime
import csv

class Spotify_Track:
	def __init__(self):
		self.id = ""
		self.artist_name = ""
		self.track_name = ""
		self.track_url = ""
		self.popularity = ""

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
# auth_key='BQBkt5GvvtxIomiHtfqjCQnw-JlhE56Jlpt77ReLZRpwB2e8cT6_omn9cvJRtgz4cFpeRIAydBXhORCDYXxbdvmtGpV0lTd_krFuyeymYVYHw2NdOqhvM0RPXNf5CIQpIWNJCJLkOB3c6K7JHoiragAwmkOhQ-8yIQ'
data_points = []


url= "https://api.spotify.com/v1/playlists/37i9dQZEVXbLRQDuF5jeBp/tracks"
# parameters = dict(q='transfer AND football AND ' + cname, from_parameter="2017-12-01", to="2018-01-31",language='en', pageSize=10, page=1,apiKey="d3e56214150b4ef6821131c9ef777faa")
auth_key='BQDAP3FqoKjl8aHl-05lTX-czuQn4uWmw6zRoUGxcdgeEigGeVAYeQxBTpg6o5uLoKJvSC4w_J1mxmlSTjhsvkBODPBeBZYOuiJBzN8vIbvq59FN0NX_KDbhmsbintDqd_bHrl5ESmi-F_G364jjsdNJcoQxpXSRbMo-XlBJ_SMpYzRT7kR_sQmNnPE'
result = requests.get(url, headers={'Authorization': 'Bearer %s' % auth_key})#, params=parameters)
print (result.status_code)
val = json.loads(result.text)
# print val["items"]

tcount = 1
today = datetime.datetime.now()
for i in val["items"]:
	# print (i["track"]["name"])
	# print (i["track"]["popularity"])
	# print (i["track"]["external_urls"]["spotify"])
	# print (i["track"]["album"]["artists"][0]["name"])
	spot = Spotify_Track()
	spot.artist_name = i["track"]["album"]["artists"][0]["name"]
	spot.id = str(today) + "_" + str(tcount)
	spot.track_name = i["track"]["name"]
	spot.track_url = i["track"]["external_urls"]["spotify"]
	spot.popularity = i["track"]["popularity"]
	data_points.append(spot.__dict__)
	tcount+=1
	with open('spotify_play.csv', 'a', newline='') as file:
		fieldnames = ['id', 'artist_name', 'track_name', 'track_url', 'popularity']
		writer = csv.DictWriter(file, fieldnames=fieldnames)
		# writer.writeheader()
		writer.writerow({'id': spot.id, 'artist_name': spot.artist_name, 'track_name': spot.track_name,
		                 'track_url': spot.track_url, 'popularity':spot.popularity})


# For Genres
url1 = "https://api.spotify.com/v1/browse/categories"
result1 = requests.get(url1, headers={'Authorization': 'Bearer %s' % auth_key})#, params=parameters)
val1 = json.loads(result1.text)
# print (val1["categories"]["items"])

for i in val1["categories"]["items"]:
	print(i["id"])
	print(i["name"])

