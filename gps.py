import serial

while True:
        # Setup serial
        ser = serial.Serial(port='/dev/ttyS1', baudrate=115200, timeout=2)

        # Read 8 byte response
        #response = ser.read(2024)
        response = ser.readline()
        ser.cancel_read()
        
        #print(response)
        
        gpsData = response.split(b',')
        if(gpsData[0] == b'$GNGGA' and gpsData[3] == b'N' and gpsData[5] == b'E'):
        	latDeg = int(gpsData[2].decode("utf-8")[:2])
        	lngDeg = int(gpsData[4].decode("utf-8")[1:3])
        	
        	latMin = float(gpsData[2].decode("utf-8")[2:]) / 60
        	lngMin = float(gpsData[4].decode("utf-8")[3:]) / 60
        	
        	lat = latDeg + latMin
        	lng = lngDeg + lngMin
        	print(lat)
        	print(lng)