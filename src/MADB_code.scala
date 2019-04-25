import sys.process._
"hdfs dfs -rmr MADB" !
"hdfs dfs -rmr recommendation_*" !
"hdfs dfs -mkdir MADB" !
"hdfs dfs -copyFromLocal spotify_files/ MADB/" !
"hdfs dfs -copyFromLocal napster_files/ MADB/" !
"hdfs dfs -copyFromLocal last_fm_files/ MADB/" !  
"hdfs dfs -copyFromLocal user_data.csv MADB/" !

var user_data = scala.io.Source.fromFile("user_data.csv").getLines().map(_.split(",").map(_.trim)).toArray
var userNoHeader = user_data.drop(1)

// Reading the data
var spotify_data = sc.textFile("MADB/spotify_files")
var napster_data = sc.textFile("MADB/napster_files")
var lastfm_data = sc.textFile("MADB/last_fm_files")

// var user_data = sc.textFile("MADB/user_data.csv")
// var userHeader = user_data.first()
// var userNoHeader = user_data.filter(row => row!= userHeader)

spotify_data.take(1)
napster_data.take(1)
lastfm_data.take(1)
userNoHeader.take(1)

var spotify_values= spotify_data.map(line => line.split(","))
var napster_values= napster_data.map(line => line.split(","))
var lastfm_values = lastfm_data.map(line => line.split(","))


//Reading the genre preference for 1 user
// var user_values= userNoHeader.map(line => line.split(","))
// var user_genre = userNoHeader.first().split(",")(3)
// var user_email = userNoHeader.first().split(",")(2)

// var spotify_top2 = spotify_usergenre.keyBy(line => line(4))
// var spotify_final_top2 =spotify_top2.sortByKey(ascending= False)
// var napster_top2 = napster_usergenre.sortBy(line=> line(4).toInt, ascending = false)

//Creating global variable
// var spotify_top : org.apache.spark.rdd.RDD[Array[String]] =sc.emptyRDD
// var napster_top : org.apache.spark.rdd.RDD[Array[String]] =sc.emptyRDD
// var lastfm_top : org.apache.spark.rdd.RDD[Array[String]] =sc.emptyRDD


////Reading the genre preference for all users
for (i <- userNoHeader)
{
val email = i(2) 
println(email)
val user_genre = i(3)
println(user_genre)
val file_name = "recommendation_" + email
//Filter in genre
val spotify_usergenre = spotify_values.filter{ case line => line(5)==user_genre }
val napster_usergenre = napster_values.filter{ case line => line(4)==user_genre }
val lastfm_usergenre = lastfm_values.filter{ case line => line(1)==user_genre }
//Sort of popularity
val spotify_usergenre2 = spotify_usergenre.sortBy(line=> line(4).toInt, ascending = false)
val lastfm_usergenre2 = lastfm_usergenre.sortBy(line=> line(4).toInt, ascending = false)
//Sort
//Take top 4 and save
var spotify_top = sc.parallelize(spotify_usergenre2.take(4)).map( x => ("Spotify ," + x(2).toString + "," + x(1).toString + "," + x(3).toString + "," + x(5).toString )).saveAsTextFile(file_name+"/spotify")
var napster_top = sc.parallelize(napster_usergenre.take(4)).map( x => ("Napster ," + x(2).toString + "," + x(1).toString + "," + x(3).toString + "," + x(4).toString)).saveAsTextFile(file_name+"/napster")
var lastfm_top = sc.parallelize(lastfm_usergenre2.take(4)).map( x => ("LastFm ," + x(3).toString + "," + x(2).toString + "," + x(5).toString + "," + x(1).toString)).saveAsTextFile(file_name+"/lastfm")
// spotify_top2.foreach{ x => { println(x) }}
// spotify_top2.map( x => (x(0).toString +","+ x(1).toString +","+ x(2).toString +","+ x(3).toString +","+ x(4).toString +","+ x(5).toString)).saveAsTextFile(file_name+"/spotify")
// napster_usergenre.map( x => (x(0).toString +","+ x(1).toString +","+ x(2).toString +","+ x(3).toString +","+ x(4).toString )).saveAsTextFile(file_name+"/napster")
// lastfm_top2.map( x => (x(0).toString +","+ x(1).toString +","+ x(2).toString +","+ x(3).toString +","+ x(4).toString )).saveAsTextFile(file_name+"/lastfm")
}

"rm recommendation_aav331@nyu.edu" !
"rm recommendation_ss11485@nyu.edu" !
"rm recommendation_sg5290@nyu.edu" !
"rm recommendation_yp345@nyu.edu" !

"hdfs dfs -getmerge recommendation_aav331@nyu.edu/* recommendation_aav331@nyu.edu" !
"hdfs dfs -getmerge recommendation_ss11485@nyu.edu/* recommendation_ss11485@nyu.edu" !
"hdfs dfs -getmerge recommendation_sg5290@nyu.edu/* recommendation_sg5290@nyu.edu" !
"hdfs dfs -getmerge recommendation_yp345@nyu.edu/* recommendation_yp345@nyu.edu" !


// var spotify_top = spotify_top2.top(2, keyFunc)
// spotify_top.top(2,key = (line=> line.split(",")(4)) )
// spotify_top.take(2)
// napster_top.take(2)
// lastfm_top.take(2)

// spotify_top2.foreach{ x => { 
//     val fw = new FileWriter(file_name, true)
//     try {
//         fw.write(x(0)+","+x(1)+","+x(2)+","+x(3)+","+x(4)+","+x(5))
//     }
//     finally fw.close() 
// }}
