import logging
import random
import json

from flask import Flask
from flask import render_template
from flask_ask import Ask, request, session, question, statement


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

reprompt = "hope that helps"

@ask.launch
def launch():
    speech_text = 'What do you want to know about Gabby and Jesses wedding.'
    return question(speech_text)

@ask.intent('WhereIntent')
def where():
    speech_text = 'Costa Rica'
    return question(speech_text).simple_card('Where', speech_text)

@ask.intent('WhenIntent')
def when():
    speech_text = 'They plan to get married in early 2018'
    return question(speech_text).simple_card('When', speech_text)

@ask.intent('LastNameIntent')
def last_name():
    speech_text = 'No decision yet, but they are progressive and open to options'
    return question(speech_text).simple_card('LastName', speech_text).reprompt(reprompt)

@ask.intent('KidsIntent')
def kids():
    speech_text = 'They will have kids someday'
    return question(speech_text).simple_card('Kids', speech_text).reprompt(reprompt)

@ask.intent('InviteIntent')
def invite():
    speech_text = 'Anyone who can make it to XXXX'
    return question(speech_text).simple_card('Kids', speech_text).reprompt(reprompt)

@ask.intent('JustinBieberIntent')
def what_is_love():
    speech_text = "What do you mean? Oh, oh"
    return question(speech_text).reprompt(reprompt)

@ask.intent('WhatDoYouMeanIntent')
def what_do_you_mean():
    speech_text = "What do you mean? Hey ey"
    return question(speech_text).reprompt(reprompt)

@ask.intent('WhatDoYouMeanAgainIntent')
def dont_hurt_me():
    speech_text = "What do you mean? Oh, what do you mean?"
    return question(speech_text).reprompt(reprompt)

@ask.intent('WhatDoYouMeanFinalIntent')
def what_do_you():
    speech_text = "what do you mean? oh, oh, oh what do you mean? Better make up your mind. What do you mean?"
    return question(speech_text).reprompt(reprompt)

@ask.session_ended
def session_ended():
    return "", 200

@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Goodbye")


@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Goodbye")


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=8000)