from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    mjpg_proxy_url = os.environ['MJPG_PROXY_URL']   
    return render_template('home.html', mjpg_proxy_url=mjpg_proxy_url)

if __name__ == '__main__':
    app.run(host="0.0.0.0")