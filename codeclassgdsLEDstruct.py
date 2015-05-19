from enum import Enum
import serial
import struct
from time import sleep

DevCodeLUT = {'tach':0x01,'speedo':0x02,'fuel':0x03,'shiftindicator':0x04,'sevenseg':0xf,'LCDdisplay':0xa}
Speedo = {'reset':0x01,'setSpeedMPH':0x03,'lightsOn':0x08}
FuelGauge = {'reset':0x01,'setPercentFull':0x04,'setLowIndicater':0x05,'lightsOn':0x08}
Tach = {'reset':0x01,'setRPM':0x04,'setRL':0x06,'lightsOn':0x08}






class CodeBook(object):
    

    def __init__(self,SerPort):
        

        self.sp = serial.Serial(SerPort)
        self.sp.baudrate = 57600
        #self.sp.write(bytearray('Connection Made','ascii'))
        self.sevenseg = DeviceCode(self,DevCodeLUT['sevenseg'])

    def sendMsg(self, BytesToSend):
        print("Sending:",BytesToSend)
        print(self.sp.write(BytesToSend))
        #self.sp.write('\n'.encode())

class DeviceCode(object):

    def __init__(self,p,dev):
        self.parent = p
        self.devcode = dev
        print('Initializing dev ',dev)

    def On(self):
        cmdcode = 0x01
        head = (self.devcode << 4) | cmdcode
        data1 = 0
        data2 = 0
        print(head)
        values = (head,data1,data2)
        msg = struct.pack('<{0}B'.format(len(values)), *values)
        self.parent.sendMsg(msg)
    
    def Off(self):
        cmdcode = 0x02
        head = (self.devcode << 4) | cmdcode
        data1 = 0
        data2 = 0
        values = (head,data1,data2)
        msg = struct.pack('<{0}B'.format(len(values)), *values)
        self.parent.sendMsg(msg)

    def SetDisplay(self,val):
        cmdcode = 0x03
        head = (self.devcode << 4) | cmdcode
        data1 = ((val & 0xff00) >> 8)
        data2 = val & 0x00ff
        values = (head,data1,data2)
        msg = struct.pack('<{0}B'.format(len(values)), *values)
        self.parent.sendMsg(msg)




CB = CodeBook('COM8')
CB.sevenseg.On()

for x in range(1,1000):
    CB.sevenseg.SetDisplay(x)
    sleep(.01)

CB.sevenseg.Off()

CB.sp.close()
