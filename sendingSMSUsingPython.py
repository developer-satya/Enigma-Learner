import os
from twilio.rest import Client

# Create Environment Variable (User variable)
# Named: TWILIO_ACCOUNT_SID     value: (twilio sid)
# Named: TWILIO_AUTH_TOKEN      value: (authorization token)
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


# Sending messaging
try:
    message = client.messages\
        .create(
            body='''Hello Mr/ms!
                        This is sample message for testing messaging API.
            ''',
            from_ =  "FROM_NUMBER",
            to = "TO_NUMBER"
        )
    print("Message sent Successfully!")
    
except Exception as e:
    print(f'SMS could not be sent. Error: {str(e)}')


