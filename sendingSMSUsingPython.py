import os
# Create Environment Variable (User variable)
#
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

from twilio.rest import Client

client = Client(account_sid, auth_token)


try:
    message = client.messages \
        .create(
            body='''Hello Saba!
                        This is sample message for testing messaging API.
            ''',
            from_ =  +12564459312,
            to = +916391383625 
        )
    print("Message sent Successfully!")
    
except Exception as e:
    print(f'Email could not be sent. Error: {str(e)}')


