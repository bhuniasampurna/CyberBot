#! /usr/bin/python3

'''

***************************************************
Using gmail and smtp
***************************************************

'''

import random
import math
import smtplib
from email.message import EmailMessage

from database import update

caseList = update()

for case in caseList:
	print(case[0], case[1], case[2], case[3])
	message = f"Dear {case[1]}, \nYour case with case id {case[2]} is {case[3]}.\n\n\nYours sincerely, \nCyberbot."
	print(message)

	msg = EmailMessage()
	msg.set_content(message)

	msg['Subject'] = f'Status of Your Case ID {case[2]}'
	msg['From'] = "cyberbot0205@gmail.com"
	msg['To'] = case[0]

	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login("cyberbot0205@gmail.com", "pumsexntwrfymdol")
	server.send_message(msg)
	server.quit()

