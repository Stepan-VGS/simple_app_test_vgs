from app import app
import sqlite3
from flask import render_template, g, request, jsonify
import requests
import os

def init_db():
    database = 'database.db'
    g.db = sqlite3.connect(database)

    g.db.execute('CREATE table cards (cnumber INT PRIMARY KEY, cvv TEXT, cexp TEXT)')
    #query = "INSERT INTO cards (cvv, cnumber, cexp)  VALUES ('data1', 'data2', 'data3')"
    #c.execute(query)
    g.db.commit()
    g.db.close()
    print('Added to DB')

init_db()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/message', methods=['GET'])
def message():
    return render_template('message.html')


@app.route('/database')
def test():
    g.db = sqlite3.connect('database.db')
    cur = g.db.execute('select * from cards')
    message = [dict(d1=row[0], d2=row[1], d3=row[2]) for row in cur.fetchall()]
    g.db.close()
    return render_template('message.html', message=message)

@app.route('/post', methods=['POST'])
def post():
    message = request.json
    print (message['card_number'])
    g.db = sqlite3.connect('database.db')
    #g.db.execute("INSERT INTO cards (cnumber, cvv, cexp)  VALUES ('data1', 'data2', 'data3')")
    g.db.execute("INSERT INTO cards (cnumber, cvv, cexp) VALUES (?,?,?)", (message['card_number'], message['card_cvc'], message['card_expirationDate']))
    g.db.close()
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
