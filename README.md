# simple_app_test_vgs

This is a simple program to demonstrate aliasing and unaliasing of credit card data. It works by taking in your credit card information (number, expiration date, cvc) and aliases that information for better security. You can then, use those aliases to get the orignal data back.

## Set up
Create a python virtual environment and activate it
```
python3 -m venv env
source env/bin/activate
```
Install the needed requirements with:
```
pip install -r requirements.txt
```

#### Create .env file
Create a .env file at the root of the project and populate with the fields below:
```
PROXY_USERNAME=
PROXY_PASSWORD=
VAULT_ID=
PORT=8080
```

The PROXY_USERNAME and PROXY_PASSWORD can be found by going to VGS Dashboard -> Vault Settings -> Access Credentials
The VAULT_ID can be found at the top left of the VGS Dashboard
#### Run the app
In a terminal run the following command to start the application
```
python3 simple_app.py
```

### Usage instructions
1. navigate to 127.0.0.1:5000
2. Input your name, card number, card expiration date, and card cvc
3. Click "Redact" to see the aliased data
4. Click "Reveal" again to see the original data