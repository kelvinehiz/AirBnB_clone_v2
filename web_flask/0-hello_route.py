#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/airbnb-onepage/')
def hello_hbnb():
    """print web"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
