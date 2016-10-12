from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def seconds():
    time_now = datetime.utcnow()
    second = ((time_now - datetime(1970, 1, 1)).total_seconds())
    second = '{:.2f}'.format(second)
    second = str(second)
    #print millisecond
    #return type(time_delta)
    return second 
    #return "ok!"
if __name__ == "__main__":
    app.run()
