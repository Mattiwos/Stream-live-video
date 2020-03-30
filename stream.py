#!/usr/bin/env python3.7
import cv2

import random
import socketio

#pip install "python-socketio[client]
# remove everything else related to socketio
# "




sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('connection established')
   
@sio.on('disconnect')
def on_disconnect():
    print('disconnected from server')

sio.connect('http://localhost:8080') #sends to nodejs


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    img_str = cv2.imencode('.jpg', frame)[1].tostring()


    sio.emit('liveClientSocket1',img_str)
  
   




cap.release()
cv2.destroyAllWindows()
sio.disconnect()






