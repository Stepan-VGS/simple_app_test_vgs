from app import app
from flask import render_template, request
from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()
# get config vars from env file
USERNAME = os.getenv('PROXY_USERNAME')
PASSWORD = os.getenv('PROXY_PASSWORD')
VAULT_ID = os.getenv('VAULT_ID')
PORT = os.getenv('PORT')

@app.route('/', methods=['GET'])
def index():
    '''
    render the index page

    Index pages has fields for user to
    enter credit card info (name, number, expiration, cvc)
    '''
    return render_template('index.html')


@app.route('/redact', methods=['POST'])
def redact():
    '''
    Take the data from index page and send to 
    VGS to alias the card number, expiration and CVC
    data. Card holder will not be aliased.

    After recieving the aliased data, render the message.html 
    page and show the aliased data.
    '''
    card_holder = request.form['card_holder']
    original_card_num = request.form['card_num']
    original_card_exp = request.form['card_exp']
    original_card_cvc = request.form['card_cvc']

    res = requests.post(f"https://{VAULT_ID}.sandbox.verygoodproxy.com/post",
                        json={'card_holder': card_holder, 'card_number': original_card_num, 'card_cvc': original_card_cvc, 'card_exp': original_card_exp}, 
                        verify=False)

    res = res.json()
    data = json.loads(res['data'])

    return render_template('message.html', data=data)


@app.route("/reveal", methods=['POST'])
def reveal():
    '''
    Take the data from the message.html page and reveal
    the original data.
    '''
    aliased_card_num = request.form['card_num']
    aliased_card_exp = request.form['card_exp']
    aliased_card_cvc = request.form['card_cvc']
    
    os.environ['HTTPS_PROXY'] = f'https://{USERNAME}:{PASSWORD}@{VAULT_ID}.sandbox.verygoodproxy.com:{PORT}'

    res = requests.post('https://echo.apps.verygood.systems/post',
                        json={'card_number': aliased_card_num, 'card_exp': aliased_card_exp, 'card_cvc': aliased_card_cvc},
                        verify='app/secrets/cert.pem')

    data = json.loads(res.json()['data'])

    return render_template('forward.html', data=data)
