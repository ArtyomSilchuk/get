import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

R2Rpins = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(R2Rpins, GPIO.OUT)

dynamic_range = 3.184

def voltage_to_number(voltage):
    if not (0 <= voltage <= dynamic_range):
        print("Напряжение не в диапазоне цап (0.0 -", dynamic_range, "В), установлено 0.0")
        return 0
    return int(voltage/dynamic_range * 255)

def dec2bin(integer):
    return [int(el) for el in bin(integer)[2:].zfill(8)]

def number_to_dac(integer):
    binary = dec2bin(integer)
    for i in range(8):
        GPIO.output(R2Rpins[i], binary[i])

try:
    while True:
        try:
            voltage = float(input("Напряжение: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)
        except ValueError:
            print("Можно вводить только числа: ")

finally:
    GPIO.output(R2Rpins, 0)
    GPIO.cleanup()