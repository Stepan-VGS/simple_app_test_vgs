# simple_app_test_vgs

This is a simple web application that enables customers to encrypt and decrypt their credit card information through a form that is processed through a VGS inbound and outbound route. This application demonstrates how inbound and outbound routes can redact and reveal data.

Feel free to download and watch my video that shows a quick demonstration of my vgs integrated app in action!

# Requirements

VGS ACCOUNT

Python How to install: (https://www.python.org/downloads/)

PIP    How to install: (https://www.makeuseof.com/tag/install-pip-for-python/)

VirtualEnv


# How to run application


1. Git clone the repository

2. Create a .env file and have the following code in the file
    
   ```
    your_tenant_id = 'Your vgs tenant id'
    USERNAME = 'Your vgs username'
    PASSWORD = 'Your vgs vault password'
    
   ```
3. In the index.html file, change <vault-id> to your vault id to initialize your Collect form.
    

4. Open your terminal and cd into the root directory of the repository and set up a python virtual enviroment by typing the following command:

    For Mac
    ```
    $ python3 -m venv venv
    ```
    For Windows
    ```
    py -3 -m venv venv
    ```
    
5. To activate the virtual enviroment, run the following command within the directory to activate it:
 
    For Mac
    
    ```
    $ . venv/bin/activate
    ```
    
    For Windows
    
    ```
    > venv\Scripts\activate
    
    You should see in the terminal that your shell prompt is changed due to the virtual enviroment being activated
    
6. Install flask through pip:

    ```
    $ pip install flask
    ```
    
7. Next pip install requests:

    ```
    $ pip install requests
    ```
 
8. To use the flask and the application itself type in the following command in the directory:

     ```
     flask run
     ```
You should now be able to access your app locally by entering 127.0.0.1:5000 on your web browser.


SImply follow the instructions on the app web page and watch VGS magic happen!
