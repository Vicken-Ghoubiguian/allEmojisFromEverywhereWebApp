#
from flask import Flask
import requests

#
app = Flask(__name__)

#
supports = {}

#
@app.route('/')
def index():

    #
    return 'Web App with Python Flask!'

#
@app.route('/emoji/<string:wished_emoji>')
def getEmoji(wished_emoji):

    #
    return "For emoji " + wished_emoji + "..."

#
@app.route('/support/<string:wished_support>')
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
    elif wished_support == "OpenMoji" or wished_support == "Openmoji" or wished_support == "openMoji" or wished_support == "openmoji":

        #
        return "OpenMoji"

    #
    elif wished_support == "Emojidex" or wished_support == "emojidex":

        #
        return "Emojidex"

    #
    elif wished_support == "Messenger" or wished_support == "messenger":

        #
        return "Messenger"

    #
    elif wished_support == "LG" or wished_support == "lg":

        #
        return "LG"

    #
    elif wished_support == "HTC" or wished_support == "htc":

        #
        return "HTC"

    #
    elif wished_support == "Mozilla" or wished_support == "mozilla":

        #
        return "Mozilla"

    #
    elif wished_support == "SoftBank" or wished_support == "Softbank" or wished_support == "softBank" or wished_support == "softbank":

        #
        return "SoftBank"

    #
    elif wished_support == "Docomo" or wished_support == "docomo":

        #
        return "Docomo"

    #
    elif wished_support == "au_by_KDDI" or wished_support == "au_by_kddi":

        #
        return "au by KDDI"

    #
    else:

        #
        return 'Here is: ' + wished_support

#
app.run(host='0.0.0.0', port=80)
