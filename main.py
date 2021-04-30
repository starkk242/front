from flask import Flask, render_template,request
import hashlib

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("landing.html")

@app.route('/login_page')
def login_page():
	return render_template("login.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)