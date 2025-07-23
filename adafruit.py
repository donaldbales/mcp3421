# SPDX-FileCopyrightText: Copyright (c) 2024 Liz Clark for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time

import board

import adafruit_mcp3421.mcp3421 as ADC
from adafruit_mcp3421.analog_in import AnalogIn

i2c = board.I2C()

adc = ADC.MCP3421(i2c, gain=1, resolution=14, continuous_mode=True)
adc_channel = AnalogIn(adc)
# gain, resolution and mode can also be set after instantiation:

# set gain to 1, 2, 4 or 8x
# defaults to 1
# adc.gain = 1

# set resolution to 12, 14, 16 or 18
# defaults to 14
# adc.resolution = 14

# set continuous read mode True or False for one-shot
# defaults to True
# adc.continuous_mode = True

while True:
    print(f"ADC value: {adc_channel.value}")
    volts = 0
    if     adc.resolution == 12:
        volts = adc_channel.value * (0.001 / adc.gain)
    elif adc.resolution == 14:
        volts = adc_channel.value * (0.00025 / adc.gain)
    elif adc.resolution == 16:
        volts = adc_channel.value * (0.0000625 / adc.gain)
    elif adc.resolution == 18:
        volts = adc_channel.value * (0.000015625 / adc.gain)
    else:
        volts = nil
    print(f"ADC voltage: {volts}")
    print(f"Current gain: {adc.gain}X")
    print(f"Current resolution: {adc.resolution}-bit")
    if adc.continuous_mode:
        mode = "continuous"
    else:
        mode = "one-shot"
    print(f"Mode: {mode}")
    print()
    time.sleep(5)

