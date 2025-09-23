import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)
tran = 6
GPIO.setup(tran, GPIO.IN)


while True:
    state = GPIO.input(tran)
    state = not state
    GPIO.output(led, state)