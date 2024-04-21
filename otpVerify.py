'''


***************************************************
Using mobile number at Twilio
***************************************************


import random
from twilio.rest import Client

otp = random.randint(10000, 99999)

account_sid = "ACaad96fea71ff503087857b0913f99d1b"

auth_token = "2187cc424aa8949aab21ab8e2b62b786"

client = Client(account_sid, auth_token)

msg = client.messages.create(
	body = f"Your otp is {otp}",
	from_ = "+15855728305",
	to = "+919883801697"
)
'''

'''

***************************************************
Using gmail and smtp
***************************************************

'''

import random
import math
import smtplib
from email.message import EmailMessage

def otpVerify(emailid, name):
	digits = "0123456789"
	OTP = ""
	for i in range(6):
	    OTP += digits[math.floor(random.random()*10)]

	message = f"Dear {name}, \nYour OTP is " + OTP + ".\n\n\nYours sincerely, \nCyberbot."

	msg = EmailMessage()
	msg.set_content(message)

	msg['Subject'] = 'CyberBot Verification OTP'
	msg['From'] = "cyberbot0205@gmail.com"
	msg['To'] = emailid

	# Send the message via our own SMTP server.
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login("cyberbot0205@gmail.com", "pumsexntwrfymdol")
	server.send_message(msg)
	server.quit()
	
	return OTP

