#
from flask import Flask
import requests

#
app = Flask(__name__)

#
@app.route('/')
def index():

    #
    return 'Web App with Python Flask!'

#
@app.route('/support/<wished_support>')
def getEmojisFromSupport(wished_support):

    #
    return 'Here is: ' + wished_support

#
app.run(host='0.0.0.0', port=80)
