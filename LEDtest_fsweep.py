from enum import Enum
import serial
import struct
from time import sleep



reps = 25
waitcnt = 20
wait_inc = .001
waitrange = []
wtime_s = .002
stallamt = 100



def GetByte(i):
    return chr(i).encode()

def packmsg(dig,val):
    if dig > 3: dig = 3
    if dig < 0: dig = 0
    if val > 9: val = 9
    if val < 0: val = 0
    dig = (dig & 0x00ff) | 0xf0
    #msg = chr(dig) + chr(val) + chr(0x11)
    values = (dig,val,0x05)
    string = ''
    #for i in values:
        #string += struct.pack('!B',i)
    #msg = chr(0xf1) + chr(0x07) + chr(0x11)
    s = struct.pack('!{0}B'.format(len(values)), *values)
    return s

v_msg = []

for x in range(101,0,-1):
    waitrange.extend([x*wait_inc] * (5))


for d in range(0,waitcnt):
    for rpt in range(0,reps):
        for pin in (0,1,2,3):
            v_msg.append(packmsg(pin,5))

tmin = waitrange[-1]


'''
for d in range(0,stallamt):
    for pin in (0,1,2,3):
        v_msg.append(packmsg(pin,5))
'''        

waitrange.extend([tmin] * ( len(v_msg)-len(waitrange)+ 1))



sp = serial.Serial('COM8')
sp.baudrate = 57600

endmsgs = v_msg[-4:]
print(endmsgs)

print(len(v_msg),len(waitrange))
try:
    for i,m in enumerate(v_msg):
        sp.write(m)
        #print("sending: ", m)
        sleep(waitrange[i])
    while (1):
        for ms in endmsgs:
            sp.write(ms)
            sleep(tmin)

        

except Exception as e:
    print("Exception!")
    print(e)


sp.close()



'''
msg = chr(0x55)
print(sp.write(msg.encode()))

'''
