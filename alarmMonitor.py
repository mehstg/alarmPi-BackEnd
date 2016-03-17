#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time, logging, sys
from pyrowl import Pyrowl
import pprint as ppt

# Setup pyrowl with API key
p = None
p = Pyrowl("e16f88f0268ebb3a332f288cf7409f605c90899f")

#Set up logging
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

GPIO.setmode(GPIO.BCM)

#Initialise GPIO Inputs
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_UP) #Terminal 1
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP) #Terminal 2
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP) #Terminal 3
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_UP) #Terminal 8

def main():
        try:
                GPIO.add_event_detect(4, GPIO.FALLING, callback=pin4Event, bouncetime=200)
                GPIO.add_event_detect(18, GPIO.FALLING, callback=pin18Event, bouncetime=200)
                GPIO.add_event_detect(17, GPIO.FALLING, callback=pin17Event, bouncetime=200)
                GPIO.add_event_detect(27, GPIO.BOTH, callback=pin27Event, bouncetime=200)

        except KeyboardInterrupt:
                GPIO.cleanup()       # clean up GPIO on CTRL+C exit

        while True:
                time.sleep(10)
def pin4Event(channel):
        pushMessage(p,"Alert Aborted","Intruder Alarm Aborted",0)
        logging.info("Intruder Alarm Aborted")

def pin18Event(channel):
        pushMessage(p,"Confirmed Alarm","Intruder Alarm Confirmed",2)
        logging.info("Intruder Alarm Confirmed")

def pin17Event(channel):
        pushMessage(p,"Intruder Alert","Intruder Alert Triggered",1)
        logging.info("Intruder Alert Triggered")

def pin27Event(channel):
    if GPIO.input(27):
        pushMessage(p,"Armed","Alarm Armed",0)
        logging.info("Alarm Armed")
    else:
        pushMessage(p,"Disarmed","Alarm Disarmed",0)
        logging.info("Alarm Disarmed")

def pushMessage(instance,event,description,pr):
       instance.push("alarmPi",event,description,priority=pr)

#Invoke main function
if __name__ == "__main__":
        main()
