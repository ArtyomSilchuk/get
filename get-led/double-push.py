import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16,12,25,17,27,23,22,24]
up = 9
down = 10
for led in leds:
    GPIO.setup(led, GPIO.OUT)

GPIO.setup(up, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(down, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
num = 0
sleep_time = 0.2

def dec2bin(value):
    binary_str = bin(value)[2:].zfill(8)
    return [int(bit) for bit in binary_str]

def update_leds(value):
    binary_value = dec2bin(value)
    for i in range(8):
        GPIO.output(leds[i], binary_value[i])
    print(value, binary_value)

def all_leds_on():
    for i in range(8):
        GPIO.output(leds[i], GPIO.HIGH)

def all_lend_off():
    update_leds(num)


try:
    while True:

        if GPIO.input(up) and GPIO.input(down):
            time.sleep(0.05)
            if GPIO.input(up) and GPIO.input(down):
                all_leds_on()
                time.sleep(sleep_time)
                while GPIO.input(up) or GPIO.input(down):
                    all_leds_off()
                    time.sleep(0.1)

        elif GPIO.input(up):
            time.sleep(0.05)
            if GPIO.input(up):
                num = (num + 1) % 256
                update_leds(num)
                time.sleep(sleep_time)
                

        elif GPIO.input(down):
            time.sleep(0.05)
            if GPIO.input(down):
                num = (num - 1) % 256
                update_leds(num)
                time.sleep(sleep_time)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Программа завершена")
