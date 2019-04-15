import json
import requests
import random
import datetime
import csv
import base64

# -------
# Source, Artist_id, artist_name, track_id, track_name, popularity_of_track

# For One playlist
playlist_id='37i9dQZEVXbLRQDuF5jeBp'
data_points = []


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
print(token)


url = "https://api.spotify.com/v1/playlists/37i9dQZEVXbLRQDuF5jeBp/tracks"
result = requests.get(url, headers={'Authorization': 'Bearer %s' % token})
print(result.status_code)
val1 = json.loads(result.text)
print(val1["items"])

with open('spotify_play.json', 'a+') as file:
		file.write(json.dumps(val1, indent=4, sort_keys=True))
