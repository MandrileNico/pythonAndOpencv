import cv2
import datetime
cap = cv2.VideoCapture(0)# capturar viedeo de la camara de mi dispositivo
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))#optengo el ancho del a imagen en pixeles , el alto
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(datetime.date.today())
#cap.set(3,700)# representa el valor del allto, se puede remplazarr el comando por el numero q lo representa
#cap.set(4,700)

#print(cap.get(3))#optengo el ancho del a imagen en pixeles , el alto
#print(cap.get(4))

while(cap.isOpened()):#verifica que se inicializo el video correctamente
    ret, frame = cap.read()# lee lo q capta la camra y lo almacena

    if ret == True :
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: '+ str(cap.get(3)) + 'Heigth: ' + str(cap.get(4))
        datet =str(datetime.datetime.today())
        frame = cv2.putText(frame, datet, (10,50), font, 1, (0,255,255), 2, cv2.LINE_AA)

        cv2.imshow('frame', frame)# muestro el video en vivio

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()