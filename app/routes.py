from app import app
from flask import render_template, request, jsonify
import requests
import os
import sqlite3


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/message', methods=['GET'])
def message():
    return render_template('message.html')


@app.route('/post', methods=['POST'])
def post():
    message = request.json
    return message, 200


@app.route("/forward", methods=['POST'])
def forward():
    message = request.form['message']

    os.environ['HTTPS_PROXY'] = 'https://UStuxaJU5RVKd7JC4GWWZN1f:93390e04-3643-4f21-b277-c1bc0852de60@tntnopmrps6.SANDBOX.verygoodproxy.com:8080'
    res = requests.post('https://echo.apps.verygood.systems/post',
                        json={'message': message},
                        verify='app/sandbox.pem')

    res = res.json()
    return render_template('forward.html', response=res)
