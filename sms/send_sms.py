import os
import time
from datetime import datetime
from twilio.rest import Client

def send_message(sid, token, name):
    client = Client(sid, token)

    client.messages.create(
        to = os.environ["MY_PHONE_NUMBER"],
        from_ = "+16476967454",
        body = "\nHey", name, "\nRemember to enter your diet and measured weight for today!"
    )

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
while (True):
    cur_time = str(datetime.now())

    # Retrieve name and whether user updated from database here
    updated = False
    name = ""

    if (not updated and cur_time[12:14] == "22" and cur_time[15:17] == "24"):
        send_message(account_sid, auth_token, name)

    time.sleep(60)
