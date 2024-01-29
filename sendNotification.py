import boto3
mysns = boto3.client("sns")

def send_sms():
	mysns.publish(
		Message="SMS Notification Amazon Web Services Using Command Prompt.👋😅",
		Subject="⚠️Notification",
		TopicArn="arn:aws:sns:ap-south-1:943393446406:SMS-notify"
	)
	return "SMS is Successfully Sent!"
	

def send_email():
	mysns.publish(
		Message="Email Notification Amazon Web Services Using Command Prompt.👋😅",
		Subject="⚠️Email Notification",
		TopicArn="arn:aws:sns:ap-south-1:943393446406:s3delete"
	)
	return "Email is Successfully Sent!"

print("1.send SMS")
print("2.send Email")
choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
	print(send_sms())
elif choice == 2:
	print(send_email())
else:
	print("❌Invalid Input!")

