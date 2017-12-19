# BuildSignal Raspberry Pi Client

These are the python scripts for controlling led lights as part of a [buildsignal](https://buildsignal.github.io) project  

## MutliLed.py
This script is used to control individually addressable ws2801 led strips.  
Install the required dependencies, Adafruit\_WS2801 and Adafruit\_GPIO  
Create a cron job to execute the script every minute (or whatever frequency you choose)  
Edit the script to update the configuration:
clientId:  Set to the same client ID configured in your CI Server plugin  
base_url:  Set to the URL for your API Gateway lambda functions  
PIXEL_COUNT:  Set to the number of LEDs on your WS2801 strip  
lights:  Set to a Hash that maps a light id as recognized by your lambda APIs to a list of led pixels to associate as that light  
  
Optionally, update the default colors used for build success and failure.  

You must enable the SPI peripheral:
1. `sudo raspi-config`
2. Use the down arrow to select `9 Advanced Options`
3. Arrow down to `A6 SPI`
4. Select `yes` when it asks you to enable SPI
5. Also select `yes` when it asks about automatically loading the kernel module.
6. Use the right arrow to select the `<Finish>` button.
7. Select `yes` when it asks to reboot.

## SingleLight.py
This script is used to control a basic SMD5050 led strip.  
Install the required dependency, pigpio  
Create a cron job to execute the script every minute (or whatever frequency you choose)  
Edit the script to update the configuration:  
GREEN_PIN: The PIO Output pin controlling connected to the Green signal  
BLUE_PIN: The PIO Output pin controlling connected to the Blue signal  
RED_PIN: The PIO Output pin controlling connected to the Red signal  
LIGHT_ID: The configured light id within the lambda api  
clientId: Must match the client id sent to the lambda functions by the CI Server  
base_url: The url of the API gateway fronting the lambda functions  

Optionally update the default colors used for the build success and failure 