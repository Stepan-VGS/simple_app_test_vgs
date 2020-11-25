from app import app
from app.config import Config
import sqlite3
from flask import render_template, g, request, json
import requests
import os

def init_db():
    database = 'database.db'
    conn = sqlite3.connect(database)

    conn.execute('CREATE table cards (cnumber INT PRIMARY KEY, cvc TEXT, cexp TEXT)')
    conn.commit()
    conn.close()
    print('Added to DB')

init_db()

#HOMEPAGE
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

#DISPLAYS REDACTED INFORMATION AND FORM TO RETRIEVE REVEALED DATA
@app.route('/showredacted')
def showredacted():
    g.db = sqlite3.connect('database.db')
    cur = g.db.execute('select * from cards')
    data = [dict(card_number=row[0], card_cvc=row[1], card_expirationDate=row[2]) for row in cur.fetchall()]
    g.db.close()
    message = json.dumps(data[0], sort_keys = False, indent = 2)

    return render_template('showredacted.html', message=message, cnumber=data[0]['card_number'], cvc=data[0]['card_cvc'], cexp=data[0]['card_expirationDate']) 

#POST endpoint for VGS Outbound Route
@app.route('/post', methods=['POST'])
def post():
    message = request.json
    print (message['card_number'])
    g.db = sqlite3.connect('database.db')
    g.db.execute("INSERT INTO cards (cnumber, cvc, cexp) VALUES (?,?,?)", (message['card_number'], message['card_cvc'], message['card_expirationDate']))
    g.db.commit()
    g.db.close()
    return message, 200

@app.route('/reveal', methods=['POST'])
def reveal():
    cnumber = request.form['card_number']
    cvc = request.form['card_cvc']
    cexp = request.form['card_expirationDate']
    cfg = Config()
    os.environ['HTTPS_PROXY'] = 'https://'+cfg.USERNAME+':'+cfg.PASSWORD+'@'+cfg.VAULTID+'.SANDBOX.verygoodproxy.com:8080'
    res = requests.post('https://echo.apps.verygood.systems/post',
                        json={'card_number':cnumber,'card_cvc':cvc,'card_expirationDate':cexp},
                        verify='app/sandbox.pem')
    res = res.json()
    return render_template('reveal.html', response=json.dumps(res.json, sort_keys = False, indent = 2))