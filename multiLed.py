#!/usr/bin/python

import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI
import RPi.GPIO as GPIO
import time
import requests

#### Configuration ####

PIXEL_COUNT = 96

lights = { '1': [0, 1, 2] }

clientId = ''
base_url = ''

# Light color for when all builds are successful
success_color = Adafruit_WS2801.RGB_to_color(0, 200, 0)

# Light color for when a light shows a build failure
failure_color = Adafruit_WS2801.RGB_to_color(200, 0, 0)

# Light color when we can't get the status of the lights
connection_error_color = Adafruit_WS2801.RGB_to_color(200, 200, 0)

status_url = base_url + '/lights/status'

SPI_PORT   = 0
SPI_DEVICE = 0

#### END Configuration ####

pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

def setLightColor( light, color ):
    if light in lights:
        for pixel in lights[light]:
            pixels.set_pixel(pixel, color)

def setLight( light, status ):
    if status:
        setLightColor( light, success_color )
    else:
        setLightColor( light, failure_color )

def connectionError():
    for lightId in lights.keys():
        setLightColor( lightId, connection_error_color )

if __name__ == "__main__":
    pixels.clear()

    headers = {'X_CLIENT_ID':clientId}
    
    response = requests.get(status_url, headers=headers)

    if response.status_code != 200:
        connectionError()
    else:
        for lightId, status in response.json().iteritems():
            setLight(lightId, status)

    pixels.show()
