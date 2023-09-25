import os
from twilio.rest import Client

# Find your Account SID and Auth Token at 👉 https://www.twilio.com/console
# Set environment variables. 👉 https://www.twilio.com/blog/how-to-set-environment-variables-html

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


