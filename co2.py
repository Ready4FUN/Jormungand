import serial
import time


co2 = serial.Serial("/dev/ttyS0", 
						baudrate=9600,
                        bytesize=serial.EIGHTBITS,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        timeout=1.0)


while True:
	crc = 0
	
	co2.write(b'\xff\x01\x86\x00\x00\x00\x00\x00\x79')
	#co2.write("xffx01x86x00x00x00x00x00x79")

	time.sleep(0.1)
	
	response = co2.read(9)
	#co2.cancel_read()

	
	
	
		
		
		
	if len(response) > 4:
		print((response[2] * 256) + response[3])
		print(crc)
		print(response[8])
		
		for i in range(1, 8):
			crc += response[i]

		
		crc = 255 - crc
		crc += 1
		
		if response[8] != crc:
			print("crc error")
		
	print(response)
	
	time.sleep(60)