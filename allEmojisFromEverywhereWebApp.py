#
from flask import Flask
import requests

#
app = Flask(__name__)

#
supports = ["Apple", "apple",
            "Google", "google",
            "Samsung", "samsung",
            "Microsoft", "microsoft",
            "WhatsApp", "Whatsapp", "whatsApp", "whatsapp",
            "Twitter", "twitter",
            "Facebook", "FaceBook", "faceBook", "facebook",
            "Skype", "skype",
            "JoyPixels", "Joypixels", "joyPixels", "joypixels",
            "OpenMoji", "Openmoji", "openMoji", "openmoji",
            "Emojidex", "emojidex",
            "Messenger", "messenger",
            "LG", "lg",
            "HTC", "htc",
            "Mozilla", "mozilla",
            "SoftBank", "Softbank", "softBank", "softbank",
            "Docomo", "docomo",
            "au_by_KDDI", "au_by_kddi"]

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
    if wished_support in supports:

        #
        return 'Choosen support: ' + wished_support

    #
    else:

        #
        return 'Unfortunately... ' + wished_support + ' is unknown...'

#
app.run(host='0.0.0.0', port=80)
