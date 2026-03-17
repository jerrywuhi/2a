from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    return "歡迎來到!"


@app.route("/")
def index():
	link = "<h1>歡迎來到吳冠頡的網站</h1>"
	link +="<a href=/mis>課程</a><hr>"
	link +="<a href=/today>今天日期</a><hr>"
    return ink    

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>" 

      
@app.route("/today")
def today():
	now = datetime.now()
	year = str(now.year)
	month = str(now.month)
	day = str(now.day)
	now = year + "/" + month + "/" + day   
	return render_template("today.html", datetime = now)

if __name__ == "__main__":
    app.run(debug=True)