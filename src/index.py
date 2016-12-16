from __future__ import print_function
from rivescript import RiveScript
import time
import datetime
import urllib2
import json
import re
import pytz


rs = RiveScript()
rs.load_directory("./brain")
rs.sort_replies()


def lambda_handler(event, context):

    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "ChatBotIntent":
        return getChatBot(intent, session)
    elif intent_name == "AMAZON.StopIntent":
        return signoff()
    else:
        return getChatBot(intent, session)


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    session_attributes = {}
    card_title = "Welcome to chatter"
    userData = ""
    dt = datetime.datetime.fromtimestamp(time.time(), pytz.utc)
    tz = pytz.timezone('US/Pacific')
    myTime = tz.normalize(dt.astimezone(tz)).strftime('%H/%M/%B/%A')
    hour,minute,mth,nameDay = myTime.split("/")
    now = int(hour)
    if now < 7:
        greetings = "Good morning, how can I help you?"
    elif now > 18:
        greetings = "Good evening, what can I do for you?"
    else:
        greetings = "Hello, how can I help you? "
    speech_output = "<speak>" + greetings + "</speak>"
    reprompt_text = "<speak>Hello, are you there?</speak>"
    should_end_session = False
    session_attributes = {"speech_output": speech_output,"reprompt_text": reprompt_text,"userData": userData}
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def getChatBot(intent, session):
    session_attributes = {}
    card_title = "Talk to me"
    username = "localuser"
    userData = session['attributes']['userData']
    if userData:
        for key, value in userData[username].items():
            rs.set_uservar(username, key, value)
    message = intent['slots']['response'].get('value')
    reply = rs.reply("localuser", message)
    userData = rs.get_uservars();

    speech_output = "<speak>"+reply+"</speak>"
    reprompt_text = "<speak>I didn't hear that, please say again.</speak>"
    should_end_session = False
    session_attributes = {"speech_output": speech_output,"reprompt_text": reprompt_text,"userData": userData}
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def inspireMe():
    url = "http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json"
    response = urllib2.urlopen(url)
    try:
        data = dict(json.loads(response.read()))
        inspireMe = data['quoteText']
    except:
        inspireMe = " Be kind to yourself."
    return inspireMe


def signoff():
    session_attributes = {}
    card_title = "Signing off"
    getTime = time.time()
    dt = datetime.datetime.fromtimestamp(time.time(), pytz.utc)
    tz = pytz.timezone('US/Pacific')
    myTime = tz.normalize(dt.astimezone(tz)).strftime('%H/%M/%B/%A')
    hour,minute,mth,nameDay = myTime.split("/")
    now = int(hour)
    inspire = inspireMe()
    if now > 21:
        goodbye = "Good night, sleep well <break time='1s'/> here's a final thought " + "<break time='1s'/>" + str(inspire)
    else:
        goodbye = "Take care, see you later, here's a final thought " + "<break time='1s'/>" + str(inspire)
    speech_output = "<speak>"+goodbye+"</speak>"
    should_end_session = True
    reprompt_text = ""
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    should_end_session = True
    return build_response({}, build_speechlet_response(
        None, None, None, should_end_session))



# --------------- Helpers that build all of the responses ----------------------


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            "type": "SSML",
            "ssml": output
        },
       'reprompt': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
