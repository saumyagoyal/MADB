import json
import requests
import random
import datetime
import csv
import base64
# import spotipy
# spotify = spotipy.Spotify()

class Spotify_Tracks:
	def __init__(self):
		self.id = ""
		self.artist_name = ""
		self.track_name = ""
		self.track_url = ""
		self.popularity = ""
		self.genre = ""

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

# Data Schema
# id, artist_name, track_name, track_url, popularity, genre


def get_access_key():
	url = "https://accounts.spotify.com/api/token"
	client_id = "bc66b8532c394a5cb916de445e2ba45b"
	client_secret = "14d1aa898da940f2b06947620e366578"
	auth_str = bytes('{}:{}'.format(client_id, client_secret), 'utf-8')
	b64_auth_str = base64.b64encode(auth_str).decode('utf-8')
	# authorization = base64.standard_b64encode(('Basic ' + client_id + ":" + client_secret).encode())

	headers = {
		'Authorization' : 'Basic ' + b64_auth_str
	}

	data = {
		'grant_type' : 'client_credentials'
	}

	auth = requests.post(url=url,headers=headers,data=data)
	print(auth.text)
	authdata = json.loads(auth.text)
	return authdata["access_token"]

token = get_access_key()
today = datetime.datetime.now()
parameters = {"country" : "US"}

# For Genres
url1 = "https://api.spotify.com/v1/browse/categories"
result1 = requests.get(url1, headers={'Authorization': 'Bearer %s' % token}, params=parameters)
val1 = json.loads(result1.text)
# print (val1["categories"]["items"])

genre_list_id  = []
for i in val1["categories"]["items"]:
	genre_list_id.append(i["id"])
	# print(i["name"])

genre_list_common=["pop", "classical", "rock", "jazz", "hiphop", "edm_dance", "soul", "metal"]
genre_list_name= ["Pop", "Classical", "Rock", "Jazz", "Hip-Hop", "Electronic", "Soul", "Metal"]

# For getting playlist based on genre
for k in range(0, len(genre_list_common)):
	url2= "https://api.spotify.com/v1/browse/categories/" + genre_list_common[k] + "/playlists"
	result2 = requests.get(url2, headers={'Authorization': 'Bearer %s' % token}, params = parameters)
	print(genre_list_name[k])
	# print (result2.status_code)
	val2 = json.loads(result2.text)

	playlist_id=[]
	for j in val2["playlists"]["items"]:
		# print(j["id"])
		playlist_id.append(j["id"])

	# Taking top three playlists all tracks
	for x in range(0,3):
		p = playlist_id[x]
		print(p)
		url= "https://api.spotify.com/v1/playlists/" + p + "/tracks"
		result = requests.get(url, headers={'Authorization': 'Bearer %s' % token}, params = parameters)
		print (result.status_code)
		val = json.loads(result.text)
		tcount = 1
		spotify_track_list = []

		for i in val["items"]:
			# print (i["track"]["name"])
			# print (i["track"]["popularity"])
			# print (i["track"]["external_urls"]["spotify"])
			# print (i["track"]["album"]["artists"][0]["name"])			
			# print (i["track"]["album"]["artists"])
			if i["track"]==None:
				continue
			spot = Spotify_Tracks()
			spot.id = str(today) + "_" + str(tcount)
			spot.artist_name = i["track"]["album"]["artists"][0]["name"]
			spot.track_name = i["track"]["name"]
			spot.track_url = i["track"]["external_urls"]["spotify"]
			spot.popularity = i["track"]["popularity"]
			spot.genre = genre_list_name[k]
			spotify_track_list.append(spot.__dict__)
			tcount += 1
			file_name="spotify_play_"+str(datetime.date.today())+".csv"
			with open(file_name, 'a', newline='') as file:
				fieldnames = ['id', 'artist_name', 'track_name', 'track_url', 'popularity', 'genre']
				writer = csv.DictWriter(file, fieldnames=fieldnames)
				# writer.writeheader()
				writer.writerow({'id': spot.id, 'artist_name': spot.artist_name, 'track_name': spot.track_name,
				                 'track_url': spot.track_url, 'popularity':spot.popularity, 'genre':spot.genre})





