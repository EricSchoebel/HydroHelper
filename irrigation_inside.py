# After booting Raspberry Pi for setting up GPIO.BOARD Pin 11: gpio_init.py should start automatically because of
# crontab -e
# @reboot /usr/bin/python3 ~/Desktop/gpio_init.py

# crontab -e (execute every morning at 7 o'clock):
# 0 7 * * * /usr/bin/python3 ~/Desktop/irrigation_inside.py

import RPi.GPIO as GPIO
import time

SWITCH_PIN = 11  # physical pin 11 (= GPIO 17 in BCM mode)
IRRIGATION_SECS = 10 # irrigation in seconds

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SWITCH_PIN, GPIO.OUT, initial=GPIO.LOW) # LOW = water pump is turned off

GPIO.output(SWITCH_PIN, GPIO.HIGH)   # turn pump on
time.sleep(IRRIGATION_SECS)
GPIO.output(SWITCH_PIN, GPIO.LOW)  # turn pump off

