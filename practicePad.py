import os
import time
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus

spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the chip select
cs = digitalio.DigitalInOut(board.D22)

#create a mcp object
mcp = MCP.MCP3008(spi, cs)

#create an analog input channel on the MCPs pin 0
chan0 = AnalogIn(mcp, MCP.P0)

#ADC -> analog-to-Digital Converter -> the MCP3008
print('Raw ADC Value: ', chan0.value)
print('ADC Voltage: ' + str(chan0.voltage) + 'V')


last_read = 0 #keeps track of the last FSR value
tolerance = 200 #Means the program will only react of the pressure has increased beyon this threshold
                #Will probably need to tweak

while True:
        #assuming no change
        force_changed = False

        #read the analog pin
        force = chan0.value

        force_adjust = abs(force - last_read)

        if force_adjust > tolerance:
                force_changed = True

        if force_changed:
                print(force)

                last_read = force
                

time.sleep(0.5)

        
