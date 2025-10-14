import smbus

dynamic_range = 5.25

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = False):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()

    def set_number(self, number):
        if not isinstance(number, int):
            print("Можно вводить только целые числа")
        if not (0 <= number <= 4095):
            print("Число выходит за разрядность MCP4752 (12 бит)")
        
        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]")
        
    def set_voltage(self, voltage):
        if not (0<=voltage<=self.dynamic_range):
            print("U вне диапазона, повторите ввод")
        else:
            number = int(voltage/self.dynamic_range * 4096)
            MCP4725.set_number(self, number)

if __name__ == "__main__":
    try:

        dac = MCP4725(dynamic_range)
        
        while True:
            try:
                voltage = float(input("Введите напряжение: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Можно вводить только числа")

    finally:
        dac.deinit()