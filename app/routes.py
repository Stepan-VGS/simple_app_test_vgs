from app import app
from flask import render_template, request, jsonify, json
import requests
import os

#config file isnt working but still put this code here to show what i tried using

#USERNAME = app.config.get("USERNAME")
#PASSWORD = app.config.get("PASSWORD")
#your_tenant_id = app.config.get("your_tenant_id")

#enter your credentials in the empty strings
USERNAME= 'USa4XQsMziwmAjwF445b3eX9'
PASSWORD= '372cce8a-1dc0-46dc-a248-ac4436066058'
your_tenant_id='tnt60zkr2pg'

#simple route that renders the home page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

#route implementation that asks the user to enter redacted data
@app.route('/add_message', methods=['GET','POST'])
def add_message():
    
    return render_template('message.html')

#route implementation that shows the user the decrpyted data
@app.route("/forward", methods=['POST'])
def forward():
    
    payload = request.form['json_data']
    headers = {
    'Content-Type': 'application/json'  
    }

    os.environ['HTTPS_PROXY'] = f'http://{USERNAME}:{PASSWORD}@{your_tenant_id}.sandbox.verygoodproxy.com:8080'
    res = requests.post('https://echo.apps.verygood.systems/post',headers=headers, data=payload, verify='app/cert.pem')
    res = res.json()
    
    return render_template('forward.html',response=res)