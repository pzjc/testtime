from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def milliseconds():
    time_now = datetime.datetime.utcnow()
    return (time_now - datetime.datetime(1970, 1, 1)).total_seconds()*1000
