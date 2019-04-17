import json
import requests
import pandas as pd

def get_genre_info(genre):
    data_points_tag = []

    url= "http://ws.audioscrobbler.com/2.0/"
    params = {
        "method": "tag.gettoptracks",
        "tag": genre,
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

def get_dict(total_songs, tag):
    data_schema = {}
    genre = []
    artist = []
    song_name = []
    playcount = []
    url = []
    index = []
    tcount = 1


    for songs in total_songs:
        genre.append(tag)
        artist.append(songs['artist']['name'])
        song_name.append(songs['name'])
        playcount.append(get_listeners(songs['name']))
        url.append(songs['url'])
        ind = str(datetime.datetime.now()) + "_" + str(tcount)
        index.append(ind)
        tcount += 1

    data_schema['Id'] = index
    data_schema['Genre'] = genre
    data_schema['Artist'] = artist
    data_schema['Song'] = song_name
    data_schema['Listeners'] = playcount
    data_schema['URL'] = url
    return data_schema


def write_to_df(data_schema):
    last_fm_df = pd.DataFrame.from_dict(data_schema)
    last_fm_df.set_index('Id', inplace = True)
    return last_fm_df

def write_to_csv(df):
    ind = str(datetime.datetime.now()).split()
    df.to_csv("FM_%s.csv" %ind[0])


tags = ['pop', 'classical', 'rock', 'jazz', 'rap', 'electronic', 'soul', 'metal']
append_list = []

for tag in tags:
    total_songs_list = get_genre_info(tag);
    final_dict = get_dict(total_songs_list, tag)
    df = write_to_df(final_dict)
    append_list.append(df)

final_frame = pd.concat(append_list, axis=0)
write_to_csv(final_frame)
