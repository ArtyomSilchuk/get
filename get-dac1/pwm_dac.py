import RPi.GPIO as GPIO

dynamic_range = 3.25

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_freq, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_freq = pwm_freq
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpio_pin, GPIO.OUT, initial=0)
        self.pwm = GPIO.PWM(self.gpio_pin, self.pwm_freq)
        self.pwm.start(0)

    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup

    def set_voltage(self, voltage):
        if not (0<=voltage<=self.dynamic_range):
            print("U вне диапазона, повторите ввод")
        else:
            self.pwm.ChangeDutyCycle(voltage/dynamic_range * 100)

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, dynamic_range, True)

        while True:
            try:
                voltage = float(input("Введите напряжение: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Можно вводить только числа")

    finally:
        dac.deinit()