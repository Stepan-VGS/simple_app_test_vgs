# VGS TEST APP

This is a simple web application which encrypts and sends payment information entered in a form to a VGS vault, and then exposes the aliased information so that it can be entered in a new form which is submitted in an outbound request (in this case to a VGS echo server) and decrypted. The objective is to demonstrate how inbound and outbound routes can redact and reveal data, rewriting HTTP requests based on user defined filters in order to secure sensitive information.

## Installation

It is recommended to use the most recent version of Python.

Navigate to the project directory and create a venv folder within:

```
$ cd vgs-test
$ python3 -m venv venv
```

On Windows:

```
$ py -3 -m venv venv
```

Before you work on your project, activate the corresponding environment:

```
$ . venv/bin/activate
```

On Windows:

```
> venv\Scripts\activate
```
Your shell prompt will change to show the name of the activated environment.


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flask:
```
$ pip install Flask
```

## Usage

In order to run the application, issue the following command:

```
$ flask run
```

The server is now running locally at `127.0.0.1:5000`. Navigate to this address in your browser, and you will be greeted with the web form which will send sensitive data to a VGS Vault. Submitting this form will present you with the aliased data in the heading of the page, which can be used to fill in the second form which will make an outbound request that decrypts the information back to its original state.