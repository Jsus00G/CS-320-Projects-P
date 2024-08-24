import flask # requires installation if not already installed - pip3 install flask
import time


app = flask.Flask("my application") # name of the web application can be anything

major_counts = {}
last_visit = 0 # TODO: dict of visit times, for each IP

# TODO: create a slow page
# GOAL: don't let people visit this more often than once per 3s
# flask.request.remote_addr: enables us to take action based on the IP address from
#                            which we receive the request

# TODO: write code for creating a page for time.html
# TEMPLATE semi-static / semi-dynamic
@app.route("/time.html")
def clock():
    with open("time.html") as f:
        s = f.read()
    s = s.replace("REPLACE_ME", str(time.time()))
    return s

# TODO: create a dynamic page ha.html
# DYNAMIC
@app.route("/ha.html")
def laugh():
    return "ha "*1000

# STATIC
# @ operator is called a "decorator"
@app.route("/")
def home():
    with open("index.html") as f:
        html = f.read()
        
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, threaded=False)

# app.run never returns, so don't define functions
# after this (the def lines will never be reached)
