import RPi.GPIO as GPIO

WATER_PIN = 11
GPIO.setmode(GPIO.BOARD)

GPIO.setup(WATER_PIN, GPIO.OUT, initial=GPIO.LOW)

