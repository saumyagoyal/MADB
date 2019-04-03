import applemusicpy
import requests
import json

data_points = []
result = requests.get('https://itunes.apple.com/search?term=guns+and+roses&limit=1')
print (result.status_code)
data_points.append(json.loads(result.text))

with open('apple_play.json', 'a+') as file:
		file.write(json.dumps(data_points, indent=4, sort_keys=True))
# https://api.music.apple.com/v1/catalog/{storefront}/genres/{id}
# secret_key = 'x'
# key_id = 'y'
# team_id = 'z'

# am = applemusicpy.AppleMusic(secret_key=secret_key, key_id=key_id, team_id=team_id)
# results = am.search('travis scott', types=['albums'], limit=5)
# for item in results['results']['albums']['data']:
#     print(item['attributes']['name'])