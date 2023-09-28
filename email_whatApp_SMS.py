import smtplib
import pywhatkit
import os
import vonage
from twilio.rest import Client


# ---------------Sending Email-------------------------
def sendEmail(receiver_email, subject, email_body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  
    sender_email = os.environ['EMAIL']
    sender_password = os.environ['EMAIL_APP_PASSWORD']
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS encryption
        server.login(sender_email, sender_password)

        # Compose the email
        email_body = f'Subject: {subject}\n\n{message}'

        # Send the email
        server.sendmail(sender_email, receiver_email, email_body)

        # Close the SMTP server
        server.quit()

        print('Email sent successfully')
    except Exception as e:
        print(f'Email could not be sent. Error: {str(e)}')


# ---------------Sending WhatsApp Message-------------------------
def sendWhatsAppmsg(number, message, hr, mint):
    pywhatkit.sendwhatmsg(number, message, hr, mint, 15, 10)


# ---------------Sending SMS-------------------------
def sendSMS(sender_detail, to_number, message):
    account_sid = os.environ['VONAGE_API_KEY']
    auth_token = os.environ['VONAGE_API_SECRET']
    client = vonage.Client(key=account_sid, secret=auth_token)
    sms = vonage.Sms(client)

    # Sending messaging
    try:
        response = sms.send_message(
            {
                "from": sender_detail,
                "to": to_number,
                "text": message,
            }
        )   
        print(f"Message sent Successfully with message id \"{response['messages'][0]['message-id']}!\"")
        
    except Exception as e:
        print(f'SMS could not be sent. Error: {str(e)}')


while True:
    try:
        print('''\n*****************************************\n
            1. Send E-mail
            2. Send WhatsApp Message
            3. Send SMS
            4. Exit
        ''')
        choice = int(input("Enter Your Choice (1/2/3/4): "))
        
        if (choice == 1):
            receiver_email = input("Enter receiver e-mail: ")
            subject = input("Enter Subject: ")
            message = input("Enter e-mail body: ")
            sendEmail(receiver_email, subject, message)
        
        elif (choice == 2):
            phone_number = input("Enter the WhatsApp Number: ")
            message = input("Enter message to send: ")
            time_hr = input("Enter the time(hours): ")
            time_min = input("Enter the time(min): ")
            sendWhatsAppmsg(phone_number, message, time_hr, time_min, 15, False, 10)

        elif (choice == 3):
            sender_detail = input("Enter Sender's Name: ")
            to_number = input("Enter Receiver's Number: ")
            message = input("Enter your message: ")
            sendSMS(sender_detail, to_number, message)

        elif(choice == 4):
            print("------------ Exit -----------")
            exit(0)

    except Exception as e:
        print(f"Something went wrong. {str(e)}")


