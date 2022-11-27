"""
# !/usr/bin/env python3
"""
import serial
import time
import sys
from Classes.dispense_drink import DispenseDrink



if __name__ == '__main__':
    #ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)
    #ser.reset_input_buffer()
    uwu = DispenseDrink()
    uwu.handler(sys.argv[1],sys.argv[2],sys.argv[3])
    
    ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)
    ser.reset_input_buffer()
    ser.write(b"Hello from Raspberry Pi!\n")
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
    time.sleep(1)

    # while True:
    #     ser.write(b"Hello from Raspberry Pi!\n")
    #     line = ser.readline().decode('utf-8').rstrip()
    #     print(line)
    #     time.sleep(1)