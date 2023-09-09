from flask import Flask, render_template

app = Flask(__name__)

jobs = [
{
  "id": 1,
  "title": "Full Stack Developer",
  "Salary": "$500000",
  "Location": "Remote"
},
{

  "id": 2,
  "title": "Devops Developer",
  "Salary": "$500000",
  "Location": "Remote"
},
{

"id": 1,
  "title": "Fultter",
  "Salary": "$500000",
  "Location": "Remote"
}
]
@app.route("/")
def learing():
  return render_template('home.html', jobs=jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)