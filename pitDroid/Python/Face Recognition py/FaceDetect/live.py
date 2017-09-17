# This script will detect faces via your webcam.
# Tested with OpenCV3

import cv2
import serial # if you have not already done so
import numpy as np

def set_res(cap, x,y):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(x))
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(y))

ser = serial.Serial(2, 250000)  #abre serial COM3

cap = cv2.VideoCapture(0)

#can be any of those
#   160.0 x 120.0
#   176.0 x 144.0
#   320.0 x 240.0
#   352.0 x 288.0
#   640.0 x 480.0
#   1024.0 x 768.0
#   1280.0 x 1024.0
frame_w = 640
frame_h = 480
set_res(cap, frame_w,frame_h)

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")



while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    cap.read()
    frame=cv2.flip(frame,1)


    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image 
    #faces = [[face],[x,y,dx,dy]]
    faces = np.array([]) 
    faces = faceCascade.detectMultiScale(
        gray,   
        scaleFactor=1.1,
        minNeighbors=20,
        minSize=(30, 30)
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )

#    print("Found {0} faces!".format(len(faces)))
#    print(faces)
    

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#        cv2.circle(frame,(x+w/2,y+y/2), 2, (0,0,255), 3, 8,0)
        cv2.circle(frame,(frame_w/2,frame_h/2), 2, (255,0,0), 3, 8,0) #ponto azul no centro
        
#        cv2.circle(frame,(faces[0,0],faces[0,1]), 2, (255,255,0), 3, 8,0) #ponto azul no centro
#        cv2.circle(frame,(faces[0,0]+faces[0,2]/2,faces[0,1]+faces[0,3]/2), 2, (255,255,0), 3, 8,0) #ponto azul no centro

 #        tamanho total de deslocamento
#        tamanho da tela - tamanho do frame do rosto
        
#        posicao do centro do rosto na tela = posicao x + dx/2
         
#    total = max_vel * (posicao x + dx/2) / (tamanho da tela - tamanho do frame do rosto)


     

#para aceitar valores negativos de deslocamento, 
#basta subtrair no valor final metade do valor do 
#tamanho da tela menos metade do tamnho do frame do rosto




    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

     
    if ([i for i in faces]):     #testa se tem rosto detectado:                                #testa se string está vazia
        face_center_x = faces[0,0]+faces[0,2]/2
        face_center_y = faces[0,1]+faces[0,3]/2
        
        err_x = 30*(face_center_x - frame_w/2)/(frame_w/2)
        err_y = 30*(face_center_y - frame_h/2)/(frame_h/2)
        
        ser.write(str(err_x) + "x!")        #otimizacao: não enviar string, mas inteiro direto
        ser.write(str(err_y) + "y!")        #otimizacao: não enviar string, mas inteiro direto
    else:
        ser.write("o!")        
                  
'''teste com serial byte a byte
#        if err_x < 0:
#            sinal = 1
#        else:
#            sinal = 0          
#        sendData = bytearray([ord('<'), ord('x'), int(sinal), int(abs(err_x)), ord('>')])
#        print sendData
#        ser.write(sendData)        #otimizacao: não enviar string, mas inteiro direto
#   '''         



# When everything done, release the capture
ser.close()
cap.release()
cv2.destroyAllWindows()
