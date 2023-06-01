from flask import Flask, render_template
import json
import urllib.request as request
import ssl
from flask_cors import CORS

app = Flask(__name__)
core = CORS(app)

api_key = "9b153f4e40437e115298166e6c1b997c"
base_url = "https://api.tmdb.org/3/discover/movie/?api_key="+api_key
# api_key = "0d4788fe34d08fa85c275fec31e7a8ea"
# base_url = "https://api.themoviedb.org/3/movie/550?api_key="+api_key
#ssl._create_default_https_context = ssl._create_unverified_context
#conn = request.urlopen(base_url)
#json_data = json.loads(conn.read())
@app.route("/")
def home():
    return render_template("index1.html")

@app.route('/login', methods=["GET"], strict_slashes=False)
def login():
    print("login page")
    return render_template('login.html')

@app.route('/sign_up', methods=["GET"], strict_slashes=False)
def sign_up():
    return render_template('signUp.html')

if __name__=="__main__":
    app.run(debug=True)
