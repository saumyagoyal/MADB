import json
import requests

data_points = []


url= "http://api.napster.com/v2.2/playlists/top"
params = {
	"apikey" : "YTkxZTRhNzAtODdlNy00ZjMzLTg0MWItOTc0NmZmNjU4Yzk4"
}
result = requests.get(url, params=params)#, params=parameters)
print(result.status_code)
data_points.append(json.loads(result.text))

with open('napster_play.json', 'a+') as file:
	file.write(json.dumps(data_points, indent=4, sort_keys=True))