import logging
import random
import json

from flask import Flask
from flask import render_template
from flask_ask import Ask, request, session, question, statement


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@ask.launch
def launch():
    speech_text = 'What do you want to know about Gabby and Jesses wedding.'
    return question(speech_text).reprompt(speech_text)


@ask.intent('WhereIntent')
def where():
    speech_text = 'We want to get married in XXXXX'
    return statement(speech_text).simple_card('Where', speech_text)

@ask.intent('WhenIntent')
def when():
    speech_text = 'They plan to get married in XXXXX'
    return question(speech_text).simple_card('When', speech_text)

@ask.intent('LastNameIntent')
def last_name():
    speech_text = 'No decision yet, but they are progressive and open to options'
    return question(speech_text).simple_card('LastName', speech_text)

@ask.intent('KidsIntent')
def kids():
    speech_text = 'They will have kids someday'
    return question(speech_text).simple_card('Kids', speech_text)

@ask.intent('InviteIntent')
def invite():
    speech_text = 'Anyone who can make it to XXXX'
    return question(speech_text).simple_card('Kids', speech_text)

@ask.session_ended
def session_ended():
    return "", 200


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=8000)