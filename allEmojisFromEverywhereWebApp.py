#
import flask.Flask
import requests

#
app = flask.Flask(__name__)

#
@app.route('/')
def index():

    #
    return 'Web App with Python Flask!'

#@app.route('/github')
#def getGitHubEmojis():

    #
    #return "GitHub emojis..."

#
app.run(host='0.0.0.0', port=80)
