from __future__ import print_function
import httplib2
import os
import sys
import json
from flask import (render_template,Flask,
        redirect,request,url_for,session)
from apiclient import discovery
from oauth2client import client
try:
        # For Python 3.0 and later
            from urllib.request import urlopen
except ImportError:
        # Fall back to Python 2's urllib2
            from urllib2 import urlopen

app=Flask(__name__)
app.config['SECRET_KEY'] = "123456"
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
    session['url']=(request.form['jsonurl'])
    auth_uri = flow.step1_get_authorize_url()
    return redirect(auth_uri)
@app.route('/loggedin', methods=['GET','POST'])
def logged_in():
    if 'code' not in request.args:
        return "Bad Request"
    auth_code = (request.args.get('code'))
    credentials = flow.step2_exchange(auth_code)
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    print(session['url'])
    f=urlopen(session['url'] )
    json_object=json.loads(f.readall().decode('utf-8'))
    print(json_object)
    for event in json_object:
        event = service.events().insert(calendarId='primary', body=event).execute()
    return "Events Created Successfully"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
