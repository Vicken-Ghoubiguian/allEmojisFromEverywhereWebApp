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
    if wished_support == "Apple" or wished_support == "apple":

        #
        return "Apple"

    #
    elif wished_support == "Google" or wished_support == "google":

        #
        return "Google"

    #
    elif wished_support == "Samsung" or wished_support == "samsung":

        #
        return "Samsung"

    #
    else:

        #
        return 'Here is: ' + wished_support

#
app.run(host='0.0.0.0', port=80)
