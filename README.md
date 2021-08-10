# VGS Test Application WIP

This is a web application which demonstrates how to use VGS to tokenize and reveal tokenized data. In our particular
example, a credit card data will be used.


## Pre-requisites:
- python3
- pip


## Running the application

1. Navigate to the project's root folder and create a python virtual environment. 

`python -m venv vgstest`

Then, to activate it, run: `source vgstest/bin/activate`

2. Install python packages, necessary for the project. They are all listed in the requirements.txt file.

`pip install -r requirements.txt`

3. In the project's root folder, create an `.env` file. It should have the following contents:

```
USERNAME=<put-your-username-here>
PASSWORD=<put-your-password-here>
TENANT_ID=<put-your-tenant-id-here>
```

Here's how to [generate username/password pair](https://www.verygoodsecurity.com/docs/settings/access-credentials), if 
you don't have or remember them.

Your tenant_id is also known as a vault_id can be found in the upper left corner of VGS dashboard. Alternatively,
take it from the code sample [here](https://www.verygoodsecurity.com/docs/guides/outbound-connection).

4. Run the application using the following command:

`flask run`

5. Now you can access the webpage on http://127.0.0.1:5000/? to send a request to tokenize the data.

6. To reveal the tokenized data, open http://127.0.0.1:5000/reveal


### Additional information

Organization ID: ACZu3P7sibhrkcDYLaefKDi
Organization Name: farafarafara
