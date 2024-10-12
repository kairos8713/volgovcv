from flask import Flask,render_template,redirect,url_for,request
import requests

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.app_context().push()
@app.route("/")
def main():
	return render_template("main.html")
@app.route("/resume")
def resume():
	return render_template("resume.html")
@app.route("/contact")
def contact():
	return render_template("contact.html",pop1="apop",apopp1="apopp")
@app.route("/objective")
def objective():
	return render_template("objective.html")
@app.route("/send",methods = ["POST"])
def send():
	name = request.form.get("name")
	email = request.form.get("email")
	subject = request.form.get("subject")
	text = request.form.get("text")
	if len(name) > 0:
		if len(email) > 0:
			if len(subject) > 0:
				if len(text) > 0:
					text = text + "\n\n\ngöndereninin ismi:{} ve e-postası:{}".format(name,email)
					#semail(subject,text)
	return redirect(url_for("contact",pop1 = "apop",apopp1="pop_progress"))
def semail(subject,text):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox062bdaf2592a4fddac332fdeb86521db.mailgun.org/messages",
		auth=("api", "a8f5e65b09b65c38fed261bc7379a996-408f32f3-6039a1b0"),
		data={"from": "<mailgun@sandbox062bdaf2592a4fddac332fdeb86521db.mailgun.org>",
			"to": ["georgii.volgov@icloud.com"],
			"subject": str(subject),
			"text": str(text)})

if __name__ == "__main__":
	app.run(debug=True)