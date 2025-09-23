import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

leds = [24,22,23,27,17,25,12,16]
aleds = [16,12,25,17,27,23,22,24]
light_time = 0.2

for led in leds:
    GPIO.setup(leds, GPIO.OUT)
    GPIO.output(leds,0)
i = 0
try:
    while True:

        for led in leds:
            GPIO.output(led, 1)
            time.sleep(light_time)
            GPIO.output(led, 0)

        for led in aleds:
            GPIO.output(led, 1)
            time.sleep(light_time)
            GPIO.output(led, 0)
        i += 1
except KeyboardInterrupt():

    GPIO.cleanup()