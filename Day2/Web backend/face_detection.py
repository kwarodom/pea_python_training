import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
	ret, frame = cap.read()

	frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
	cv2.imshow("Frame",frame)

	img = frame
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	path = "haarcascade_frontalface_default.xml"

	face_cascade = cv2.CascadeClassifier(path)

	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=5, minSize=(40,40))
	print(len(faces))

	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
		cv2.imwrite("output.jpg", img)
	cv2.imshow("Image",img)

	ch = cv2.waitKey(1)
	if ch & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()