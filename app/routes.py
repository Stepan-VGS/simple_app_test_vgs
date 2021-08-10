from app import app
from flask import render_template, request, jsonify, Flask, json

import requests
import os
import sqlite3

USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
TENANT_ID = os.environ.get('TENANT_ID')


def init_db():
    database = 'database.db'
    if (os.path.isfile(database)):
        os.remove(database)
    conn = sqlite3.connect(database)
    conn.execute('CREATE table card_data (card_number TEXT, card_cvc TEXT, card_exp TEXT)')
    conn.commit()
    conn.close()


init_db()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# For some reason, this route is not used, can't figure out why.
@app.route('/post', methods=['POST'])
def post():
    message = request.json
    print(message['card_data'])
    g.db = sqlite3.connect('database.db')
    # At least data is not in the database
    # I am also not sure that this construction is correct :|
    g.db.execute("INSERT INTO card_data (card_number, card_cvc, card_exp) VALUES (?,?,?)", (message['card_number'], message['card_cvc'], message['card_exp']))
    g.db.commit()
    g.db.close()
    return message, 200


@app.route('/reveal', methods=['GET'])
def reveal():
    return render_template('reveal.html')


@app.route("/forward", methods=['POST'])
def forward():
    message = request.form['message']

    os.environ['HTTPS_PROXY'] = f'https://{USERNAME}:{PASSWORD}@{TENANT_ID}.sandbox.verygoodproxy.com:8080'
    res = requests.post('https://echo.apps.verygood.systems/post',
                        # Being a bit lazy here, form is for only revealing tokenized card num which surely can be
                        # expanded to all three fields
                        json={'card_number': message},
                        verify='app/secrets/sandbox.pem')

    res = res.json()
    return render_template('forward.html', response=res)
