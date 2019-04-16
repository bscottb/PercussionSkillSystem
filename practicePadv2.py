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
tolerance = 20000 #Means the program will only react of the pressure has increased beyon this threshold
                #Will probably need to tweak
start_time = time.time()
expected = [1, 2, 4, 5, 6, 8]

def check_timing(elapsed_time, expected):
    for time in expected:
        if round(elapsed_time) == time:
            return True
    return False
        
while True:
    elapsed_time = round(time.time() - start_time)
    print("Elapsed time: " + str(elapsed_time))
    if chan0.value > tolerance:
        print("yo" + str(chan0.value))
        if check_timing(elapsed_time, expected):
            print("right                on        time")
##def main(bpm = 60, bpb = 4):
##    sleep = 60.0 / bpm
##    counter = 0
##    last_read = 0
##    while True:
##        counter += 1
##        
##        #assuming no change
##        force_changed = False
##
##        #read the analog pin
##        force = chan0.value
##
##        force_adjust = abs(force - last_read)
##        #if counter % bpb:
##        print("Elapsed time: " + str(round(time.time() - start_time)))
##
##        if force_adjust > tolerance:
##                print (force)
##                last_read = force
##
##        else:
##                
##                if round(time.time() - start_time) % 4 == 0 and force_adjust > tolerance:
##                    print("success")
##
##                    
##
##        time.sleep(sleep)
##main()

