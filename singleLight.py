#!/usr/bin/python

import pigpio
import time
import requests

#### Configuration ####

GREEN_PIN = 19
BLUE_PIN = 17
RED_PIN = 25

LIGHT_ID = '1'

clientId = ''
base_url = ''

# Light color for when all builds are successful
success_color = (0, 255, 0)

# Light color for when a light shows a build failure
failure_color = (255, 0, 0)

# Light color when we can't get the status of the lights
connection_error_color = (255, 255, 0)

status_url = base_url + '/lights/status'

#### END Configuration ####

pi = pigpio.pi()

def setColorByRGB(red, green, blue):
    pi.set_PWM_dutycycle(RED_PIN, red)
    pi.set_PWM_dutycycle(GREEN_PIN, green)
    pi.set_PWM_dutycycle(BLUE_PIN, blue)

def setLightColor( color ):
    setColorByRGB( color[0], color[1], color[2] )

def setLight( status ):
    if status:
        setLightColor( success_color )
    else:
        setLightColor( failure_color )

def connectionError():
    setLightColor( connection_error_color )

if __name__ == "__main__":

    headers = {'X_CLIENT_ID':clientId}
    response = requests.get(status_url, headers=headers)

    if response.status_code != 200:
        connectionError()
    else:
        for lightId, status in response.json().iteritems():
            if lightId == LIGHT_ID:
            	setLight(status)

