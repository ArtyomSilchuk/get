import RPi.GPIO as GPIO

R2Rpins = [16, 20, 21, 25, 26, 17, 27, 22]
dynamic_range = 3.15

def dec2bin(integer):
    return [int(el) for el in bin(integer)[2:].zfill(8)]

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = R2Rpins
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)
    
    def set_number(self, number):
        binary = dec2bin(number)
        for i in range(8):
            GPIO.output(self.gpio_bits[i], binary[i])

    def set_voltage(self, voltage):
        if not (0<=voltage<=self.dynamic_range):
            print("U вне диапазона, повторите ввод")
        else:
            number = int(voltage/self.dynamic_range * 255)
            R2R_DAC.set_number(self, number)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup

if __name__ == "__main__":
    try:
        dac = R2R_DAC(R2Rpins, dynamic_range, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Можно вводить только числа")

    finally:
        dac.deinit()