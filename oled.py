from OmegaExpansion import oledExp
import time

print('Writing to OLED screen')
text = 'Omega2 <3 Python3'

# initialize the screen
oledExp.setVerbosity(0)
ret = oledExp.driverInit()

# set the cursor position
#ret = oledExp.setCursor(3,0)

# write the message
ret = oledExp.drawFromFile("hereLogo.lcd")

print('Done')