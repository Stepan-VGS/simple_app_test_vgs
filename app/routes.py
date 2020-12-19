from app import app
from flask import render_template, request, jsonify
import requests
import os


username = app.config.get("USERNAME")
password = app.config.get("PASSWORD")
vault_id = app.config.get("VAULT_ID")
vgs_sample_echo_server = app.config.get("VGS_SAMPLE_ECHO_SERVER")
port = app.config.get("PORT")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/grab_data', methods=['GET','POST'])
def grab_data():
    return render_template('reveal.html')

@app.route('/reveal_data', methods=['POST'])
def reveal_data():
    
    payload = request.form['token_data']
    headers = {
    'Content-Type': 'application/json'  
    }

    os.environ['HTTPS_PROXY'] = f'http://{username}:{password}@{vault_id}.sandbox.verygoodproxy.com:{port}'
    res = requests.request("POST", f'{vgs_sample_echo_server}/post' , headers=headers, data=payload, verify='app/CERT.PEM')

    res = res.json()
    return render_template('final.html',response=res)
