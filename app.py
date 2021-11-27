from flask import Flask, render_template, request, json, request, jsonify
import requests
import os

app = Flask(__name__)

#This route will show the main webpage
@app.route('/', methods=['GET'])
def index():
    return render_template('credit.html')

#This route will forward the request to the outbound vault and reveal the data.
@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        json_dict = request.get_json()
        json1 = request.form['json']
        os.environ[
            'HTTPS_PROXY'] = 'http://US8rEaYKV5sZ39ntynukNKN7:6356b750-87f2-4128-9ce5-730d7057391c@tntcwq7dd18.sandbox.verygoodproxy.com:8080'
        url = 'https://echo.apps.verygood.systems/post'
        data = json1
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, data=data, headers=headers, verify='cert.pem')
        result = json.dumps(r.json(), indent=4)
        result = json.dumps(json.JSONDecoder().decode(result))
        result_dict = json.loads(result)
        return result_dict["json"]
        
    return render_template('base.html')

#This route will show the posts sent to outbound route to the webapp. They are filtered.
@app.route('/post', methods=['POST']) 
def post():
    req_data = request.get_json()
    print (req_data)
    card_cvc = req_data['card_cvc']
    card_expirationDate = req_data['card_expirationDate']
    card_name = req_data['card_name']
    card_number = req_data['card_number']

    return '''
           The card_name is: {}
           The card_number is: {}
           The card_expirationDate is: {}
           The card_cvc is: {}
           '''.format(card_name, card_number, card_expirationDate, card_cvc)
if __name__ == '__main__':
    app.debug = True
    app.run()
