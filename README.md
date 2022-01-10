# simple_app_test_vgs

This application will demonstrate the use of VGS redact and reveal features.

- Make sure you have Python3 installed with pip
- You'll also need ngrok downloaded 

# Setup
	- Under "simple_app_test_vgs" edit the file ".env" and your USERNAME, PASSWORD, and VAULT
	- USERNAME and PASSWORD need to be generated following these instructions: 
		https://www.verygoodsecurity.com/docs/settings/access-credentials
	- VAULT is the "Vault ID" located at the top of your home page when logged into your vgs dashboard.
	
# Python virtual enviroment
	- This is optional but it's recommended to setup a python virtual env for this.
	- In cmd navigate to "simple_app_test_vgs" folder and enter this command:
		python -m venv vgsenv
	- To activate run this for windows:
		source vgsenv/Scripts/activate
	- Activate for Linux
		source vgsenv/bin/activate
		
# Install the project requirements, while in the same folder in cmd run this command:
	- pip install -r requirements.txt
	
# Ngrok
	- Startup your ngrok and run:
		ngrok http 5000
	- Then copy the forwarding address
	- Log into vgs dashboard and open inbound routes
	- paste the address in the "Upstream Host" text box and save
	
# While logged into VGS you should setup your routes
	- Inbound Routes
		Conditions for all IB routes will be
			PathInfo > matches > /redact
			ContentType > equals > application/json
		Fields in JSON path, need three varibles:
			$.card_number
			$.card_exp
			$.card_cvc
	- Outbound Routes
		Conditions for all OB routes will be
			PathInfo > matches > /reveal
			ContentType > equals > application/json
		Fields in JSON path, need three varibles:
			$.card_number
			$.card_exp
			$.card_cvc
	$.card_cvc should have a "Storage" type of "Volatile" for compliance
	
# Run Flask
	- Within cmd and the project folder type in:
		flask run
	- You can now enter http://127.0.0.1:5000 into your web browser
	
# Operation
	- Fill in the three text boxes and enter any data you would like then click the submit button.
	- You will see the aliased values returned by vgs at the top of the page.
	- Open the "Reveal" page in a new tab and copy the aliased values over and click submit.
	- You should now see the original values returned.
	
# VGS logs
	- This is for validation and/or for fun but you can also log into your vgs dashboard and see the Inbound and Outbound logs.
	- Click "Logs" on left hand side menu in the VGS dashboard.
	- Click "Record payloads" button near the top to enable logging for 1 hour.
	- run your program with data.
	- wait 1 miute then click the "Load New Request" button on the dashboard.