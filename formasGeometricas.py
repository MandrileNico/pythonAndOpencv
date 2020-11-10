import numpy as np 
import cv2

#img = cv2.imread('lena.jpg', 1)#lee la iamgen opciones 1, 0 , -1
img = np.zeros([512, 512, 3], np.uint8)
img = cv2.line(img, (0,0), (255,255), (255,0,100), 10)
img = cv2.arrowedLine(img, (0,0), (200,255), (255,0,100), 10)
img= cv2.rectangle(img, (384,0), (510,128),(0,0,255), -1 )
img = cv2.circle(img, (255,255), 63, (0,255,0), -1)
font= cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'openCV', (10,500), font,4, (0,255,255), 10, cv2.LINE_AA )
cv2.imshow('image',img) #muestra la imagen tal como es 
cv2.waitKey(0) #espera a q se cierre la ventana
cv2.destroyAllWindows()