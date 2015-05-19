from enum import Enum
import serial
import struct
from time import sleep

head = (0x7E)
data = (0x0f,0xf0,0x00,0xff) 
print(head)
print(data)
values = (head,len(data)) + data
msg = struct.pack('<{0}B'.format(len(values)), *values)
print(msg)

#test comment
sp = serial.Serial('COM8')
sp.baudrate = 57600
sp.write(msg)
sp.close()
