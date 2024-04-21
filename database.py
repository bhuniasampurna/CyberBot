'''


***************************************
Using MySQL
***************************************


'''
import mysql.connector

def register(msg):
	print(msg)
	try:
		mydb = mysql.connector.connect(
		  host="localhost",
		  user="root",
		  password="SBDatabase@02",
		  database="SBHtest"
		)

		mycursor = mydb.cursor()
		print(msg.keys())

		if "referenceid" in msg.keys():
			addr = msg['house'] + ', ' + msg['street'] + ',' + msg['vtc'] + ' P.O.- ' + msg['postoffice'] + ', ' + msg['subdistrict'] + ', ' + msg['district'] + ', ' + msg['state'] + ', ' + msg['pincode']
			mycursor.execute(f"INSERT INTO Crimes(id, aadhaar_last_4digits, name, address, email, contact, dob, case_details, status) VALUES(\"{msg['referenceid']}\", {msg['adhaar_last_4_digit']}, \"{msg['name']}\", \"{addr}\", \"{msg['emailID']}\", \"{msg['contactNumber']}\", \"{msg['dob']}\", \"{msg['caseDetails']}\", \"Registered\");")
			
		elif 'uid' in msg.keys():
			addr = msg['vtc'] + ', ' + msg['dist'] + ', ' + msg['state'] + ', ' + msg['pc']
			mycursor.execute(f"INSERT INTO Crimes(id, aadhaar_last_4digits, name, address, email, contact, dob, case_details, status) VALUES(\"{msg['uid']}\", {msg['uid'][-4:]}, \"{msg['name']}\", \"{addr}\", \"{msg['emailID']}\", \"{msg['contactNumber']}\", \"{msg['yob']}\", \"{msg['caseDetails']}\", \"Registered\");")
		
		mycursor.execute("SELECT LAST_INSERT_ID();")
		id = mycursor.fetchall()
		mydb.commit()
		return id[0][0]
	except:
		return False
  
def tracking(msg):
	print(msg)
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  password="SBDatabase@02",
	  database="SBHtest"
	)
	
	mycursor = mydb.cursor()
	mycursor.execute(f"SELECT status FROM Crimes WHERE case_id={msg['id']} and email=\"{msg['email']}\";")
	rows = mycursor.fetchall()
	if not rows:
		return "Case ID Not Found."
	else:
		return f"The case is {rows[0][0]}"

def update():
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  password="SBDatabase@02",
	  database="SBHtest"
	)
	
	mycursor = mydb.cursor()
	mycursor.execute("SELECT distinct(email), name, case_id, status FROM Crimes WHERE status!=\"Completed\";")
	rows = mycursor.fetchall()
	if not rows:
		pass
	else:
		caseList = []
		for row in rows[1:]:
			caseList.append((row[0], row[1], row[2], row[3]))
		return caseList




'''


**************************************
Using Apex
**************************************


import pandas as pd
import requests

url = "https://apex.oracle.com/pls/apex/demossb/employee/?limit=10000"
r = requests.get(url)
json = r.json()
df = pd.DataFrame(json['items'])
'''

'''


***************************************
Using Firebase
***************************************


import pyrebase
from collections import Mapping

config = {
  "apiKey": "AIzaSyBHm1GAQ8DdIkegwhaY5ewRUkKttP-bb_8",
  "authDomain": "sbhr-97464.firebaseapp.com",
  "projectId": "sbhr-97464",
  "storageBucket": "sbhr-97464.appspot.com",
  "messagingSenderId": "522023490284",
  "appId": "1:522023490284:web:73b8ea779f89f836360bc9",
  "measurementId": "G-HTSQ9CQ7ZG"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

email = "sbhar2002@gmail.com"
password = "SBH@2023"

user = auth.create_user_with_email_and_password(email, password)
print("User created")
'''
