from ast import Tuple
import html
import json
from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

# function to fetch hostname and IP address of incoming request
def fetch_details() -> Tuple:
    hostName = socket.gethostname()
    hostIP = socket.gethostbyname(hostName)
    return str(hostName), str(hostIP)

@app.route("/", methods = ['GET'])
def hello_world() -> html:
    return "<p> HELLO FROM THE APP BY BHARATH @thebharathkumar </p>"

@app.route("/health")
def health() -> json:
    return jsonify(
        status = "UP"
    )

@app.route("/details")
def details() -> html:
    host, ip = fetch_details()
    return render_template('index.html', hostname = host, IP = ip)

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 5000)