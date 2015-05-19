DevCodeLUT = {'tach':0x01,'speedo':0x02,'fuel':0x03,'shiftindicator':0x04}





TxMsg = bytearray([Header, data1, data2])
sp.write(TxMsg)

class CodeBook(object):
    Tach = {'reset':0x01,'setRPM':0x04,'setRL':0x06,'lightsOn':0x08}
    Speedo = {'reset':0x01,'setSpeedMPH':0x03,'lightsOn':0x08}
    FuelGauge = {'reset':0x01,'setPercentFull':0x04,'setLowIndicater':0x05,'lightsOn':0x08}

    def _init_(self,SerPort):
        

class DeviceCode(object):
