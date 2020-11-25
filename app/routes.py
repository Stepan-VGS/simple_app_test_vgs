from app import app
import sqlite3
from flask import render_template, g, request, jsonify, json
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

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')



@app.route('/showredacted') #TEST ENDPOINT
def showredacted():
    g.db = sqlite3.connect('database.db')
    data = g.db.execute('select * from cards').fetchall()
    
    g.db.close()
    message = jsonify(data)
    return render_template('message.html', message=message)

@app.route('/post', methods=['POST'])
def post():
    message = request.json
    print (message['card_number'])
    g.db = sqlite3.connect('database.db')
    g.db.execute("INSERT INTO cards (cnumber, cvc, cexp) VALUES (?,?,?)", (message['card_number'], message['card_cvc'], message['card_expirationDate']))
    g.db.commit()
    g.db.close()
    return message, 200



@app.route("/reveal", methods=['GET'])
def reveal():
    g.db = sqlite3.connect('database.db')
    cur = g.db.execute('select * from cards')
    message = [dict(card_number=row[0], card_cvc=row[1], card_expirationDate=row[2]) for row in cur.fetchall()]
    g.db.close()

    os.environ['HTTPS_PROXY'] = 'https://UStuxaJU5RVKd7JC4GWWZN1f:93390e04-3643-4f21-b277-c1bc0852de60@tntnopmrps6.SANDBOX.verygoodproxy.com:8080'
    res = requests.post('https://echo.apps.verygood.systems/post',
                        json=message,
                        verify='app/sandbox.pem')

    res = res.json()
    return render_template('forward.html', response=res)
