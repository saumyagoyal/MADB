import smtplib, ssl
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv

RecSongs = []

receiver_emails = {}  # Enter receiver address

for root, dirs, files in os.walk("C:\\Users\\Saurabh Sharan\\Documents\\MADB"):
	for file in files:
		if file.startswith("recommendation_"):
			receiver_emails[os.path.join(root, file)] = ""
			email = file.replace(".csv", "").split("_")[1]
			receiver_emails[os.path.join(root, file)]=email

print(receiver_emails)

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "MusicAggregatorDB@gmail.com"  # Enter your address

password = input("Type your password and press enter: ")

context = ssl.create_default_context()
for receipient in receiver_emails.keys():

	# if receiver_emails[receipient] != "ss11485@nyu.edu":
	# 	continue

	person_name = ""

	message = MIMEMultipart("html")
	message["Subject"] = "Your Latest Recommendations!"
	message["From"] = sender_email
	message["To"] = receiver_emails[receipient]

	with open("user_data.csv", mode="r") as file:
		csv_reader = csv.reader(file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				line_count += 1
				continue
			else:
				if receiver_emails[receipient] == row[2]:
					person_name = row[1]
					break
				line_count += 1

	with open(receipient, mode='r') as file:
		csv_reader = csv.reader(file, delimiter=',')
		line_count = 0
		RecSongs = []
		lines = [0,1,4,5,8,9]
		for row in csv_reader:
			if line_count not in lines:
				line_count += 1
				continue
			url = row[3]
			RecSongs.append(row[1]+","+row[0]+","+row[2]+","+url)
			line_count += 1

	print(RecSongs)

	# Create the plain-text and HTML version of your message
	song1 = RecSongs[0].split(",")
	song2 = RecSongs[1].split(",")
	song3 = RecSongs[2].split(",")
	song4 = RecSongs[3].split(",")
	song5 = RecSongs[4].split(",")
	song6 = RecSongs[5].split(",")
	html = """\
	<html>
	  <body>
	    <p style="color: red">Hi """ + person_name + """,<br><br>
	       Your MADB recommendations are waiting to be discovered!<br><br> 
	       Click on the source links to go to track!<br><br>
	    </p>
	    <table style="width:100%">
		  <tr>
		    <th style="text-align: left; display:none;">Track Name</th>
		    <th style="text-align: left; display:none;">Artist Name</th>
		    <th style="text-align: left; display:none;">Go to Track</th>
		  </tr>
		  <tr>
		    <td><strong>""" + song1[0] + """</strong></td>
		    <td><strong>""" + song1[2] + """</strong></td>
		    <td><a href=""" + song1[3] + """/><img src="https://cdn0.iconfinder.com/data/icons/social-flat-rounded-rects/512/lastfm-512.png"
		     style="width:42px;height:42px;border:0;"></td>
		  </tr>
		  <tr>
		    <td><strong>""" + song2[0] + """</strong></td>
		    <td><strong>""" + song2[2] + """</strong></td>
		    <td><a href=""" + song2[3] + """/><img src="https://cdn0.iconfinder.com/data/icons/social-flat-rounded-rects/512/lastfm-512.png"
		     style="width:42px;height:42px;border:0;"></td>
		  </tr>
		  <tr>
		    <td><strong>""" + song3[0] + """</strong></td>
		    <td><strong>""" + song3[2] + """</strong></td>
		    <td><a href=""" + song3[3] + """/><img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/fa577965-5d99-4132-8fe4-0de190bb01ad/d5ugjxf-42061c12-ca6b-4871-995f-e7b508f6f304.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2ZhNTc3OTY1LTVkOTktNDEzMi04ZmU0LTBkZTE5MGJiMDFhZFwvZDV1Z2p4Zi00MjA2MWMxMi1jYTZiLTQ4NzEtOTk1Zi1lN2I1MDhmNmYzMDQucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.7W_FC_FPGbQ_CQ5a4qNvGfuEaQbJTFOnyG-1F0FT6tk" 
		    style="width:42px;height:42px;border:0;"></td>
		  </tr>
		  <tr>
		    <td><strong>""" + song4[0] + """</strong></td>
		    <td><strong>""" + song4[2] + """</strong></td>
		    <td><a href=""" + song4[3] + """/><img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/fa577965-5d99-4132-8fe4-0de190bb01ad/d5ugjxf-42061c12-ca6b-4871-995f-e7b508f6f304.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2ZhNTc3OTY1LTVkOTktNDEzMi04ZmU0LTBkZTE5MGJiMDFhZFwvZDV1Z2p4Zi00MjA2MWMxMi1jYTZiLTQ4NzEtOTk1Zi1lN2I1MDhmNmYzMDQucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.7W_FC_FPGbQ_CQ5a4qNvGfuEaQbJTFOnyG-1F0FT6tk"
		     style="width:42px;height:42px;border:0;"></td>
		  </tr>
		  <tr>
		    <td><strong>""" + song5[0] + """</strong></td>
		    <td><strong>""" + song5[2] + """</strong></td>
		    <td><a href=""" + song5[3] + """/><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/1024px-Spotify_logo_without_text.svg.png"
		     style="width:42px;height:42px;border:0;"></td>
		  </tr>
		  <tr>
		    <td><strong>""" + song6[0] + """</strong></td>
		    <td><strong>""" + song6[2] + """</strong></td>
		    <td><a href=""" + song6[3] + """/><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/1024px-Spotify_logo_without_text.svg.png"
		     style="width:42px;height:42px;border:0;"></td>
		  </tr>
		</table>
	  </body>
	</html>
	"""

	# Turn these into plain/html MIMEText objects
	part2 = MIMEText(html, "html")
	# Add HTML/plain-text parts to MIMEMultipart messageT
	# The email client will try to render the last part first
	message.attach(part2)

	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_emails[receipient],message.as_string())
		print("Done")
