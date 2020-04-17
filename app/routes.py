from app import app
from flask import render_template, request, redirect, url_for, jsonify
import requests
import json
import os

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/add_message', methods=['POST'])
def add_message():

    ccn = request.form['ccn']
    cvv = request.form['cvv']
    exp = request.form['exp']

    res = requests.post("https://tntaeqsy19v.sandbox.verygoodproxy.com/post",
                             json={'ccn': ccn, 'cvv': cvv, 'exp': exp})

    res = res.json()
    str_data = res['data']

    data = json.loads(str_data)

    ccn_redacted = data['ccn']
    cvv_redacted = data['cvv']
    exp_redacted = data['exp']

    return render_template('message.html', ccn=ccn_redacted, cvv=cvv_redacted, exp=exp_redacted)

@app.route("/forward", methods=['POST'])
def forward():
    ccn = request.form['ccn']
    cvv = request.form['cvv']
    exp = request.form['exp']

    os.environ['HTTPS_PROXY'] = 'https://USnH8Ne1Lo65DGcDjBnBkorW:eba20426-5c70-41fa-9d5a-642e31b085b1@tntaeqsy19v.sandbox.verygoodproxy.com:8080'
    res = requests.post("https://echo.apps.verygood.systems/post",
                        json={'ccn': ccn, 'cvv': cvv, 'exp': exp},
                        verify='/Users/jxd8fbj/Documents/simple_app_test_vgs/app/static/cert/cert.pem')

    res = res.json()
    data = res['json']

    ccn_clean = data['ccn']
    cvv_clean = data['cvv']
    exp_clean = data['exp']


    return render_template('forward.html', ccn=ccn_clean, cvv=cvv_clean, exp=exp_clean)