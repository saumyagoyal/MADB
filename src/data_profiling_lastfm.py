import json
import requests
import pandas as pd

def get_genre_info():
    data_points_tag = []


    url= "http://ws.audioscrobbler.com/2.0/"
    params = {
        "method": "tag.gettoptracks",
        "tag": "rock",
        "api_key": "e86f0e6ebb5cf5776b4276d520ea541e",
        "format": "json"
    }
    result = requests.get(url, params=params)
    data_points_tag.append(json.loads(result.text))

    total_songs = data_points_tag[0]['tracks']['track']
    return total_songs

def get_listeners(song_name):
    data_points = []


    url= "http://ws.audioscrobbler.com/2.0/"
    params = {
        "method": "track.search",
        "track": song_name,
        "api_key": "e86f0e6ebb5cf5776b4276d520ea541e",
        "format": "json"
    }
    result = requests.get(url, params=params)

    data_points.append(json.loads(result.text))
    listeners = data_points[0]['results']['trackmatches']['track'][0]['listeners']
    return listeners


def write_to_csv(data_schema):
    last_fm_df = pd.DataFrame.from_dict(data_schema)
    last_fm_df.to_csv("FM.csv")



total_songs_list = get_genre_info();

data_schema = {}
genre = []
artist = []
song_name = []
playcount = []
url = []

for songs in total_songs:
    genre.append('Rock')
    artist.append(songs['artist']['name'])
    song_name.append(songs['name'])
    playcount.append(get_listeners(songs['name']))
    url.append(songs['url'])

data_schema['Genre'] = genre
data_schema['Artist'] = artist
data_schema['Song'] = song_name
data_schema['Listeners'] = playcount
data_schema['URL'] = url

write_to_csv(data_schema)

print(data_schema)
