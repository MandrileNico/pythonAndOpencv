import numpy as np 
import cv2

img = cv2.imread('lena.jpg', 0)#lee la iamgen opciones 1, 0 , -1
print(img)# la imprime como matriz

cv2.imshow('image',img) #muestra la imagen tal como es 
k = cv2.waitKey(0) #espera a q se cierre la ventana
if k==27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copý.png', img) #copia imagenes
    cv2.destroyAllWindows()