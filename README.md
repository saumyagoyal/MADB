# MADB
Big Data Project

Client ID bc66b8532c394a5cb916de445e2ba45b  
Client Secret 14d1aa898da940f2b06947620e366578

# Flask API for User Registration 
The following steps need to be performed:
* Download Python 3
* Download Flask module - pip install flask
* Download WTForms module - pip install wtforms

## Running Flask API
* Go to command line and type python user_data.py
* Once the server is running successfully, go to browser and type http://localhost:5000
* Genre is populated using the Napster Genre API call
* Enter all details on the registration page and hit Submit
* If success message shown, go to user_data.csv and verify

## Sample User Data
id,name,email,genre
ss11485@nyu.edu,Saurabh,ss11485@nyu.edu,Rock
smc324@nyu.edu,Suzanne,smc324@nyu.edu,Soul/R&B
hp17@nyu.edu,Harry,hp17@nyu.edu,Jazz

# Napster Data

## Napster Data Schema
* ID - DateTime.now() appended with song number
* Artist Name
* Track Name
* Track URL
* Genre

## Napster Code
* The Python code uses the Napster Public API - 
e.g. 
url= "http://api.napster.com/v2.2/genres/g.397/tracks/top"
params = {
	"apikey" : "xxx",
	"limit": 10
}
* Data is stored and appended to a CSV File called napster_play.csv

## Napster Data CSV
* Data is stored in a CSV format using the data scheme given above. For example,
id,artist_name,track_name,track_url,genre
2019-04-12 11:43:12.109128_1,Billie Eilish,bad guy,https://listen.hs.llnwd.net/g3/3/6/7/2/7/1496172763.mp3,Alternative
