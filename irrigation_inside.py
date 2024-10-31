# After booting Raspberry Pi for setting up GPIO.BOARD Pin 11: gpio_init.py should start automatically because of
# crontab -e
# @reboot /usr/bin/python3 ~/Desktop/gpio_init.py

# crontab -e (execute every morning at 7 o'clock):
# 0 7 * * * /usr/bin/python3 ~/Desktop/irrigation_inside.py

import RPi.GPIO as GPIO
import time

SWITCH_PIN = 11  # physical pin 11 (= GPIO 17 in BCM mode)
# LOW = water pump is turned off

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SWITCH_PIN, GPIO.OUT, initial=GPIO.LOW)

GPIO.output(SWITCH_PIN, GPIO.HIGH)   # turn pump on

time.sleep(5) # irrigation in seconds

GPIO.output(SWITCH_PIN, GPIO.LOW)  # turn pump off

