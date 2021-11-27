import os
import requests

os.environ['HTTPS_PROXY'] = 'http://US8rEaYKV5sZ39ntynukNKN7:6356b750-87f2-4128-9ce5-730d7057391c@tntcwq7dd18.sandbox.verygoodproxy.com:8080'
response = requests.post('https://55409aa3b25c.ngrok.io/post',
						 json={"card_cvc":"tok_sandbox_trHLbVsMCSJCGKVShoS1oA","card_expirationDate":"tok_sandbox_tsk88Qn6npwb3b9oyZefrB","card_name":"Joe Test","card_number":"tok_sandbox_7bjzhsPZHWe14yuxRw13Um"},
                         verify='cert.pem')
print(str(response.text))
