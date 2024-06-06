from twilio.rest import Client

ACCOUNT_SID_TWILIO = "AC5682c9cbaa6c11f32402f92d38ebf8e6"
AUTH_TOKEN_TWILIO = "69980f5fbdf5f048e7b9361e0356417c"
TWILIO_VIRTUAL_PH_NO = "+18329253283"
TWILIO_VERIFIED_PH_NO ="+917075912537"



class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.Client = Client(ACCOUNT_SID_TWILIO, AUTH_TOKEN_TWILIO)

    def send_sms(self,message):
        message = self.Client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_PH_NO,
            to=TWILIO_VERIFIED_PH_NO
        )
        print(message.sid)

