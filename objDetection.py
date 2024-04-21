import cv2
import matplotlib.pyplot as plt


def obj(imgpath):
	config_file = '/home/sampurnab/Sampurna_Bhunia_1/College/College_Documents/Project/Personal_project/SBH_All/frozen_inference_graph.pb'
	frozen_model = '/home/sampurnab/Sampurna_Bhunia_1/College/College_Documents/Project/Personal_project/SBH_All/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'

	classlabels = []
	file_name = open(r'/home/sampurnab/Sampurna_Bhunia_1/College/College_Documents/Project/Personal_project/SBH_All/labels.txt','rt').read()

	classlabels = file_name.split('\n')
	print(classlabels)

	model = cv2.dnn_DetectionModel(frozen_model,config_file)
	print(model)

	model.setInputSize(320, 320)
	model.setInputScale(1.0/127.5)
	model.setInputMean((127.5, 127, 5, 127.5))
	print(model.setInputSwapRB(True))

	img = cv2.imread(imgpath)
	plt.imshow(img)
	#plt.show()

	ClassIndex, confidence, bbox = model.detect(img, confThreshold=0.5)
	print(ClassIndex)
	
	if len(ClassIndex) == 0:
		return False
	else:
		if ClassIndex[0] == 1:
			return True
		else:
			return False
