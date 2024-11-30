# HydroHelper
## Automated Plant Irrigation 

by Eric Schöbel

**HydroHelper** automates plant irrigation using a Raspberry Pi and a weather API. For balcony plants, the daily weather report is retrieved via an API, and depending on temperature and rainfall, it determines whether to water the plants. For indoor plants, irrigation occurs without weather data.

**Features**

 + Indoor irrigation: Daily automatic watering for a predefined duration
 + Outdoor irrigation with weather dependency:
    - Retrieval of daily weather data (temperature and precipation)
    - No watering in case of precipation (rain, snow, hail, sleet, ...)
    - Watering above 20°C or every three days at lower temperatures
 + File-based storage of the last watering date for adaptive irrigation based on temperature and time criteria
 
**Application**

The project is based on Python and runs on a Raspberry Pi Model B+. Two scripts, controlled by Crontab entries – one for indoor and one for outdoor irrigation – are executed daily at 7:00 am to operate the water pump.

**Code Modules**

+ gpio_init.py: Initializes the GPIO pin to control the water pump
+ irrigation_inside.py: Handles indoor irrigation, activating the pump for a predefined number of seconds
+ irrigation_outside.py: Manages outdoor irrigation, including weather data retrieval and watering decision logic

**Overview**

![Überblick](./overview.jpg "Overview")

**Disclaimer**

Any liability or warranty is excluded. The use of this code is at your own risk.
