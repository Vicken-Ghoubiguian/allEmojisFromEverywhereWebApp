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
    elif wished_support == "Microsoft" or wished_support == "microsoft":

        #
        return "Microsoft"

    #
    elif wished_support == "WhatsApp" or wished_support == "Whatsapp" or wished_support == "whatsApp" or wished_support == "whatsapp":

        #
        return "WhatsApp"

    #
    elif wished_support == "Twitter" or wished_support == "twitter":

        #
        return "Twitter"

    #
    elif wished_support == "Facebook" or wished_support == "FaceBook" or wished_support == "faceBook" or wished_support == "facebook":

        #
        return "Facebook"

    #
    elif wished_support == "Skype" or wished_support == "skype":

        #
        return "Skype"

    #
    elif wished_support == "JoyPixels" or wished_support == "Joypixels" or wished_support == "joyPixels" or wished_support == "joypixels":

        #
        return "JoyPixels"

    #
    else:

        #
        return 'Here is: ' + wished_support

#
app.run(host='0.0.0.0', port=80)
