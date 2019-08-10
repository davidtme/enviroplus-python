#!/usr/bin/env python

import time
import atexit
import ads1015
import RPi.GPIO as GPIO

MICS6814_HEATER_PIN = 24
MICS6814_GAIN = 6.144

ads1015.I2C_ADDRESS_DEFAULT = ads1015.I2C_ADDRESS_ALTERNATE
_is_setup = False
_adc_enabled = False
_adc_gain = 6.148


def setup():
    global adc, _is_setup
    if _is_setup:
        return
    _is_setup = True

    adc = ads1015.ADS1015(i2c_addr=0x49)
    adc.set_mode('single')
    adc.set_programmable_gain(MICS6814_GAIN)
    adc.set_sample_rate(1600)

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MICS6814_HEATER_PIN, GPIO.OUT)
    GPIO.output(MICS6814_HEATER_PIN, 1)
    atexit.register(cleanup)


def enable_adc(value=True):
    """Enable reading from the additional ADC pin."""
    global _adc_enabled
    _adc_enabled = value


def set_adc_gain(value):
    """Set gain value for the additional ADC pin."""
    global _adc_gain
    _adc_gain = value


def cleanup():
    GPIO.output(MICS6814_HEATER_PIN, 0)

def read_all():
    """Return gas resistence for oxidising, reducing and NH3"""
    setup()
    
    in0 = adc.get_voltage('in0/ref')
    print('in0: {in0}')
    
    in1 = adc.get_voltage('in1/ref')
    print('in1: {in1}')

    in2 = adc.get_voltage('in2/ref')
    print('in2: {in2}')
    
try:
    while True:
        read_all()
        time.sleep(1.0)
except KeyboardInterrupt:
    pass
