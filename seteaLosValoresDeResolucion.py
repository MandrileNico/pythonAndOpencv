import cv2

cap = cv2.VideoCapture(0)# capturar viedeo de la camara de mi dispositivo
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#optengo el ancho del a imagen en pixeles , el alto
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3,700)# representa el valor del allto, se puede remplazarr el comando por el numero q lo representa
cap.set(4,700)

print(cap.get(3))#optengo el ancho del a imagen en pixeles , el alto
print(cap.get(4))

while(cap.isOpened()):#verifica que se inicializo el video correctamente
    ret, frame = cap.read()# lee lo q capta la camra y lo almacena

    if ret == True :

        #print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#optengo el ancho del a imagen en pixeles , el alto
        #print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        

        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)# convierte a escale de gris

        cv2.imshow('frame', gray)# muestro el video en vivio

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()