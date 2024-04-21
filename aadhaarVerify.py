import cv2
from pyzbar.pyzbar import decode
from pyaadhaar.utils import isSecureQr
from pyaadhaar.decode import AadhaarSecureQr
from pyaadhaar.decode import AadhaarOldQr

def aadhaar(imgPath) :
	img = cv2.imread(imgPath)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	code = decode(gray)
	qrData = code[0].data
	decoded_secure_qr_data = {}
	try:
		secure_qr = AadhaarSecureQr(int(qrData))
	except:
		secure_qr = AadhaarOldQr(qrData)
	finally:
		decoded_secure_qr_data = secure_qr.decodeddata()
	
	return decoded_secure_qr_data

