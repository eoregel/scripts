#!/usr/bin/python3

import os 
import re
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from flask import Flask, request, redirect

# Your Account SID from twilio.com/console
account_sid = "ACb4f2702cfb0d222aa27205f9cd365429"
# Your Auth Token from twilio.com/console
auth_token  = "adefe18cba753e4dc9732e48eadaf048"

client = Client(account_sid, auth_token)

app = Flask(__name__)
@app.route("/sms", methods=['GET', 'POST'])

def sms_reply():
    #respond to incoming messages
    res = MessagingResponse()
    res.message("The robots are coming! Head for the hills!")
    return str(res)

if __name__ == "__main__":
    app.run(debug=True)