import json
import requests

data_points = []


url= "http://ws.audioscrobbler.com/2.0/"
params = {
	"method": "tag.gettoptracks",
	"tag": "disco"
	"api_key": "e86f0e6ebb5cf5776b4276d520ea541e",
	"format": "json"
}
result = requests.get(url, params=params)
print(result.status_code)
print(result.text)
data_points.append(json.loads(result.text))

with open('lastfm_play.json', 'a+') as file:
	file.write(json.dumps(data_points, indent=4, sort_keys=True))
