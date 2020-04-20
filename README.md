# simple_app_test_vgs

#Requirements

##System

* python
* pip
* ngrok

##VGS

* VGS Account
* VGS Sandbox Certificate
* VGS Sandbox Credentials File

# Setup

## System

Open a terminal to setup and run flask

`virtualenv .venv`
`source .venv/bin/activate`
`pip install -r requirements.txt`
#Make sure your local bin is in your path for flask to run
`export PATH=$PATH:~/.local/bin/`
`flask run`

Open another terminal to run ngrok

`ngrok http 5000`

Note the ngrok Forwarding URL that ngrok provides (https://*********.ngrok.io)

Export these variables for your sandbox instance

* VGS_TENANT_ID - The tenant ID of your sandbox ( {tenant_id}.sandbox.verygoodproxy.com )
* VGS_CERT - Path to your VGS Sandbox certificate file (cert.pem)
* HTTPS_PROXY_USERNAME - The proxy username from the VGS credentials file
* HTTPS_PROXY_PASSWORD - The proxy password from the VGS credentials file

## VGS

Import the YAML configurations for the inbound and outbound rules in the VGS Dashboard

Click on manage for the inbound rule, paste in your ngrok Forwarding URL to the Upstream Host field and click Save.

#Usage

Navigate to the URL for your VGS sandbox and fill out the form to redact the data. Fill in the next form with the redacted data to reveal it.