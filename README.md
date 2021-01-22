# simple_app_test_vgs

This is a simple web application that enables customers to encrypt and decrypt their credit card information through a form that is processed through a VGS inbound and outbound route. This application demonstrates how inbound and outbound routes can redact and reveal data.

Feel free to download and watch my video that shows a quick demonstration of my vgs integrated app in action!

# Requirements

Python How to install: (https://www.python.org/downloads/)

PIP    How to install: (https://www.makeuseof.com/tag/install-pip-for-python/)

VirtualEnv


# How to run application


1. Git clone the repository

2. Open your terminal and cd into the root directory of the repository and set up a python virtual enviroment by typing the following command:


    For Mac
    ```
    $ python3 -m venv venv
    ```
    For Windows
    ```
    py -3 -m venv venv
    ```
    
3. To activate the virtual enviroment, run the following command within the directory to activate it:
 
    For Mac
    ```
    $ . venv/bin/activate
    ```
    For Windows
    ```
    > venv\Scripts\activate
    
    You should see in the terminal that your shell prompt is changed due to the virtual enviroment being activated
    
4. While you are in the virtual enviroment, install flask through pip:
    ```
    $ pip install flask
    ```
    
5. Next pip install requests,
    ```
    $ pip install requests
    ```
 
6.  To use the flask and the application itself type in the following command in the directory:
 
     ```
     flask run
     ```
You should now be able to access your app locally by entering 127.0.0.1:5000 on your web browser.

# Using the App

In the routes.py and config.py files, you should see at the beginning of each file to enter in your username, password and tenant_id in the empty strings that are provided by your vgs vault. 

SImply follow the instructions on the app web page and watch VGS magic happen!
