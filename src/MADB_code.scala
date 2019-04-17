// hdfs dfs -rmr MADB
// hdfs dfs -mkdir MADB 
// hdfs dfs -copyFromLocal spotify_files/ MADB/    
// hdfs dfs -copyFromLocal napster_files/ MADB/ 
// hdfs dfs -copyFromLocal last_fm_files/ MADB/      
// hdfs dfs -copyFromLocal user_data.csv MADB/ 

// Reading the data
var spotify_data = sc.textFile("MADB/spotify_files")
var napster_data = sc.textFile("MADB/napster_files")
var lastfm_data = sc.textFile("MADB/last_fm_files")

var user_data = sc.textFile("MADB/user_data.csv")

spotify_data.take(1)
napster_data.take(1)
lastfm_data.take(1)
user_data.take(1)

var userHeader = user_data.first()
var userNoHeader = user_data.filter(row => row!= userHeader)

var spotify_values= spotify_data.map(line => line.split(","))
var napster_values= napster_data.map(line => line.split(","))
var lastfm_values = lastfm_data.map(line => line.split(","))
var user_values= userNoHeader.map(line => line.split(","))

//Reading the genre preference for 1 user
var user_genre = userNoHeader.first().split(",")(3)
var user_email = userNoHeader.first().split(",")(2)

var spotify_usergenre= spotify_values.filter{ case line => line(5)==user_genre }
var napster_usergenre= napster_values.filter{ case line => line(4)==user_genre }
var lastfm_usergenre= lastfm_values.filter{ case line => line(1)==user_genre }

// var spotify_top2 = spotify_usergenre.keyBy(line => line(4))
// var spotify_final_top2 =spotify_top2.sortByKey(ascending= False)

var spotify_top2 = spotify_usergenre.sortBy(line=> line(4).toInt, ascending = false)
// var napster_top2 = napster_usergenre.sortBy(line=> line(4).toInt, ascending = false)
var lastfm_top2 = lastfm_usergenre.sortBy(line=> line(4).toInt, ascending = false)

spotify_top2.take(2)
napster_usergenre.take(2)
lastfm_top2.take(2)
