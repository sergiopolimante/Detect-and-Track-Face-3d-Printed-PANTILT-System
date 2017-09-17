# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 18:54:12 2017

@author: sergi
"""

import serial # if you have not already done so
import time                #used to keep track of time


#ser = serial.Serial('/dev/tty.usbserial', 9600)

ser = serial.Serial(2, 9600)

i=0
while i<10:
    
    i= i+1
    time.sleep(1) #loop executes once every 0.2 seconds (= 5 Hz)

    ser.write("foi!")
    
ser.close()