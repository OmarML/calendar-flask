from __future__ import print_function
import httplib2
import os
import sys
import json
from flask import render_template,Flask,redirect
from oauth2client import client

app=Flask(__name__)
flow = client.flow_from_clientsecrets(
'client_secret_web.json',
scope='https://www.googleapis.com/auth/calendar',
redirect_uri='http://localhost:8080/loggedin')
flow.user_agent="Winning Student"

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload_file():
    auth_uri = flow.step1_get_authorize_url()
    return redirect(auth_uri)
@app.route('/loggedin', methods=['GET','POST'])
def logged_in():
    return "Hello"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
