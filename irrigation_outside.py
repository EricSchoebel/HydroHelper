# After booting Raspberry Pi for setting up GPIO.BOARD Pin 11: gpio_init.py should start automatically because of
# crontab -e
# @reboot /usr/bin/python3 ~/Desktop/gpio_init.py

# crontab -e (execute every morning at 7 o'clock):
# 0 7 * * * /usr/bin/python3 ~/Desktop/irrigation_outside.py

import requests
import RPi.GPIO as GPIO
import time
import os
import openmeteo_requests
import requests_cache
from retry_requests import retry

SWITCH_PIN = 11 # physical pin 11 (= GPIO 17 in BCM mode)
IRRIGATION_SECS = 10 # irrigation in seconds

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SWITCH_PIN, GPIO.OUT, initial=GPIO.LOW) # LOW = water pump is turned off

# File to store the last irrigation day
LAST_WATERING_FILE = "~/Desktop/last_watering.txt" # lists only watering day numbers
CURRENT_DAY = time.localtime().tm_yday  # day number in the year (1 to 365)

def get_weather_data():
    # https://api.open-meteo.com/v1/forecast?latitude=51.3396&longitude=12.3713&daily=temperature_2m_max,precipitation_sum&timezone=Europe%2FBerlin&forecast_days=1

    # Setting up the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 51.3396,
        "longitude": 12.3713,  # latitude and longitude refer to Leipzig
        "daily": ["temperature_2m_max", "precipitation_sum"],
        "timezone": "Europe/Berlin",
        "forecast_days": 1  # weather of the upcoming day
    }
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    daily = response.Daily()
    max_temp = daily.Variables(0).ValuesAsNumpy()[0]  # maximum temperature °C two meters above the ground
    precipitation_sum = daily.Variables(1).ValuesAsNumpy()[0]  # precipation in mm is rain, snow, hail, sleet, ...

    return max_temp, precipitation_sum

def water_plants():
    GPIO.output(SWITCH_PIN, GPIO.HIGH)   # turn pump on
    time.sleep(IRRIGATION_SECS)
    GPIO.output(SWITCH_PIN, GPIO.LOW)  # turn pump off

def should_water_plants(temp, precip):
    if precip > 0:  # if water from the sky, no watering
        return False
    elif temp >= 20:  # 20°C and above, watering
        if os.path.exists(LAST_WATERING_FILE):
            with open(LAST_WATERING_FILE, "r+") as f:
                file_content = f.read()
                f.seek(0)  # Pointer to start of the file
                f.write(str(CURRENT_DAY)+"\n"+file_content)
        else:
            with open(LAST_WATERING_FILE, "w") as f:
                f.write(str(CURRENT_DAY))
        return True
    elif temp < 20:  # under 20°C, only every third day
        if should_water_every_third_day():
            return True
    return False

def should_water_every_third_day():
    """
    Checks if watering is necessary today.
    :return: bool
             true for watering today (and writing the day number in LAST_WATERING_FILE),
             false for no watering today
    """
    if os.path.exists(LAST_WATERING_FILE):
        with open(LAST_WATERING_FILE, "r+") as f:
            last_watering_day = int(f.readline().strip())
            if CURRENT_DAY - last_watering_day >= 3:
                f.seek(0)
                file_content = f.read()
                f.seek(0)
                f.write(str(CURRENT_DAY) + "\n" + file_content)
                return True
            else:
                return False
    else:
        with open(LAST_WATERING_FILE, "w") as f:
            f.write(str(CURRENT_DAY))
        return True

if __name__ == "__main__":
    temp, precip = get_weather_data()
    if should_water_plants(temp, precip):
        water_plants()
