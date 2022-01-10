import os
import dotenv
import json
import requests
from flask import render_template, request
from app import app

# Grabs values from '.env'
dotenv.load_dotenv(override=True)
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
VAULT = os.getenv('VAULT')

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')
	
# Redirect back to index.html which is the redact page
@app.route('/redact_page', methods=['GET'])
def redact_page():
	return render_template('index.html')

# Link on index.html page will activate this to take us to reveal.html
@app.route('/reveal_page', methods=['GET'])
def reveal_page ():
	return render_template('reveal.html')

# When the submit button is clicked on index.html, it will activate this meathod and alias the data
@app.route('/redact', methods=['POST'])
def redact():
	card_number = request.json['card_number']
	card_exp = request.json['card_exp']
	card_cvc = request.json['card_cvc']
	return {"card_number": card_number, "card_exp": card_exp, "card_cvc": card_cvc}

# When the submit button is clicked on reveal.html this method will send aliased data to VGS vault
# it will then return the actual values.
@app.route("/reveal", methods=['POST'])
def reveal():
	card_number = request.form['card_number']
	card_exp = request.form['card_exp']
	card_cvc = request.form['card_cvc']
	card = {'card_number':card_number, 'card_exp':card_exp, 'card_cvc':card_cvc}	
	os.environ['HTTPS_PROXY'] = 'https://{0}:{1}@{2}.sandbox.verygoodproxy.com:8080'.format(
		USERNAME,
		PASSWORD,
		VAULT,
	)
	response = requests.post('https://echo.apps.verygood.systems/post',
						json=card,
						verify='app/sandbox.pem')
	
	data = json.loads(response.json()['data'])
	return render_template(
		'reveal.html',
		card_number=data['card_number'],
		card_exp=data['card_exp'],
		card_cvc=data['card_cvc']
	)
