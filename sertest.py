import serial
import irsdk
import threading
from time import sleep

carspeed = 0

class Racecar:

    def __init__(self, name):
        self.speed = 0
           #

    def accelerate(tgtspeed,timetospeed):
        step = (carspeed - tgtspeed) / (timetospeed * 0.05)
        while(self.speed < tgtspeed and self.speed > 0):
            sleep(0.05)
            self.speed = self.speed + step

    def getspeed:
        return self.speed    

    
'''
def simulatecar():
    while not shutdown_event.is_set():
        #wait at starting line
        sleep(2) 
        
        #accelerate to 100m/h
        while carspeed < 100:
            sleep(.1)
            carspeed


ser = serial.Serial(0)  # open first serial port
print(ser.portstr)       # check which port was really used
ser.write('hello'.encode())      # write a string
ser.close()  
'''


