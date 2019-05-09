from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField
import requests
import json
import csv

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
genres = []

url= "http://api.napster.com/v2.2/genres"
params = {
	"apikey" : "YTkxZTRhNzAtODdlNy00ZjMzLTg0MWItOTc0NmZmNjU4Yzk4"
}
choices = [("0","--Select--"),("1","Pop"),("2","Classical"),("3","Rock"),("4","Jazz"),("5","Hip-Hop"),("6","Electronic")
	,("7","Soul"),("8","Metal")]

print(choices)

class ReusableForm(Form):
	name = TextField('Name:', validators=[validators.required()])
	email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
	genre = SelectField('Genre:', choices=choices)

class User:

	def __init__(self):
		self.id = ""
		self.name = ""
		self.email = ""
		self.genre = ""

user_data = []

try:
	with open("user_data.csv", mode="r") as file:
		if(sum(1 for line in file) == 0):
			print("Empty file")
		else:
			csv_reader = csv.DictReader(file, delimiter=',')
			line_count = 0
			for row in csv_reader:
				if line_count == 0:
					print(f'Column names are {", ".join(row)}')
					user_data.append((",".join(row)))
					line_count += 1
				else:
					# print(f'\t{row["n"]} works in the {row[1]} department, and was born in {row[2]}.')
					user_data.append((row["id"],row["name"],row["email"],row["genre"]))
					line_count += 1
except Exception as e:
	print(e)

print(user_data)

@app.route("/", methods=['GET', 'POST'])
def hello():
	form = ReusableForm(request.form)
	print(form.errors)
	u = User()
	print(user_data)
	if request.method == 'POST':
		u.id = request.form['email']
		u.name = request.form['name']
		u.genre = request.form["genre"]
		u.email = request.form['email']
		# print (name, " ", email, " ", genre)
		with open('user_data.csv', mode='a', newline='') as csv_file:
			fieldnames = ['id', 'name', 'email', 'genre']
			writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
			# writer.writeheader()
			writer.writerow({'id': u.id, 'name': u.name, 'email': u.email, 'genre': u.genre})
			flash('Thanks for registration ' + u.name)

	if form.validate() == False:
		flash('Error: All the form fields are required. ')

	return render_template('Register.html', form=form)

if __name__ == "__main__":
	app.run(debug=False, use_reloader=False)