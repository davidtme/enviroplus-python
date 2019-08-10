#!/usr/bin/env python

import time
from enviroplus import gas

print("""gas.py - Print readings from the MICS6814 Gas sensor.

Press Ctrl+C to exit!

""")

try:
    while True:
        in0 = adc.get_voltage('in0/ref')
        print('in0: {in0}')

        in1 = adc.get_voltage('in1/ref')
        print('in1: {in1}')
    
        in2 = adc.get_voltage('in2/ref')
        print('in2: {in2}')

        time.sleep(1.0)
except KeyboardInterrupt:
    pass
