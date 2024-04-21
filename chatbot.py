import PySimpleGUI as pg
import re

from imgCapture import image
from aadhaar import aadhaar
from otpVerify import otpVerify
from database import register, tracking

lodge = ['Please Give Your AADHAAR QR Image.',
	 'Please Enter Your Email.',
	 'Please Enter Mobile Number.',
	 'Enter Your Case Details.']
		 
track = ['Please Enter Your Email.',
	 'Enter Your Case ID.']

greeting = 'Welcome to Cyber Friend!!'
options = 'What Do You Want? Press 1: Lodge a Complaint. Press 2: Track a Complaint.'

messages = [greeting, options]
chatArea = pg.Listbox(messages, font=('Times New Roman', 12), expand_x=True, expand_y=True, horizontal_scroll=True, enable_events=True, key='-CHAT-')

layout = [[chatArea],
	  [pg.Input(size=(10, 1), font=('Book Antiqua', 12), expand_x=True, key='-INPUT-'), pg.Button('Send')],
	  [pg.In(key='-PATH-', disabled=True), pg.FileBrowse('Browse', disabled=True)]]

window = pg.Window('CyberBot', layout, size=(600, 1200), resizable=True)

if image():
	index, count, otp = 0, 0, ''
	aadhaarData = {}
	event, values = window.read()
	choice = values['-INPUT-']

	while True:
		if event == pg.WIN_CLOSED:
			break

		elif event == 'Send' and choice == '1':
			if values['-INPUT-'] == '1' and index == 0:
				messages.append(values['-INPUT-'])
				messages.append(lodge[index])
				window['-INPUT-'].update('')
				window['Browse'].update(disabled=False)

			elif values['-PATH-'] != '' and index == 0:
				try:
					aadhaarData = aadhaar(values['-PATH-'])
					if 'referenceid' in aadhaarData.keys():
						id = aadhaarData['referenceid']
						index += 1
						messages.append(f"Hi {aadhaarData['name']}, Your AADHAAR Number Verified!!")
						messages.append(lodge[index])
					elif 'uid' in aadhaarData.keys():
						id = aadhaarData['uid']
						index += 1
						messages.append(f"Hi {aadhaarData['name']}, Your AADHAAR Number Verified!!")
						messages.append(lodge[index])
				except:
					messages.append('Sorry!! Please Give Proper AADHAAR QR Image.')
				window['-PATH-'].update('')

			elif index == 1 and count == 0:
				window['Browse'].update(disabled=True)
				messages.append(values['-INPUT-'])
				regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
				if re.fullmatch(regex, values['-INPUT-']) and count == 0:
					otp = otpVerify(values['-INPUT-'], aadhaarData['name'])
					messages.append(f"OTP Sent Successfully to {values['-INPUT-']}. Enter Your OTP.")
					count += 1
				else:
					messages.append('Please Enter Valid Email.')
				aadhaarData['emailID'] = values['-INPUT-']
				window['-INPUT-'].update('')

			elif index == 1 and count == 1:
				messages.append(values['-INPUT-'])
				if values['-INPUT-'] == otp:
					messages.append('OTP Verified!')
					index += 1
					messages.append(lodge[index])
				else:
					messages.append('Incorrect OTP.')
				window['-INPUT-'].update('')

			elif values['-INPUT-'] != '' and index == 2:
				messages.append(values['-INPUT-'])
				regex = re.compile("(0|91)?[6-9][0-9]{9}")
				if regex.match(values['-INPUT-']):
					index += 1
					messages.append(lodge[index])
				else:
					messages.append('Please Enter Valid Mobile Number.')
				aadhaarData['contactNumber'] = values['-INPUT-']
				window['-INPUT-'].update('')

			elif values['-INPUT-'] != '' and index == 3:
				messages.append(values['-INPUT-'])
				aadhaarData['caseDetails'] = values['-INPUT-']
				window['-INPUT-'].update('')
				index += 1

			if index == 4:
				caseid = register(aadhaarData)
				if caseid is not False:
					messages.append(f'Your Case Has Been Successfully Registered. Your Case ID is {caseid}.')
					window['-CHAT-'].update(messages)
					messages.append('Thank You for Giving Your Valuable Informations. We Will Revert Back to You Soon.')
					window['-CHAT-'].update(messages)
				else:
					messages.append('Your Case Has Not Been Registered Due To Some Problems. Please Try Again Later.')

		elif event == 'Send' and choice == '2':
			if values['-INPUT-'] == '2' and index == 0:
				messages.append(values['-INPUT-'])
				messages.append(track[index])
				window['-INPUT-'].update('')

			elif values['-INPUT-'] != '' and index == 0 and count == 0:
				messages.append(values['-INPUT-'])
				regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
				if re.fullmatch(regex, values['-INPUT-']) and count == 0:
					otp = otpVerify(values['-INPUT-'], 'User')
					messages.append(f"OTP Sent Successfully to {values['-INPUT-']}. Enter Your OTP.")
					aadhaarData['email'] = values['-INPUT-']
					count += 1
				else:
					messages.append('Please Enter Valid Email.')
				window['-INPUT-'].update('')

			elif index == 0 and count == 1:
				messages.append(values['-INPUT-'])
				if values['-INPUT-'] == otp:
					messages.append('OTP Verified!')
					index += 1
					count = -1
					messages.append(track[index])
				else:
					messages.append('Incorrect OTP.')
				window['-INPUT-'].update('')

			elif values['-INPUT-'] != '' and index == 1:
				messages.append(values['-INPUT-'])
				aadhaarData['id'] = values['-INPUT-']
				messages.append(tracking(aadhaarData))
				window['-INPUT-'].update('')

		window['-CHAT-'].update(messages)
		event, values = window.read()

	window.close()

