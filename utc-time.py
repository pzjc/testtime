from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def milliseconds():
    time_now = datetime.utcnow()
    return str((time_now - datetime(1970, 1, 1)).total_seconds()*1000)

if __name__ == "__main__":
    app.run()
