import time
import onionGpio


gpio19 = onionGpio.OnionGpio(19)

status = gpio19.setInputDirection()

count = 0

while True:
	value = gpio19.getValue()
	
	print(value)
	
	time.sleep(0.5)
	#
	#if(value == '1\n'):
	#	count += 1
	#	print(count)