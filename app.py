from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello peoples'

@app.route("/hehehe")
def spongebob_gif():
    return send_from_directory("static", "spongebob.mp4")
