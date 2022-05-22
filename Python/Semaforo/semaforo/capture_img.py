import cv2
import numpy as np
import imutils
import os

Datos = 'n'
if not os.path.exists(Datos):
	print('La carpeta fue creada exitosamente: ', Datos)
	os.makedirs(Datos)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

x1, y1 = 190, 80
x2, y2 = 450, 398

count = 0
while True:

	ret, frame = cap.read()
	if ret == False:
		break
	imAux = frame.copy()
	cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

	semaforo = imAux[y1:y2, x1:x2]
	semaforo = imutils.resize(semaforo, width=38)
	# print(semaforo.shape)

	k = cv2.waitKey(1)
	if k == ord('s'):
		cv2.imwrite(Datos+'/semaforo_{}.jpg'.format(count), semaforo)
		print('Imagen almacenada como: ', 'semaforo_{}.jpg'.format(count))
		count = count + 1
	if k == 27:
		break

	cv2.imshow('frame', frame)
	cv2.imshow('Semaforo', semaforo)

cap.release()
cv2.destroyAllWindows()
