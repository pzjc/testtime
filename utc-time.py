from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def milliseconds():
   # time_now = datetime.utcnow()
   # second = ((time_now - datetime(1970, 1, 1)).total_seconds()) * 1000
   # millisecond = '{:.2f}'.format(millisecond)
   # millisecond = str(millisecond)
    #print millisecond
    #return type(time_delta)
   # return millisecond 
    return "ok!"
if __name__ == "__main__":
    app.run()
