import smtplib

smtp_server = 'smtp.gmail.com'
smtp_port = 587  
sender_email = 'itssatyanarayanyadav@gmail.com'
sender_password = 'fbqn ltuz pckr epro'  

receiver_email = input("Enter receiver e-mail: ")
subject = input("Enter Subject: ")
message = input("Enter e-mail body: ")

# Create an SMTP connection
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
