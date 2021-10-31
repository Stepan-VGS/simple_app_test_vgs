import os
import json
import requests
from flask import render_template, request

from app import app

VGS_SANDBOX_URL = "SANDBOX.verygoodproxy.com:8080"

#This will throw an exception if these env vars are not configured at runtime
VGS_SANDBOX_USER = os.environ['HTTPS_PROXY_USERNAME']
VGS_SANDBOX_PW = os.environ['HTTPS_PROXY_PASSWORD']
VGS_SANDBOX_CERT = os.environ['VGS_CERT']
VGS_SANDBOX_TENANT = os.environ['VGS_TENANT_ID']

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/add_payment', methods=['POST'])
def add_payment():
    card_num = request.form['card_num']
    exp_date = request.form['exp_date']
    cvv = request.form['cvv']
    return render_template(
        'message.html',
        card_num=card_num,
        exp_date=exp_date,
        cvv=cvv
    )

@app.route("/forward", methods=['POST'])
def forward():
    card_num = request.form['card_num']
    exp_date = request.form['exp_date']
    cvv = request.form['cvv']
    payload = {'card_num':card_num, 'exp_date':exp_date, 'cvv':cvv}
    os.environ['HTTPS_PROXY'] = 'https://{0}:{1}@{2}.{3}'.format(
        VGS_SANDBOX_USER,
        VGS_SANDBOX_PW,
        VGS_SANDBOX_TENANT,
        VGS_SANDBOX_URL,
    )
    res = requests.post('https://echo.apps.verygood.systems/post',
                        json=payload,
                        verify='{0}'.format(VGS_SANDBOX_CERT))

    data = json.loads(res.json()['data'])
    return render_template(
        'forward.html',
        card_num=data['card_num'],
        exp_date=data['exp_date'],
        cvv=data['cvv']
    )
